#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import TrelloClient, get_boards
from trello import Board
from trello import get_config

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
    try:
        list_done = [x for x in lists if x.name == list_name][0]
        cards = list_done.get_cards()
        for card in cards:
            card.set_closed("true")
    except:
        exit()


if __name__ == u"__main__":
    archived_cards(board_name="Private", list_name="Done")
    archived_cards(board_name="Work", list_name="Done")
