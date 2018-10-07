from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime


def get_events():
    # Setup the Calendar API
    # SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    tomorrow = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='SET_YOUR_CALENDAR_ID', timeMin=now,
                                          timeMax=tomorrow, maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    events_list = ""

    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date')).replace(":00+09:00","")
        start = start.replace('T', ' ')
        events_list = events_list + '\n' + start + '\n' + event['summary'] + '\n'
    return events_list


if __name__ == '__main__':
    print(get_events())
