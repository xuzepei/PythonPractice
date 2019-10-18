
#sudo pip install Pillow

#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from array import *
import json
import os
import sys
import argparse
from github import Github

# Read json file
def init():
    get_branches("xuzepei/UKRadio")

def get_branches(repo_name):
    repo = _g.get_repo(repo_name)
    for branch in list(repo.get_branches()):
        print(branch.name)
        print(branch.commit.commit.author.name + ": " + branch.commit.commit.message)
        print(branch.commit.commit.committer.date)


_MODE = 'test'
_CONFIG_FILENAME = 'items.json'
_g = Github("a319389097bc4ca7e576d2222289086e42c03c94")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage="It's a tip.", description="help info.")
    parser.add_argument("-m", "--mode", choices=['test', 'pro'], default="test", help="Input mode, test or production")
    #parser.add_argument("-mode", type=string, required=True, help="Input ")
    #parser.add_argument("-l", "--log", default=False, action="store_true", help="active log info.")
 
    args = parser.parse_args()
    #print(">>>>>>>>>upload.py --mode {0}".format(args.mode))
    _MODE = args.mode
    init()



