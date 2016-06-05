#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Card(object):
    """
    Card class in trello
    """

    def __init__(self, client, card_id, name="", dateLastActivity=""):
        self.id = card_id

        self.client = client
        self.name = name
        self.dateLastActivity = dateLastActivity

    def __repr__(self):
        return self.name

    def fetch(self):
        """ Fetch all attributes """
        json_obj = self.client.fetch_json("/cards/" + self.id)

        self.name = json_obj["name"]
        self.dateLastActivity = json_obj["dateLastActivity"]

    def set_name(self, name):
        self.client.fetch_json("/cards/" + self.id + "/name", "PUT", {"value": name})
        self.name = name

    def set_closed(self, closed):
        self.client.fetch_json("/cards/" + self.id + "/closed", "PUT", {"value": closed})
        self.closed = closed
