from json import dumps

from src.youtube import Youtube
from src.exceptions_yt import BrokenVideoId


class Video(Youtube):
    def __init__(self, video_id: str):
        """
        Экземпляр инициализируется id видео и добавляет данные по API.
        А также проводится корректность введённого id видео.
        """
        try:
            self.video: dict = self.get_info_about_video(video_id)
            if not self.video['items']:
                raise BrokenVideoId
            self.video_id: str = video_id
            self.title: str = self.video['items'][0]['snippet']['title']
            self.url = 'https://www.youtube.com/watch?v=' + self.video_id
            self.view_count: int = int(self.video['items'][0]['statistics']['viewCount'])
            self.like_count: int = int(self.video['items'][0]['statistics']['likeCount'])
        except BrokenVideoId:
            self.video_id: str = video_id
            self.title: None = None
            self.url: None = None
            self.view_count: None = None
            self.like_count: None = None

    def get_info_about_video(self, video_id: str) -> dict:
        """
        Получает информацию о видео
        """
        video_response = super().YOUTUBE.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                       id=video_id
                                                       ).execute()
        return video_response

    def print_info(self) -> None:
        """Выводит информацию о видео в словарь в JSON формате с отступами"""
        print(dumps(self.video, indent=2, ensure_ascii=False))

    def __str__(self) -> str:
        """
        Выводит информацию о название видео
        """
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, pl_video_id: str):
        """
        Экземпляр инициализируется id видео, id плейлиста и добавляет
        название и URL видео, кол-во просмотров и лайков по API использую класс Video
        """
        super().__init__(video_id)
        self.pl_video_id: str = pl_video_id
