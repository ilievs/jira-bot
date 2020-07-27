import argparse

from argparse import ArgumentDefaultsHelpFormatter

import logger

from command.attachments import AttachmentsMockCommandHandler


class Application:

    def run(self):
        # top level parser
        parser = argparse.ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
        subparsers = parser.add_subparsers(title='subcommands', description='Choose a command')

        # attachments subcommand
        attachment_parser = subparsers.add_parser('attachments', help='Use a subcommand')
        attachment_subparsers = attachment_parser.add_subparsers()

        # attachments mock subcommand
        mock_parser = attachment_subparsers.add_parser('mock',
                                                       help='Creates a directory with mocked issue folders '
                                                            'and attachments in them',
                                                       formatter_class=ArgumentDefaultsHelpFormatter)
        mock_parser.add_argument('--project_key', help='the project key', default='ABC')
        mock_parser.add_argument('--num_issues', help='the number of issue folders to create', default=10)
        mock_parser.add_argument('--num_attachments_per_issue',
                                 help='the number of attachment folders to create in each issue folder',
                                 default=2)
        mock_parser.add_argument('--fileattachment_table_csv_export_file_name',
                                 help='the name of the mocked csv file with the fileattachment table export',
                                 default='fileattachment.csv')
        mock_parser.add_argument('--dates_hours_diff',
                                 help='the hour difference acting as a timezone for the dates in the attachment '
                                      'file names and csv export. Values is between -24 and +24. Examples: -1, +3, 0',
                                 default=0,
                                 type=int)
        mock_parser.add_argument('path', help='The path where the mock directory will be created')
        mock_parser.set_defaults(exec=AttachmentsMockCommandHandler())

        args = parser.parse_args()
        try:
            args.exec(args)
        except AttributeError:
            logger.info('Please, choose a command or chain of subcommands. Use -h or --help for more details')


if __name__ == '__main__':
    app = Application()
    app.run()
