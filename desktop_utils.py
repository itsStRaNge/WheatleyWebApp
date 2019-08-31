import requests
import argparse
import config
from config import URL
from config import ENDPOINT_SOCKET

parser = argparse.ArgumentParser(description='Wheatley')
parser.add_argument('state', type=str, help='Turning on/off socket')
args = parser.parse_args()

state = {
    "State": args.state
}

requests.post(URL + ENDPOINT_SOCKET % config.MONITOR_POWER_SOCKET, json=state)
requests.post(URL + ENDPOINT_SOCKET % config.MUSIC_POWER_SOCKET, json=state)
