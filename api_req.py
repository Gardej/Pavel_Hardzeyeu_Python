#!/usr/bin/env python

import requests
import argparse
import getpass

user = "Gardej"
passwd = getpass.getpass()

# I have tested it with -user_name "alenaPy" and -repo "devops_lab".
parser = argparse.ArgumentParser()
parser.add_argument('-user_name', nargs=1, help="write user name", required=True)
parser.add_argument('-repo', nargs=1, help="write name of repo", required=True)
parser.add_argument('-req', action="store_true",
                    help="request names and last request update")
parser.add_argument('-basic', action="store_true",
                    help="basic account info")
parser.add_argument('-forks', action="store_true",
                    help="forks info: owners, default branch, number of branches")
parser.add_argument('-v', action="version", version="version 0.0.7")
args = parser.parse_args()

url = "https://api.github.com"
basic_info = requests.get(url + '/user', auth=(user, passwd))
pulls_info = requests.get(
    url + '/repos/' + args.user_name[0] + '/' + args.repo[0] + '/pulls', auth=(user, passwd))
stats_info = requests.get(
    url + '/repos/' + args.user_name[0] + '/' + args.repo[0] + '/forks', auth=(user, passwd))
data1 = basic_info.json()
data2 = pulls_info.json()
data3 = stats_info.json()

if args.req:
    for i, j in enumerate(data2):
        print("Last title: %s - \n last update: %s" % (
            data2[i]["title"],
            data2[i]["updated_at"]))
elif args.basic:
    print("Name: %s " % data1["login"])
    print("ID: %s " % data1["id"])
    print("Creation data: %s " % data1["created_at"])
elif args.forks:
    for i, j in enumerate(data3):
        print("Owners full name: %s" % data3[i]["full_name"])
        print("Default_branch: %s" % data3[i]["default_branch"])
        print("Number of forks: %s" % data3[i]["forks_count"])
else:
    print("No arguments! Please enter the argument. For help info please enter ""-h"".")
