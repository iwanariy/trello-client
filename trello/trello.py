#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "../config.ini"
base_url = "https://api.trello.com"
api_members = "/1/members/{0}/boards"
key_token = "key={0}&token={1}"

import configparser
import sys
import requests


def get_config(path):
    """ Get config object """
    config = configparser.ConfigParser()

    try:
        config.read(path)
        return config
    except Exception as e:
        print(e)
        sys.exit(1)


def get_boards(username, key, token):
    """ Get hash of board name and id """
    boards = {}

    # Get json
    url = base_url + api_members.format(username) + "?" + key_token.format(key, token) + "&fields=name"
    r = requests.get(url)

    for record in r.json():
        id = record["id"]
        name = record["name"]
        boards[name] = id

    return boards


if __name__ == u"__main__":
    config = get_config(CONFIG)
    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    get_boards(username, key, token)
