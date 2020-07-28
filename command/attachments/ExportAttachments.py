from attachments.export import export


def sanitized_path(path):
    return path[:-1] if path.endswith('/') else path


class ExportAttachments:

    def __call__(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError('Expecting at least 1 argument, got 0')

        cmdline_args = args[0]
        if 'attachments_path' not in cmdline_args:
            raise ValueError('Parameter "path" is required!')

        if 'fileattachment_table_csv_export_file' not in cmdline_args:
            raise ValueError('Parameter "fileattachment_table_csv_export_file" is required!')

        if 'target_path' not in cmdline_args:
            raise ValueError('Parameter "target_path" is required!')

        attachments_path = sanitized_path(cmdline_args.attachments_path)
        fileattachment_table_csv_export_file = sanitized_path(cmdline_args.fileattachment_table_csv_export_file)
        target_path = sanitized_path(cmdline_args.target_path)

        export(attachments_path, fileattachment_table_csv_export_file, target_path)
