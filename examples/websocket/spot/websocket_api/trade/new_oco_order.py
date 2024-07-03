#!/usr/bin/env python

import logging
import time
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_api import SpotWebsocketAPIClient
from examples.utils.prepare_env import get_api_key

api_key, api_secret = get_api_key()

config_logging(logging, logging.DEBUG)


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


my_client = SpotWebsocketAPIClient(
    stream_url="wss://ws-api.testnet.binance.vision/ws-api/v3",
    api_key=api_key,
    api_secret=api_secret,
    on_message=message_handler,
    on_close=on_close,
)


my_client.new_oco_order(
    symbol="BNBUSDT",
    side="BUY",
    quantity=1,
    aboveType="LIMIT_MAKER",
    belowType="LIMIT_MAKER",
    abovePrice=400,
    belowPrice=395,
    listClientOrderId="123",
)

time.sleep(2)

logging.info("closing ws connection")
my_client.stop()
