from src.playlist import PlayList


def test_playlist():
    """
    Проверяет добавление атрибутов плейлиста
    """
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"

    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
