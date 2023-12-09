import asyncio
import websockets
import json

async def connect_and_print():
    uri = "ws://127.0.0.1:9000"  # Замініть це на адресу вашого WebSocket сервера
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received: {json.loads(message)}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_and_print())
