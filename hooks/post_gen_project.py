#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath):
    shutil.rmtree(dirpath)


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' not in ['y', 'yes']:
        remove_file('AUTHORS.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.test_suite }}' not in ['y', 'yes']:
        remove_file('conftest.py')
        remove_dir('tests/')

    if '{{ cookiecutter.admin_module }}' not in ['y', 'yes']:
        remove_dir('{{cookiecutter.project_core_dir}}/admin_module')
