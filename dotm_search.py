#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a directory path, search all files in the path for a given text string
within the 'word/document.xml' section of a MSWord .dotm file.
"""
__author__ = "Joey Brown w/ help from Google and coaches"
from zipfile import ZipFile
import argparse
import os 

def create_parser():
    parser = argparse.ArgumentParser(description='searches dotm files for text')
    parser.add_argument('--dir', help = 'directory to search', default='.')
    parser.add_argument('text', help='text to search for')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print args
    fileList = os.listdir(args.dir)
    print fileList
    total_counter = 0
    match_counter = 0

    for file_1 in fileList:
        if file_1.endswith('dotm'):
            with ZipFile(args.dir+'/'+file_1) as zip:
                with zip.open('word/document.xml') as doc:
                    total_counter += 1
                    line = doc.read()
                    if line.find(args.text) != -1:
                        match_counter +=1
                        print "Match found in file: " + args.dir+'/'+file_1 
                        print line[line.find(args.text)-40:line.find(args.text)+40] + '\n'
    print total_counter
    print match_counter


if __name__ == '__main__':
    main()
