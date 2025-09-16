from src.schemas import CreatePlayerResponse


def handle_get_user(player_id) -> CreatePlayerResponse:
    # TODO: logic here
    a = ""
    return CreatePlayerResponse(nickname=a, player_id=player_id)
