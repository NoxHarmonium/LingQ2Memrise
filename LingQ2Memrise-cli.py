#!/bin/python
# Requires python-requests. On Fedora I just ran 'yum install python-requests'

# The command line version for testing it out
import argparse, requests, json, sys
from urlparse  import urljoin

# Constants
LINGQ_API_URL = "https://www.lingq.com/api/"
LINGQ_API_PROFILE = "profile"
LINGQ_API_LESSONS = "languages/{0}/lessons"
LINGQ_API_LESSON_LINGQS = "languages/{0}/lessons/{1}/lingqs/"

# Functions
def dump(filename, text):
    f = open(filename, 'w')
    f.write(text)
    f.close()


# Main
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
response = requests.get(url, headers=headers)

if (response.status_code != requests.codes.ok):
    print "Error accessing API:"
    response.raise_for_status()

data = None

try:
    data = response.json()
except ValueError:
    print "Could not read json. Dumping response to dump.html"
    dump("dump.html",response.text.encode('utf8'))
    exit(1);

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
    
print "Loading lessons for language: {0}...".format(language)
url = urljoin(LINGQ_API_URL, LINGQ_API_LESSONS.format(language))
print ("Url: {0}".format(url))

response = requests.get(url, headers=headers)

if (response.status_code != requests.codes.ok):
    print "Error accessing API:"
    response.raise_for_status()

lessons = None
try:
    lessons = response.json()
except ValueError:
    print "Could not read json. Dumping response to dump.html"
    dump("dump.html",response.text.encode('utf8'))
    exit(1);



for lesson in lessons:
    id = lesson["id"]
    title = lesson["title"]
    print u"Lesson: {0} (ID: {1})".format(title,id)
    url = urljoin(LINGQ_API_URL, LINGQ_API_LESSON_LINGQS.format(language, id))
    
    print ("URL: {0}".format(url))
    
    response = requests.get(url, headers=headers)

    if (response.status_code != requests.codes.ok):
        print "Error accessing API:"
        response.raise_for_status()

    lingQs = None
    try:
        lingQs = response.json()
    except ValueError:
        print "Could not read json. Dumping response to dump.html"
        dump("dump.html",response.text.encode('utf8'))
        exit(1);
    
    print "{0} linqs were found:".format(len(lingQs))
        
    for lingQ in lingQs:
        print u"\tLingQ: {0}".format(lingQ["term"])
        
    print "Done\n"



