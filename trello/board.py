#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Board(object):
    """
    Class Board in trello
    """

    def __init__(self, board_id, client):
        self.id = board_id
        self.client = client

    def fetch(self):
        """ Fetch all attributes """
        json_obj = self.client.get_json("/boards/" + self.id)

        self.name = json_obj["name"]
