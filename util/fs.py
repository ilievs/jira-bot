import os


def mkdir_if_not_exists(path):
    try:
        # create the directory if it doesn't already exist
        os.mkdir(path)
    except FileExistsError:
        # ignore the error, this means the path exists
        pass