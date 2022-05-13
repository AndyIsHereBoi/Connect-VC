from websocket import WebSocket
from json import dumps
import time, json

token = "your token here

socket = WebSocket()


socket.connect("wss://gateway.discord.gg/?v=9&encoding=json")
socket.send(dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
print(f"connected with \"{token}\"")
while True:
    print(ws.recv())
