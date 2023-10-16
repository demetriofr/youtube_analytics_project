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

    def __init__(self, channel_id_: str) -> None:
        """
        Экземпляр инициализируется id канала и добавляет данные по API
        """
        self.channel = self.get_info_about_channel(channel_id_)
        self.__channel_id = self.channel_id
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.channel['items'][0]['snippet']['customUrl']
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self):
        return self.channel['items'][0]['id']

    def get_info_about_channel(self, channel_id):
        """
        Получает информацию о канале
        """
        channel = self.YOUTUBE.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит информацию о канале в словарь в JSON формате с отступами"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.YOUTUBE
