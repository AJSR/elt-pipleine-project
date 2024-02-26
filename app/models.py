from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DATE, TIME, ForeignKeyConstraint, PrimaryKeyConstraint, TIMESTAMP

class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, nullable=False)
    season = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    game_date = Column(DATE, nullable=False)
    game_time_eastern = Column(TIME(timezone=False), nullable=False)
    home_team_abbr = Column(String, nullable=False)
    visitor_team_abbr = Column(String, nullable=False)
    home_final_score = Column(Integer, nullable=False)
    visitor_final_score = Column(Integer, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Player(Base):
    __tablename__ = "players"

    nfl_id = Column(Integer, primary_key=True, nullable=False)
    height = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    birth_date = Column(DATE, nullable=True)
    college_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    display_name = Column(String, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Play(Base):
    __tablename__ = "plays"

    game_id = Column(Integer, nullable=False)
    play_id = Column(Integer, nullable=False)
    ball_carrier_id = Column(Integer, nullable=False)
    ball_carrier_name = Column(String, nullable=False)
    play_description = Column(String(500), nullable=True)
    quarter = Column(Integer, nullable=True)
    down = Column(Integer, nullable=True)
    yards_to_go = Column(Integer, nullable=True)
    possesion_team = Column(String, nullable=True)
    defensive_team = Column(String, nullable=True)
    yard_line_side = Column(String, nullable=True)
    yard_line_number = Column(Integer, nullable=True)
    game_clock = Column(String, nullable=True)
    pre_snap_home_score = Column(Integer, nullable=True)
    pre_snap_visitor_score = Column(Integer, nullable=True)
    pass_result = Column(String, nullable=True)
    pass_length = Column(Float, nullable=True)
    penalty_yards = Column(Float, nullable=True)
    pre_penalty_play_result = Column(Integer, nullable=True)
    play_result = Column(Integer, nullable=True)
    play_nullified_by_penalty = Column(String, nullable=True)
    absolute_yardline_number = Column(Integer, nullable=True)
    offense_formation = Column(String, nullable=True)
    defenders_in_the_box = Column(Float, nullable=True)
    pass_probability = Column(Float, nullable=True)
    pre_snap_home_team_win_probability = Column(Float, nullable=True)
    pre_snap_visitor_team_win_probability = Column(Float, nullable=True)
    home_team_win_probability_added = Column(Float, nullable=True)
    visitor_team_probability_added = Column(Float, nullable=True)
    expected_points = Column(Float, nullable=True)
    expected_points_added = Column(Float, nullable=True)
    foul_name_1 = Column(String, nullable=True)
    foul_name_2 = Column(String, nullable=True)
    foul_nfl_id_1 = Column(Integer, nullable=True)
    foul_nfl_id_2 = Column(Integer, nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))    

    __table_args__ = (ForeignKeyConstraint(["game_id"], ["games.game_id"]),
                      ForeignKeyConstraint(["ball_carrier_id"], ["players.nfl_id"]),
                      PrimaryKeyConstraint("play_id", "game_id", 
                                           name="plays_pk"))

class Tackle(Base):
    __tablename__ = "tackles"

    game_id = Column(Integer, nullable=False)
    play_id = Column(Integer, nullable=False)
    nfl_id = Column(Integer, nullable=False)
    tackle = Column(Boolean, nullable=True)
    assist = Column(Boolean, nullable=True)
    forced_fumble = Column(Boolean, nullable=True)
    pff_missed_tackle = Column(Boolean, nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    __table_args__ = (ForeignKeyConstraint(["play_id", "game_id"], ["plays.play_id", "plays.game_id"]),
                      ForeignKeyConstraint(["nfl_id"], ["players.nfl_id"]),
                      PrimaryKeyConstraint("play_id", "game_id", "nfl_id", 
                                           name="tackles_pk"))

class Tracking(Base):
    __tablename__ = "trackings"

    game_id = Column(Integer, nullable=False)
    play_id = Column(Integer, nullable=False)
    nfl_id = Column(Integer, nullable=False)
    display_name = Column(String, nullable=True)
    frame_id = Column(Integer, nullable=False)
    time = Column(String, nullable=True)
    jersey_number = Column(Integer, nullable=True)
    club = Column(String, nullable=True)
    play_direction = Column(String, nullable=True)
    x = Column(Float, nullable=True)
    y = Column(Float, nullable=True)
    s = Column(Float, nullable=True)
    a = Column(Float, nullable=True)
    dis = Column(Float, nullable=True)
    o = Column(Float, nullable=True)
    dir = Column(Float, nullable=True)
    event = Column(String, nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    __table_args__ = (ForeignKeyConstraint(["play_id", "game_id"], ["plays.play_id", "plays.game_id"]),
                      PrimaryKeyConstraint("play_id", "game_id", "frame_id", "nfl_id",
                                           name="trackings_pk"))
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    scope = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
