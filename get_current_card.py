#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import TrelloClient, get_boards
from trello import Board
from trello import get_config

CONFIG = "./config.cfg"


if __name__ == u"__main__":
    config = get_config(CONFIG)
    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    client = TrelloClient(key, token)

    # Get "Private" board
    boards = get_boards(username, client)
    board_id = boards["Private"]
    board = Board(board_id, client)

    # Get "Doing" board
    board.fetch()
    lists = board.get_lists()
    lists[1].fetch()

    # Get current card
    cards = lists[1].get_cards()
    try:
        print(cards[0].name)
    except:
        print("nothing :)")
