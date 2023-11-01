import datetime
from json import dumps

import isodate

from src.youtube import Youtube


class PlayList(Youtube):
    def __init__(self, playlist_id: str):
        """
        Экземпляр инициализируется через id плeйлиста и добавляет данные по API
        """
        self.playlist: dict = self.get_info_about_playlist(playlist_id)
        self.playlist_id: str = playlist_id
        self.title: str = self.playlist['items'][0]['snippet']['title']
        self.url: str = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def get_info_about_playlist(self, playlist_id: str) -> dict:
        """
        Получает информацию о плейлисте
        """
        playlists: dict = super().YOUTUBE.playlists().list(id=playlist_id,
                                                           part='snippet',
                                                           maxResults=50,
                                                           ).execute()
        return playlists

    def print_info(self) -> None:
        """
        Выводит информацию о плейлисте в словарь в JSON формате с отступами
        """
        print(dumps(self.playlist,
                    indent=2,
                    ensure_ascii=False)
              )

    def get_videos_part(self, part: str) -> dict:
        """
        Получить заданный параметр у видео в плейлисте
        """
        # Получить данные по видеороликам в плейлисте
        playlist_videos: dict = super().YOUTUBE.playlistItems().list(playlistId=self.playlist_id,
                                                                     part='contentDetails',
                                                                     maxResults=50,
                                                                     ).execute()

        # Получить все id видеороликов из плейлиста
        video_ids: str = ','.join([video['contentDetails']['videoId'] for video in playlist_videos['items']])

        # Вывести словарь с нужным параметром видеороликов из плейлиста
        video_response: dict = super().YOUTUBE.videos().list(part=part,
                                                             id=video_ids
                                                             ).execute()
        return video_response

    @property
    def total_duration(self):
        """
        Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
        """
        # Часть содержащая длительность
        part: str = 'contentDetails'

        # Начальное значение длительности
        total_time_video = datetime.timedelta(
            hours=0,
            minutes=0,
            seconds=0
        )

        # Вывести длительности видеороликов из плейлиста
        for video in self.get_videos_part(part)['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video[part]['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time_video += duration

        return total_time_video

    def show_best_video(self) -> str:
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        """
        # Часть содержащая количество лайков
        part: str = 'statistics'

        like_max: int = 0
        video_id: str = ''
        # Сравнивает количество лайков у видео в плейлисте
        for video in self.get_videos_part(part)['items']:
            like = int(video[part]['likeCount'])
            if like > like_max:
                like_max = like
                video_id = video['id']

        # Выводит ссылку на видео в плейлисте с большим количеством лайков
        return f'https://youtu.be/{video_id}'
