from dotenv import load_dotenv
import os


load_dotenv()


class Config():
    def __init__(self) -> None:
        self.symbols = os.environ.get('SYMBOLS', 'BTCUSDT').split(',')