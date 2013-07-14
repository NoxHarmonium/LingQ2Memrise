#!/bin/python
# Requires python-requests. On Fedora I just ran 'yum install python-requests'

# The command line version for testing it out
import argparse, requests, json, sys
from urlparse  import urljoin

# Constants
LINGQ_API_URL = "https://www.lingq.com/api/"
LINGQ_API_PROFILE = "profile"
LINGQ_API_LESSONS = "{0}/lessons/"

parser = argparse.ArgumentParser(description='Copy LingQs into Memrise')
parser.add_argument('lingQApiKeyPath',
                   help='The filename containing the API key for LingQ')

args = parser.parse_args()

f=open(args.lingQApiKeyPath, "r")
lingQApiKey = f.read();

headers = {'Authorization': 'Token ' + lingQApiKey }
#print ("Header: {0}".format('Authorization: Token ' + lingQApiKey))

# Access profile
url = urljoin(LINGQ_API_URL, LINGQ_API_PROFILE)
response = requests.post(url, headers=headers)

if (response.status_code != requests.codes.ok):
    print "Error accessing API:"
    response.raise_for_status()

data = response.json()
language = data["language"]

print "Profile download successful\n"
print "Language: {0}".format(language)
print "level: {0}".format(data["level"])
print "Locale: {0}".format(data["locale"])
print "Time Zone: {0}".format(data["time_zone"])
print "Native Language: {0}".format(data["native_language"])
print "Dictionary Locale: {0}".format(data["dictionary_locale"])
print "Points: {0}\n".format(data["points"])

print "Is this the correct account? [Y/n]"
choice = raw_input().lower().strip()
if (choice == "n"):
    sys.exit(0)
    




