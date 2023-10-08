from src.channel import Channel


def test_channel_id():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_print_info():
    pass
