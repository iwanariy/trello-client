#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import get_config

CONFIG = "./config.cfg"


def get_credential():
    """ Get crediential for trello """
    config = get_config(CONFIG)

    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    return username, key, token


if __name__ == u"__main__":
    print(get_credential())
