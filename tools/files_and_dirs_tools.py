import os


def generator_files_in_dir(top_directory, extension=''):
    """
    Генератор имен файлов в некоторой директории
    """

    for root, dirs, files in os.walk(top_directory):
        for filename in filter(lambda tmp: tmp.endswith(extension), files):
            filename_full = os.path.join(root, filename)
            if os.path.isfile(filename_full) is True:
                yield filename_full