from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, time, datetime

class PlayerOut(BaseModel):
    nfl_id: int
    display_name: str
    position: str
    height: str
    weight: int
    birth_date: Optional[date] = None
    college_name: str
    updated_at: datetime

    class Config:
        from_attributes = True

class GameOut(BaseModel):
    game_id: int
    season: int
    week: int
    game_date: date
    game_time_eastern: time
    home_team_abbr: str
    visitor_team_abbr: str
    home_final_score: int
    visitor_final_score: int
    updated_at: datetime

    class Config:
        from_attributes = True

class PlayOut(BaseModel):
    game_id: int
    play_id: int
    ball_carrier_id: int
    ball_carrier_name: str
    play_description: Optional[str] = None
    quarter: Optional[int] = None
    down: Optional[int] = None
    yards_to_go: Optional[int] = None
    possesion_team: Optional[str] = None
    defensive_team: Optional[str] = None
    yard_line_side: Optional[str] = None
    yard_line_number: Optional[int] = None
    game_clock: Optional[str] = None
    pre_snap_home_score: Optional[int] = None
    pre_snap_visitor_score: Optional[int] = None
    pass_result: Optional[str] = None
    pass_length: Optional[float] = None
    penalty_yards: Optional[float] = None
    pre_penalty_play_result: Optional[int] = None
    play_result: Optional[int] = None
    play_nullified_by_penalty: Optional[str] = None
    absolute_yardline_number: Optional[int] = None
    offense_formation: Optional[str] = None
    defenders_in_the_box: Optional[float] = None
    pass_probability: Optional[float] = None
    pre_snap_home_team_win_probability: Optional[float] = None
    pre_snap_visitor_team_win_probability: Optional[float] = None
    home_team_win_probability_added: Optional[float] = None
    visitor_team_probability_added: Optional[float] = None
    expected_points: Optional[float] = None
    expected_points_added: Optional[float] = None
    foul_name_1: Optional[str] = None
    foul_name_2: Optional[str] = None
    foul_nfl_id_1: Optional[int] = None
    foul_nfl_id_2: Optional[int] = None
    updated_at: datetime

    class Config:
        from_attributes = True  

class TackleOut(BaseModel):
    game_id: int
    play_id: int
    nfl_id: int
    tackle: Optional[bool] = None
    assist: Optional[bool] = None
    forced_fumble: Optional[bool] = None
    pff_missed_tackle: Optional[bool] = None
    updated_at: datetime

    class Config:
        from_attributes = True

class TrackingOut(BaseModel):
    game_id: int
    play_id: int
    nfl_id: int
    frame_id: int
    display_name: Optional[str]
    time: Optional[str]
    jersey_number: Optional[int]
    club: Optional[str]
    play_direction: Optional[str]
    x: Optional[float]
    y: Optional[float]
    s: Optional[float]
    a: Optional[float]
    dis: Optional[float]
    o: Optional[float]
    dir: Optional[float]
    event: Optional[str]
    updated_at: datetime

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    scope: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int = None
