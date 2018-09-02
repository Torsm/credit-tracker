import urllib.parse
import urllib.request
import json
import logging
import time


class Session:
    def __init__(self, session_id, credit = 0, current_date = 0, expiry_date = 0):
        self.session_id = session_id
        self.credit = credit
        self.local_expiry_date = 0
        self.update_time(current_date, expiry_date)

    def update_time(self, current_date, expiry_date):
        self.local_expiry_date = int(time.time()) + (expiry_date - current_date) / 2

    def revalidate(self):
        if self.local_expiry_date > int(time.time()):
            return False

        body = {
            'session_id': self.session_id
        }
        data = request('https://www.runemate.com/client/user/revalidate2.php', body)
        self.credit = data['credit']
        self.update_time(data['current_date'], data['expiry_date'])
        return True

    def close(self):
        body = {
            'session_id': self.session_id
        }
        return request('https://www.runemate.com/client/user/logout.php', body)


def login(username, password, key, jar):
    body = {
        'username': username,
        'password': password,
        'key': key,
        'remember': 0,
        'os': None,
        'jar': jar
    }
    data = request('https://www.runemate.com/client/user/login.php', body)
    return Session(data['session_id'], data['credit'], data['current_date'], data['expiry_date'])


def request(url, body):
    req = urllib.request.Request(
        url=url,
        data=urllib.parse.urlencode(body).encode('UTF-8'),
        headers={'User-Agent': 'RuneMate'},
        method='POST'
    )
    response = urllib.request.urlopen(req).read().decode()
    data = json.loads(response)
    logging.debug(data)
    if 'error' in data:
        print(data['error'])
        logging.error(data['error'])
        raise Exception(data['error'])
    return data
