from pydantic import BaseModel, Field


class CreatePlayerRequest(BaseModel):
    """Take in a nickname to create a player"""

    nickname: str


class CreatePlayerResponse(BaseModel):
    """Given a nickname return a nickname and player id"""

    nickname: str
    player_id: str


class CreateRoomRequest(BaseModel):
    """Requires a player id from the host and number of players"""

    host_player_id: str
    num_players: int = Field(ge=3, le=8)


class CreateRoomResponse(BaseModel):
    """Given a host's player id and number of players return a room id"""

    room_id: str
    host_player_id: str
    num_players: int = Field(ge=3, le=8)
