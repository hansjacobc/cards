from src.schemas import CreateRoomRequest, CreateRoomResponse


def handle_create_room(request: CreateRoomRequest) -> CreateRoomResponse:
    # TODO: logic here
    type(request)
    a = ""
    b = ""
    c = 1
    return CreateRoomResponse(room_id=a, host_player_id=b, num_players=c)
