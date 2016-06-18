#!/usr/bin/env python
# -*- coding: utf-8 -*-


base_url = "https://api.trello.com/1"

import requests
import sys
from requests.exceptions import ConnectionError


class TrelloClient(object):
    """
    Class for connection to trello
    """
    def __init__(self, key, token):
        self.key = key
        self.token = token

    def fetch_json(self, api, http_method="GET", params={}):
        """ Get json by using uri """
        uri = base_url + api + "?" + "key={0}&token={1}".format(self.key, self.token)

        try:
            r = requests.request(http_method, uri, params=params)
        except ConnectionError:
            print("[ERROR]\tConnection Error.")
            sys.exit(1)

        return r.json()


def get_boards(username, client):
    """ Get hash of board name and id """
    boards = {}

    json_obj = client.fetch_json("/members/{0}/boards".format(username))

    for record in json_obj:
        id = record["id"]
        name = record["name"]
        boards[name] = id

    return boards


if __name__ == u"__main__":
    pass
