import line_notify
import google_calendar_api


def lambda_handler(event, context):
    line_notify.line(google_calendar_api.get_events())

