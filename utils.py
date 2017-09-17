import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict
import os
from models import Page_Obj

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
page_path = DIR_PATH + '/data/viwiki-20170901-page.sql'
pagelink_path = DIR_PATH + '/data/viwiki-20170901-pagelinks.sql'


def parse(page_path, pagelink_path):
    page_file = open(page_path, "r")
    pagelink_file = open(pagelink_path, 'r')

    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines
    page_lines = page_file.readlines()
    pagelink_lines = pagelink_file.readlines()

    page_count = 0
    for line in page_lines:
        if line.startswith('INSERT INTO'):
            page_count = page_count + 1

    pagelink_count = 0
    for line in pagelink_lines:
        if line.startswith('INSERT INTO'):
            pagelink_count = pagelink_count + 1


    ## close the file after reading the lines.
    page_file.close()
    pagelink_file.close()


parse(page_path, pagelink_path)


def parse_page_line(line_sting):
    list_record = line_sting.split('(')
    
    pass

def parse_page_line(line_sting):
    pass
