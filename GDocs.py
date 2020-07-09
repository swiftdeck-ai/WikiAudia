from __future__ import print_function

import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import discovery
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools

ADD_DOC_ID = '1WIbeNB8Y7uQRCcxSNy3xVMsBoRMk6U6wCE6pSmB5vOA'
LOG_DOC_ID = '1tWkIOi65FChxLmAo75hltBDR-XcqwtNtP7yMPWGeIkQ'
SCOPES = ['https://www.googleapis.com/auth/documents']
DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'

global service
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
service = build('docs', 'v1', credentials=creds)


def initToken(id):
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=id).execute()

    print('The title of the document is: {}'.format(document.get('title')))


def addTitle(title, id):
    title += '\n'
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': title
            }
        }]
    result = service.documents().batchUpdate(
        documentId=id, body={'requests': requests}).execute()


def removeTitle(title, id):
    global service

    requests = [
        {
            'replaceAllText': {
                'replaceText': '',
                'containsText': {
                    'text': title,
                    'matchCase': 'False'
                }
            }

        }
    ]
    result = service.documents().batchUpdate(
        documentId=id, body={'requests': requests}).execute()


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth 2.0 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    store = file.Storage('token.json')
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets('creds.json', SCOPES)
        credentials = tools.run_flow(flow, store)
    return credentials


def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')


def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be
            # nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_strucutural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_strucutural_elements(toc.get('content'))
    return text


def getText(id):
    """Uses the Docs API to print out the text of a document."""
    credentials = get_credentials()
    http = credentials.authorize(Http())
    docs_service = discovery.build(
        'docs', 'v1', http=http, discoveryServiceUrl=DISCOVERY_DOC)
    doc = docs_service.documents().get(documentId=id).execute()
    doc_content = doc.get('body').get('content')
    return read_strucutural_elements(doc_content)


if __name__ == '__main__':
    print(getText(LOG_DOC_ID).split('\n'))
