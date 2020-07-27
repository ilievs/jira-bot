from attachments.export import export


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

        export(cmdline_args.attachments_path,
               cmdline_args.fileattachment_table_csv_export_file,
               cmdline_args.target_path)
