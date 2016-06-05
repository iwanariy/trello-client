#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trello.trello_list import List


class Board(object):
    """
    Class Board in trello
    """

    def __init__(self, board_id, client):
        self.id = board_id
        self.client = client

    def __repr__(self):
        return self.name

    def fetch(self):
        """ Fetch all attributes """
        json_obj = self.client.fetch_json("/boards/" + self.id)

        self.name = json_obj["name"]

    def get_lists(self):
        """ Get card lists of this board """
        json_obj = self.client.fetch_json("/boards/" + self.id + "/lists")

        lists = []
        for obj in json_obj:
            lists.append(List(self.client, obj["id"]))

        return lists
