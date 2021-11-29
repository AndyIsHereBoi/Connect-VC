import threading, json, webbrowser, json
from websocket import WebSocket
from json import dumps
from threading import Thread
import time

guild_id = input("Enter the server id:\n")
chid = input("Enter the channel id:\n")

tokens = open("tokens.txt", 'r').readlines()
for token in tokens:
    socket = WebSocket()
    socket.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    socket.send(dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    socket.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": False,"self_deaf": True}}))
    socket.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "russia"}}))
    print(f"connected with {token}")
