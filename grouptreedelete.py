import requests
import argparse
import json


def getchildgroups(parentgroup):

    groupurl = f"{url}/api/Groups?$filter=ParentGroupId eq {parentgroup}"

    parentrequest = requests.get(groupurl, headers=apiheaders)

    childgroupstext = parentrequest.text

    childrenparsed = json.loads(childgroupstext)

    for i in childrenparsed:

        if i != "[]":

            getchildgroups(i["Id"])

            deletehistoricals(i["Id"])

            deletegroup(i["Id"])

        else:

            deleteattendances(i["Id"])

            deletehistoricals(i["Id"])

            deletegroup(i["Id"])


def deleteattendances(group):

    occurrencesurl = f"{url}/api/AttendanceOccurrences?$filter=GroupId eq {group}"

    occurrencesrequest = requests.get(occurrencesurl, headers=apiheaders)

    occurrencestext = occurrencesrequest.text

    occurrencesparsed = json.loads(occurrencestext)

    for i in occurrencesparsed:

        occurrenceid = i["Id"]

        if i != "[]":

            attendanceurl = (
                f"{url}/api/Attendances?$filter=OccurrenceId eq {occurrenceid}"
            )

            attendancerequest = requests.get(attendanceurl, headers=apiheaders)

            attendancetext = attendancerequest.text

            attendanceparsed = json.loads(attendancetext)

            for j in attendanceparsed:

                attendanceid = j["Id"]

                deleteattendanceurl = f"{url}/api/Attendances/{attendanceid}"

                requests.delete(deleteattendanceurl, headers=apiheaders)

            deleteoccurrenceurl = f"{url}/api/AttendanceOccurrence/{occurrenceid}"

            requests.delete(deleteoccurrenceurl, headers=apiheaders)

        else:

            deleteoccurrenceurl = f"{url}/api/AttendanceOccurrence/{occurrenceid}"

            requests.delete(deleteoccurrenceurl, headers=apiheaders)


def deletegroup(group):

    groupurl = f"{url}/api/Groups/{group}"

    changegrouptypedata = """{ 
        "GroupTypeId": 357
    }"""

    requests.patch(groupurl, changegrouptypedata, headers=apiheaders)

    requests.delete(groupurl, headers=apiheaders)


def deletehistoricals(group):

    historicalurl = f"{url}/api/GroupHistoricals?$filter=GroupId eq {group}"

    historicalrequest = requests.get(historicalurl, headers=apiheaders)

    historicaltext = historicalrequest.text

    historicalparsed = json.loads(historicaltext)

    for h in historicalparsed:

        historicalid = h["Id"]

        deletehistoricalurl = f"{url}/api/GroupHistoricals/{historicalid}"

        requests.delete(deletehistoricalurl, headers=apiheaders)


# Initialize argparse

parser = argparse.ArgumentParser()

"""Argument Parser:
    --rockurl: Rock Server URL
    --apikey: Rock Api Key
    --groupid:  Top level group to delete , all groups and attendance below this 
                group will be deleted as well
"""

parser.add_argument(
    "-u", "--rockurl", required=True, type=str, help="The URL of your Rock server"
)
parser.add_argument("-k", "--apikey", required=True, type=str, help="Your Rock API key")
parser.add_argument(
    "-g",
    "--groupid",
    required=True,
    type=str,
    help="The group id that you wish to delete",
)

args = parser.parse_args()

url = args.rockurl

key = args.apikey

apiheaders = {"Content-Type": "application/json", "Authorization-Token": key}

toplevelgroup = args.groupid

getchildgroups(toplevelgroup)

deletegroup(toplevelgroup)

