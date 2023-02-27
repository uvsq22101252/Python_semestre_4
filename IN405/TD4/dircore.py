#!/usr/bin/python3

import os
import tempfile
import unittest

def mode_octal_to_str(octal_value):
    if octal_value == :
        

    raise NotImplementedError

def mode_str_to_octal(str_value):
    raise NotImplementedError

def change_mode(path_in, new_mode):
    raise NotImplementedError

def touch(path_in):
    raise NotImplementedError

def dir_list(path_in):
    raise NotImplementedError

def dir_all_list(path_in):
    raise NotImplementedError

def dir_rec_list(path_in):
    raise NotImplementedError

class TestSimpleDirList(unittest.TestCase):
    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as folder:
            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_files(self):
        with tempfile.TemporaryDirectory() as folder:
            files = [tempfile.NamedTemporaryFile(dir=folder) for _ in range(2)]
            for file in files:
                file.flush()

            prev = os.dup(1)
            os.close(1)
            _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
            dir_rec_list(folder)
            os.dup2(prev, 1)

            for file in files:
                file.close()

        with open('__buffer__') as exec_res:
            good_lines = [os.path.basename(file.name) + '\n' for file in files]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')

    def test_two_dirs(self):
        with tempfile.TemporaryDirectory() as folder_A:
            file_A = tempfile.NamedTemporaryFile(dir=folder_A)
            file_A.flush()

            with tempfile.TemporaryDirectory(dir=folder_A) as folder_B:
                file_B = tempfile.NamedTemporaryFile(dir=folder_B)
                file_B.flush()

                prev = os.dup(1)
                os.close(1)
                _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
                dir_rec_list(folder_A)
                os.dup2(prev, 1)

                file_A.close()
                file_B.close()

        with open('__buffer__') as exec_res:
            fol_base_A = os.path.basename(folder_A)
            fol_base_B = os.path.basename(folder_B)
            good_lines = [
                os.path.basename(file_A.name) + "\n",
                fol_base_B + "\n",
                fol_base_B + "/" + os.path.basename(file_B.name) + "\n"
            ]
            good_lines.sort()
            exec_lines = exec_res.readlines()
            exec_lines.sort()
            self.assertListEqual(good_lines, exec_lines)

        os.unlink('__buffer__')