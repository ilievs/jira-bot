import csv
import os
import shutil

import logger
from util.fs import mkdir_if_not_exists


def get_mapping_fileattachment_export_csv(fileattachment_table_csv_export_file, csv_separator):
    attachments_mapping = {}
    with open(fileattachment_table_csv_export_file) as f:
        line_num = 1
        for row in csv.reader(f, delimiter=csv_separator):
            if len(row) != 9:
                raise ValueError(f'Line {line_num} in the fileattachment csv export file '
                                 f'{fileattachment_table_csv_export_file} is corrupt or '
                                 f'is exported from an unsupported Jira version')

            attachment_id = row[0]
            attachment_file_name = row[3]
            attachments_mapping[attachment_id] = attachment_file_name

            line_num += 1

    return attachments_mapping


def export_issue(issue_attachments_path, target_path, attachments_mapping, fileattachment_table_csv_export_file):
    for attachment_file_name in os.listdir(issue_attachments_path):
        attachment_file = f'{issue_attachments_path}/{attachment_file_name}'
        if os.path.isfile(attachment_file):
            if attachment_file_name in attachments_mapping:
                new_attachment_file_name = attachments_mapping[attachment_file_name]
                new_file_path = f'{target_path}/{new_attachment_file_name}'
                shutil.copyfile(attachment_file, new_file_path)
            else:
                logger.warning(f'attachment {attachment_file} does not contain a mapping in '
                               f'{fileattachment_table_csv_export_file}')


def export(attachments_path, fileattachment_table_csv_export_file, target_path, fileattachment_csv_separator=','):

    mkdir_if_not_exists(target_path)

    # the directory might have existed, so check if it's empty
    if os.listdir(target_path):
        raise ValueError(f'Target path {target_path} not empty!')

    attachments_mapping = get_mapping_fileattachment_export_csv(fileattachment_table_csv_export_file,
                                                                fileattachment_csv_separator)

    for issue_folder in os.listdir(attachments_path):
        issue_path = f'{attachments_path}/{issue_folder}'
        if os.path.isdir(issue_path):
            new_issue_path = f'{target_path}/{issue_folder}'
            mkdir_if_not_exists(new_issue_path)
            export_issue(issue_path, new_issue_path, attachments_mapping, fileattachment_table_csv_export_file)
