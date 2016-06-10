#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import TrelloClient, get_boards
from trello import Board
from trello import get_config
import dateutil.parser
import datetime
import pytz

CONFIG = "./config.cfg"


def archived_cards(board_name="Private", list_name="Done"):
    """ archive cards """
    # Load config
    config = get_config(CONFIG)
    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    client = TrelloClient(key, token)

    # Get board
    boards = get_boards(username, client)
    board_id = boards[board_name]
    board = Board(board_id, client)

    # Get board
    lists = board.get_lists()
    list_done = [x for x in lists if x.name == list_name][0]
    cards = list_done.get_cards()

    target = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=1)

    for card in _filter_cards(cards, target):
        card.set_closed("true")


def _filter_cards(cards, day):
    """ filter cards """
    cards_filtered = []

    for card in cards:
        dateLastActivity_datetime = dateutil.parser.parse(card.dateLastActivity)
        if dateLastActivity_datetime < day:
            cards_filtered.append(card)

    return cards_filtered


if __name__ == u"__main__":
    archived_cards(board_name="Private", list_name="Done")
    archived_cards(board_name="Work", list_name="Done")
