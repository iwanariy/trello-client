#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import get_config
import os

CONFIG = "./config.cfg"


def get_credential():
    """ Get crediential for trello """
    config = get_config(CONFIG)

    # env
    username = os.getenv("TRELLO_USERNAME")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    if username and key and token:
        pass
    else:
        username = config.get("trello", "username")
        key = config.get("trello", "key")
        token = config.get("trello", "token")

    return username, key, token


if __name__ == u"__main__":
    print(get_credential())
