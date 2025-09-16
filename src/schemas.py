import uuid

from pydantic import BaseModel, Field

class CreatePlayerRequest(BaseModel):
    nickname: str

class CreatePlayerResponse(BaseModel):
    nickname: str
    user_id: uuid

class CreateRoomRequest(BaseModel):
    host_user_id: str
    max_players: int = Field(ge=3, le=8)

class CreateRoomResponse(BaseModel):
    room_id: str
    host_user_id: str
    max_players: int

