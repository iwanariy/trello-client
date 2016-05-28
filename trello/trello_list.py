#!/usr/bin/env python
# -*- coding: utf-8 -*-


class List(object):
    """
    Class List in trello
    """

    def __init__(self, list_id, client):
        self.id = list_id
        self.client = client

    def fetch(self):
        """ Fetch all attributes """
        json_obj = self.client.get_json("/lists/" + self.id)

        self.name = json_obj["name"]
        self.closed = json_obj["closed"]
        self.pos = json_obj["pos"]
