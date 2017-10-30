from __future__ import print_function

import pip
pip.main(['install', '--upgrade', 'google-api-python-client'])

import httplib2
import os

from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly",
          "https://www.googleapis.com/auth/spreadsheets"]
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


# helper function
def get_service():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        service, the obtained service based off the credentials.
    """
    home_dir = os.path.expanduser("~")
    credential_dir = os.path.join(home_dir, ".credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   "sheets.googleapis.com-python-quickstart.json")

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print("Storing credentials to " + credential_path)

    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ("https://sheets.googleapis.com/$discovery/rest?"
                    "version=v4")
    service = discovery.build("sheets", "v4", http=http,
                          discoveryServiceUrl=discoveryUrl)
    return service


# Converts integer index into a letter for Sheet coordinates
def letter(index):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[index]


class SheetManager:

    # Shared Service Object
    service = get_service()


    # Constructor
    def __init__(self, doc_id):
        # Set internal Doc ID
        self.doc_id = doc_id
        # Read the first row of the sheet (headers)
        self.headers = self.read("1:1")[0]


    # Returns array of values in the given range
    # Data is organized as: list of (list of rows), i.e. data[row][column]
    def read(self, range_in):
        result = self.service.spreadsheets().values().get(
                spreadsheetId=self.doc_id, range=range_in).execute()
        return result.get('values', [])

    # suppy an array of [[row], [row], ... ]
    def write(self, range_in, values):
        body = {
            "values": values
        }
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.doc_id, range=range_in,
            valueInputOption="RAW", body=body).execute()


    # Searches first row (header) for specified label
    # returns number index of desired column
    def get_column_index(self, label):
        try:
            return self.headers.index(label)
        except:
            # Not found
            return -1


    def get_column_letter(self, label):
        return letter(self.get_column_index(label))

    def get_headers_length(self):
        return len(self.headers)


