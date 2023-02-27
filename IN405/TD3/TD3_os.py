#!/usr/bin/python3

import os
import tempfile
import unittest

def file_cat(path_in):
    file = os.open(path_in,dir_fd=os.O_RDONLY)
    read = os.read(file,16)
    while len(read) != 0:
        print(read.decode(),end = " ")
        read = os.read(file,16)
    os.close(file)
    raise NotImplementedError

def file_copy(path_in, path_out):
    file_1 = os.open(path_in,dir_fd=os.O_RDONLY)
    file_2 = os.open(path_out,os.O_WRONLY | os.O_CREAT, 0o660)
    read = os.read(file_1,16)
    while len(read) !=0 :
        os.write(file_2, read)
        os.read(file_1, 16)
    os.close(file_1)
    os.close(file_2)
    raise NotImplementedError

def file_move(path_in, path_out):
    os.link(path_in,path_out)
    os.unlink(path_in)
    raise NotImplementedError

def file_find(path, filename):
    find = os.listdir(path)
    for elt in find:
        if elt == filename:
            print(path + "/"+ filename)
        if os.path.isdir(path + "/" + elt) == True:
            file_find(path + "/" + elt, filename)
    raise NotImplementedError

def file_diff(path_a, path_b):
    file_1 = os.open(path_a,os.O_RDONLY)
    file_2 = os.open(path_b,os.O_RDONLY)
    read_file_1 = os.read(file_1,16)
    read_file_2 = os.read(file_2,16)
    while len(read_file_1) !=0 or len(read_file_2) !=0:
        if read_file_1 != read_file_2:
            os.close(file_1)
            os.close(file_2)
            return False
        else:
            os.read(path_a,16)
            os.read(path_b,16)
    os.close(file_1)
    os.close(file_2)
    return True
    raise NotImplementedError


def file_sed_char(path, target, modif):
    file = os.open(path,os.O_RDWR)
    byte_target = bytes(target,'utf-8')
    byte_modif = bytes(modif,'utf-8')
    read = os.read(target,1)
    while len(read)!=0:
        if read == byte_target:
            os.lseek(file, -1,os.SEEK_CUR)
            os.write(file,byte_modif)
        else:
            os.read(target,1)
    os.close(file)
    raise NotImplementedError


def file_sed_string(path, target, modif):
    file = os.open(path,os.O_RDONLY)
    info_b = b''
    read = os.read(file,16)
    while len(read)!= 0:
        info_b += read
        os.read(file,16)
    os.close(file)
    info_b = info_b.decode
    info_b = os.replace(target,modif)
    info_b = info_b.encode('utf-8')
    file = os.open(path,os.O_WRONLY |os.O_TRUNC) #os.O_TRUNC vide l'intégralité du fichier avant d'ecrire dedans
    os.write(file,info_b)
    os.close(file)
    raise NotImplementedError

def file_grep_char(path_in, target):
    file = os.open(path_in,os.O_RDONLY)
    target_b = bytes(target,'utf-8')
    read = os.read(file,1)
    while len(read)!=0 :
        if read == target_b:
            print(os.lseek(read,-1, os.SEEK_CUR))
        else:
            read = os.read(file,1)
    os.close(file)
    raise NotImplementedError
        

def file_grep_string(path_in, target):
    raise NotImplementedError

def file_grep_line(path_in, target):
    file = os.open(path_in,os.O_RDONLY)
    info_b = b''
    read = os.read(file,16)
    while len(read) !=0:
        info_b+= read
        os.read(file,16)
    os.close(file)
    info_b = info_b.decode()
    info_b = info_b.split('\n')
    if target in info_b:
        return True
    else:
        return False
    
    raise NotImplementedError

    

class TestBasicFileGrepString(unittest.TestCase):
    def test_empty_file(self):
        tmp_f = tempfile.NamedTemporaryFile()
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'a')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = []
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)
        
        os.unlink('__buffer__')

    def test_simple_search(self):
        tmp_f = tempfile.NamedTemporaryFile(mode='w')
        tmp_f.writelines([
            "123\n",
            "abc\n",
            "ABC\n"
        ])
        tmp_f.flush()

        prev = os.dup(1)
        os.close(1)
        _ = os.open('__buffer__', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        file_grep_string(tmp_f.name, 'abc')
        os.dup2(prev, 1)

        tmp_f.close()
        with open('__buffer__') as exec_res:
            good_lines = ['1:0\n']
            exec_lines = exec_res.readlines()
            self.assertListEqual(good_lines, exec_lines)
