import pytest

from src.channel import Channel


def test_channel_id():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_print_info():
    pass


def test_channel_attribute():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert moscowpython.title == 'MoscowPython'
    assert moscowpython.description == '''Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)
Присоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'''
    assert moscowpython.url == 'https://www.youtube.com/@moscowdjangoru'
    assert moscowpython.subscriber_count >= 26600
    assert moscowpython.video_count >= 709
    assert moscowpython.view_count >= 2432150


@pytest.mark.xfail(raises=AttributeError)
def test_channel_attribute__channel_id():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.channel_id = 'Новое название'


def test_channel__get_service():
    assert str(Channel.get_service())[1:45] == 'googleapiclient.discovery.Resource object at'


def test_get_service():
    pass


def test_channel__to_json():
    pass


def test_channel_dunder_method():
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Проверяем магические методы (сложение / вычитание / сравнение)
    assert str(moscowpython) == 'MoscowPython (https://www.youtube.com/@moscowdjangoru)'
    assert moscowpython + highload >= 100100
    assert moscowpython - highload <= -48300
    assert highload - moscowpython >= 48300
    assert bool(moscowpython > highload) == False
    assert bool(moscowpython >= highload) == False
    assert bool(moscowpython < highload) == True
    assert bool(moscowpython <= highload) == True
    assert bool(moscowpython == highload) == False
