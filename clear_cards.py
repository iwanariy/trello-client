#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from __future__ import print_function
from trello import TrelloClient, get_boards
from trello import Board
import os
import util
import dateutil.parser
import datetime
import pytz
import logging


DAYS = int(os.getenv("DAYS", 1))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def archive_cards(board_name="Private", list_name="Done", days=1):
    """ archive cards """
    username, key, token = util.get_credential()

    client = TrelloClient(key, token)

    # Get board
    boards = get_boards(username, client)
    board_id = boards[board_name]
    board = Board(board_id, client)

    # Get board
    lists = board.get_lists()
    list_done = [x for x in lists if x.name == list_name][0]
    cards = list_done.get_cards()

    target = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=days)

    for card in _filter_cards(cards, target):
        card.set_closed("true")
        logger.debug(card)


def _filter_cards(cards, day):
    """ filter cards """
    cards_filtered = []

    for card in cards:
        dateLastActivity_datetime = dateutil.parser.parse(card.dateLastActivity)
        if dateLastActivity_datetime < day:
            cards_filtered.append(card)

    return cards_filtered


def lambda_handler(event, context):
    archive_cards(board_name="Private", list_name="Done", days=DAYS)

    return True


if __name__ == u"__main__":
    archive_cards(board_name="Private", list_name="Done", days=DAYS)
