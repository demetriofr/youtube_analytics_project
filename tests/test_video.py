from src.video import Video, PLVideo


def test_video():
    """
    Проверяет добавление атрибутов видео
    """
    video1 = Video('AWX4JnAnjBE')
    assert video1.video_id == 'AWX4JnAnjBE'
    assert video1.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video1.url == 'https://www.youtube.com/watch?v=AWX4JnAnjBE'
    assert video1.view_count >= 55_369
    assert video1.like_count >= 2_349
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_plvideo():
    """
    Проверяет добавление атрибутов плейлиста
    """
    video1 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert video1.video_id == '4fObz_qw9u4'
    assert video1.pl_video_id == 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
    assert video1.title == 'MoscowPython Meetup 78 - вступление'
    assert video1.url == 'https://www.youtube.com/watch?v=4fObz_qw9u4'
    assert video1.view_count >= 694
    assert video1.like_count >= 10
    assert str(video1) == 'MoscowPython Meetup 78 - вступление'


def test_broken_video_id():
    broken_video_id = '123_4fObz_q'
    broken_video = Video(broken_video_id)
    assert broken_video.video_id == '123_4fObz_q'
    assert broken_video.title is None
    assert broken_video.url is None
    assert broken_video.view_count is None
    assert broken_video.like_count is None
