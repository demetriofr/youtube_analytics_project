import os

from googleapiclient.discovery import build


class Youtube:
    """Класс для загрузки информации с Youtube"""

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
