#!/usr/bin/env PYTHONIOENCODING=UTF-8 python
# -*- coding: utf-8 -*-


from trello import TrelloClient, get_boards
from trello import Board
import util

CONFIG = "./config.cfg"


if __name__ == u"__main__":
    username, key, token = util.get_credential()

    client = TrelloClient(key, token)

    # Get "Private" board
    boards = get_boards(username, client)
    board_id = boards["Private"]
    board = Board(board_id, client)

    # Get "Doing" board
    lists = board.get_lists()

    # Get current card
    cards = lists[1].get_cards()
    try:
        print(cards[0].name)
    except:
        print("nothing :)")
