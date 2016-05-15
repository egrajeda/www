#!/usr/bin/python
"""
Script que recibe la información de un enlace y lo agrega a la colección, al
mismo tiempo que actualiza o agrega una blog post para reflejar eso en la
página de inicio.
"""

import argparse
import datetime
import json
import re
import subprocess
from pprint import pprint

LINKS_JSON = './_data/enlaces.json'
LINKS_DIRECTORY = './enlaces'
POSTS_DIRECTORY = '%s/_posts' % LINKS_DIRECTORY

def find_last_post_path():
    ps1 = subprocess.Popen(['find', '.', '-path', '*/_posts/*', '-not', '-path', './vendor/*'], stdout=subprocess.PIPE)
    ps2 = subprocess.Popen(['awk', '-vFS=/', '-vOFS=/', '{ print $NF, $0 }'], stdin=ps1.stdout, stdout=subprocess.PIPE)
    ps3 = subprocess.Popen(['sort', '-rnt/'], stdin=ps2.stdout, stdout=subprocess.PIPE)
    ps4 = subprocess.Popen(['cut', '-f2-', '-d/'], stdin=ps3.stdout, stdout=subprocess.PIPE)
    ps5 = subprocess.Popen(['head', '-n1'], stdin=ps4.stdout, stdout=subprocess.PIPE)
    ps1.wait()

    output, err = ps5.communicate()
    return output.decode('utf-8').strip()

def get_post_path_to_update():
    last_post_path = find_last_post_path()
    if LINKS_DIRECTORY in last_post_path:
        return last_post_path
    else:
        return '%s/%s-update.md' % (POSTS_DIRECTORY, datetime.date.today())

def store_link(filename, link):
    with open(filename, 'r+') as data_file:
        data = json.load(data_file)
        data.append(link)

        data_file.seek(0)
        json.dump(data, data_file, indent=2)
        data_file.truncate()

def store_link_post(filename, link):
    with open(filename, 'r+') as post_file:
        m = re.search('counter: (\d*)', post_file.read())
        counter = int(m.group(1)) if m else 0

        post_file.seek(0)
        post_file.write(
"""---
layout: post
title: %s
permalink: %s
counter: %d
sitemap: false
draft: true
---""" % (link['title'], link['url'], counter + 1))
        post_file.truncate()

def create_link(title, url, tags, excerpt):
    m = re.search('public-([a-z]*)', tags)
    category = m.group(1) if m else ''
    return {
        'title': title,
        'excerpt': excerpt,
        'url': url,
        'category': category
    }

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('title', metavar='title', type=str)
    parser.add_argument('url', metavar='url', type=str)
    parser.add_argument('tags', metavar='tags', type=str)
    parser.add_argument('excerpt', metavar='excerpt', type=str)
    args = parser.parse_args()
    return (args.title, args.url, args.tags, args.excerpt)

def main():
    link = create_link(*parse_args())
    store_link(LINKS_JSON, link)
    store_link_post(get_post_path_to_update(), link)

if __name__ == '__main__':
    main()
