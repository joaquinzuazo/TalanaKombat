import pytest
from ..helpers.helpers import start_play
from talana.entities.player import Player

@pytest.fixture
def payload():
    player1 = Player(
            'Test',
            {},
            6,
            ["DSD", "S", "S"],
            ["P", "", "P", "K", "K", "K"]
        )

    player2 = Player(
        'Test2',
        {},
        6,
        ["DSD", "S"],
        ["P", "", "P", "K", "K", "K"]
        )
    return player1, player2

def test_start_play(payload):
    result = start_play(payload[0],payload[1])
    # Returns the order of the players, in this case, player two starts, for having fewer moves
    assert result == (payload[1],payload[0])
