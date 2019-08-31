import requests
import config
from config import URL
from config import ENDPOINT_SOCKET

state = {
    "State": "on"
}

requests.post(URL + ENDPOINT_SOCKET % config.MONITOR_POWER_SOCKET, data=state)
requests.post(URL + ENDPOINT_SOCKET % config.MUSIC_POWER_SOCKET, data=state)
