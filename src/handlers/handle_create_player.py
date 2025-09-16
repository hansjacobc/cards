import secrets

from src.schemas import CreatePlayerRequest, CreatePlayerResponse


def handle_create_player(request: CreatePlayerRequest):
    nickname = request.nickname
    player_id = secrets.token_hex(3)
    return CreatePlayerResponse(nickname=nickname, player_id=player_id)
