import requests
import argparse
import json

def getchildgroups(parentgroup):

    groupurl = f'{url}/api/Groups?$filter=ParentGroupId eq {parentgroup}'

    parentrequest = requests.get(groupurl, headers=apiheaders)

    childgroupsparsed = json.loads(parentrequest.text)


def deleteattendances(group):

    pass
    #Get attendance occurrences

    #Loop through and delete all attendances

    #Delete attendance occurrence


# Initialize argparse

parser = argparse.ArgumentParser()

"""Argument Parser:
    --rockurl: Rock Server URL
    --apikey: Rock Api Key
    --groupid:  Top level group to delete , all groups and attendance below this 
                group will be deleted as well
"""

parser.add_argument("-u", "--rockurl", required=True, type=str,
                    help="The URL of your Rock server")
parser.add_argument("-k", "--apikey", required=True, type=str,
                    help="Your Rock API key")
parser.add_argument("-g", "--groupid", required=True, type=str,
                    help="The group id that you wish to delete")

args = parser.parse_args()

url = args.rockurl

apiheaders = f"{{'Content-Type': 'application/json', 'Authorization-Token': '{args.apikey}'}}"

toplevelgroup = args.groupid



