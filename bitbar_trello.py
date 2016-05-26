#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "./config.ini"
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


if __name__ == u"__main__":
    config = get_config(CONFIG)
