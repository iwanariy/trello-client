#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "../config.ini"
base_url = "https://api.trello.com/1"

import requests
import util
from board import Board


class TrelloClient(object):
    """
    Class for connection to trello
    """
    def __init__(self, key, token):
        self.key = key
        self.token = token

    def get_json(self, api):
        """ Get json by using uri """
        uri = base_url + api + "?" + "key={0}&token={1}".format(self.key, self.token)
        r = requests.get(uri)

        return r.json()


def get_boards(username, client):
    """ Get hash of board name and id """
    boards = {}

    json_obj = client.get_json("/members/{0}/boards".format(username))

    for record in json_obj:
        id = record["id"]
        name = record["name"]
        boards[name] = id

    return boards


if __name__ == u"__main__":
    config = util.get_config(CONFIG)
    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    client = TrelloClient(key, token)

    boards = get_boards(username, client)

    board_id = boards["Private"]
    print(board_id)

    board = Board(board_id, client)
    board.fetch()
