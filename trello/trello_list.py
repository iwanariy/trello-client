#!/usr/bin/env python
# -*- coding: utf-8 -*-


from trello.card import Card


class List(object):
    """
    Class List in trello
    """

    def __init__(self, client, list_id, name=""):
        self.id = list_id
        self.client = client
        self.name = name

    def fetch(self):
        """ Fetch all attributes """
        json_obj = self.client.get_json("/lists/" + self.id)

        self.name = json_obj["name"]
        self.closed = json_obj["closed"]
        self.pos = json_obj["pos"]

    def __repr__(self):
        return self.name

    def get_cards(self):
        """ Get all cards for this list """
        json_obj = self.client.get_json("/lists/" + self.id + "/cards")
        print(json_obj)

        cards = []
        for obj in json_obj:
            cards.append(Card(self.client, obj["id"]))

        return cards
