#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "../config.ini"
base_url = "https://api.trello.com/1"
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


def get_json(api, key, token):
    """ Get json by using uri """
    uri = base_url + api + "?" + key_token.format(key, token)
    r = requests.get(uri)

    return r.json()


def get_boards(username, key, token):
    """ Get hash of board name and id """
    boards = {}

    json_obj = get_json("/members/{0}/boards".format(username), key, token)

    for record in json_obj:
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
