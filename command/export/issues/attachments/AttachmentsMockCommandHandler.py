from export.issues.attachments import mock_dir


class AttachmentsMockCommandHandler:

    def __call__(self, *args, **kwargs):
        if len(args) < 1:
            raise ValueError('Expecting at least 1 argument, got 0')

        cmdline_args = args[0]
        if 'path' not in cmdline_args:
            raise ValueError('Parameter "path" is required!')

        # take only the arguments known to the mock_dir function
        known_arguments = {'project_key',
                           'num_issues',
                           'num_attachments_per_issue',
                           'fileattachment_table_csv_export',
                           'dates_hours_diff'}

        kwargs = {k: v for k, v in cmdline_args.__dict__.items() if k in known_arguments}
        mock_dir(cmdline_args.path, **kwargs)
