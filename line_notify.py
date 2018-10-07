import requests


def line(Me):
    line_notify_token = 'SET_YOUR_TOKEN'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = Me
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)


if __name__ == '__main__':
    line('Hello World!')
