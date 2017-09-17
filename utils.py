import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict
import os
from models import Page_Obj

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
page_path = DIR_PATH + '/data/viwiki-20170901-page.sql'
pagelink_path = DIR_PATH + '/data/viwiki-20170901-pagelinks.sql'


def parse(pagelink_path):
    file = open("pages.txt", "w")

    with open(pagelink_path) as infile:
        for line in infile:
            if line.split(' ')[0] == 'INSERT':
                list_record = line.split('(')
                # for record in list_record:
                #     id = record.split(',')[0]
                #
                # file.write('id: {} - title: {} \n'.format(id, title))
                for record in list_record:
                    file.write('record: {} \n'.format(record))

    file.close()

parse(pagelink_path)