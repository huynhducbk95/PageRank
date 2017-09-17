import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict
import os
from models import Page_Obj

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
page_path = DIR_PATH + '/data/viwiki-20170901-page.sql'
pagelink_path = DIR_PATH + '/data/viwiki-20170901-pagelinks.sql'


def parse(pagelink_path):
    file_page = open("pages.txt", "w")

    with open(page_path) as infile:
        for line in infile:
            if line.split(' ')[0] == 'INSERT':
                list_record = line.split('(')
                for record in list_record:
                    page_id = record.split(',')[0]
                    page_namespace = record.split(',')[1]
                    page_title = record.split(',')[2]
                    file_page.write('id: {} -- nspace: {} -- title: {}\n'.format(page_id, page_namespace, page_title))

    file_page.close()

    file_pagelink = open("pagelinks.txt", "w")

    with open(pagelink_path) as infile:
        for line in infile:
            if line.split(' ')[0] == 'INSERT':
                list_record = line.split('(')
                for record in list_record:
                    id_from = record.split(',')[0]
                    namespace_from = record.split(',')[1]
                    title_to = record.split(',')[2]
                    namespace_to = record.split(',')[3]
                    file_pagelink.write('{} \n'.format(record))

    file_pagelink.close()


parse(pagelink_path)
