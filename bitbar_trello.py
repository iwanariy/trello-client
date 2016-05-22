#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "./config.ini"

import configparser
import sys


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
    pass
