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

    @staticmethod
    def youtube(api_key):
        """
        Создаёт специальный объект для работы с API
        """
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    __API_KEY = __api_key()
    YOUTUBE = youtube(__API_KEY)



    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала и добавляет данные по API
        """
        self.channel_id = channel_id
        self.channel = self.get_info_about_channel(channel_id)

    def get_info_about_channel(self, channel_id):
        """
        Получает информацию о канале
        """
        channel = self.YOUTUBE.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит информацию о канале в словарь в JSON формате с отступами"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
