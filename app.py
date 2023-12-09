import asyncio
import websockets
from binance import AsyncClient, BinanceSocketManager
from config import Config
import json


async def handle_websocket(websocket, path):
    config = Config()
    multiplex_socket_symbols = [x.lower() + "@kline_1m" for x in config.symbols]
    print("WebSocket connected")
    client = await AsyncClient.create()
    binance_socket_manager = BinanceSocketManager(client)
    multiplex_socket = binance_socket_manager.multiplex_socket(multiplex_socket_symbols)
    async with multiplex_socket as stream:
        while True:
            try:
                socket_info = await stream.recv()
                await websocket.send(json.dumps(socket_info))
            except asyncio.TimeoutError:
                continue
            except websockets.exceptions.ConnectionClosed:
                pass
            except Exception as e:
                print(f"Error in handle_websocket: {e}")

async def main():
    server = await websockets.serve(handle_websocket, "127.0.0.1", 9000)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
