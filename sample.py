#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = "./config.ini"


from trello.trello_client import TrelloClient, get_boards
from trello.board import Board
from trello.util import get_config


if __name__ == u"__main__":
    config = get_config(CONFIG)
    username = config.get("trello", "username")
    key = config.get("trello", "key")
    token = config.get("trello", "token")

    client = TrelloClient(key, token)

    boards = get_boards(username, client)

    board_id = boards["Private"]
    board = Board(board_id, client)

    board.fetch()
    lists = board.get_lists()
