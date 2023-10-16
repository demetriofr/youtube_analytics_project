import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    @staticmethod
    def __api_key():
        """
        Добавляет API key YouTube из переменного окружения операционной системы
        """
        # YT_API_KEY копируется из Google и добавляется в переменные окружения
        __api_key: str = os.getenv('YT_API_KEY')
        return __api_key

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=__api_key())

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # Выводит словарь в json-подобном удобном формате с отступами
        print(json.dumps(channel, indent=2, ensure_ascii=False))
