from typing import List
from pydantic import BaseModel, validator
from pydantic.error_wrappers import ErrorWrapper

class Song(BaseModel):
    """
    Represents a song.
    
    Attributes:
    ----------
    id : int
        Unique identifier for the song.
    title : str
        Title of the song.
    artist : str
        Artist who performed the song.
    genre : str
        Genre of the song.
    """
    id: int
    title: str
    artist: str
    genre: str

    @validator('title')
    def title_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Title must not be empty')
        return v

    @validator('artist')
    def artist_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Artist must not be empty')
        return v

    @validator('genre')
    def genre_must_be_valid(cls, v):
        valid_genres = ['pop', 'rock', 'hip-hop', 'electronic', 'classical']
        if v.lower() not in valid_genres:
            raise ValueError(f'Invalid genre. Must be one of {valid_genres}')
        return v


class User(BaseModel):
    """
    Represents a user.
    
    Attributes:
    ----------
    id : int
        Unique identifier for the user.
    username : str
        Username chosen by the user.
    password : str
        Password for the user's account.
    """
    id: int
    username: str
    password: str

    @validator('username')
    def username_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Username must not be empty')
        return v

    @validator('password')
    def password_must_meet_requirements(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v


class Playlist(BaseModel):
    """
    Represents a playlist.
    
    Attributes:
    ----------
    id : int
        Unique identifier for the playlist.
    name : str
        Name of the playlist.
    songs : List[Song]
        Songs in the playlist.
    """
    id: int
    name: str
    songs: List[Song]

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Name must not be empty')
        return v


class Recommendation(BaseModel):
    """
    Represents a song recommendation.
    
    Attributes:
    ----------
    song : Song
        Recommended song.
    reason : str
        Reason for the recommendation.
    """
    song: Song
    reason: str

    @validator('reason')
    def reason_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('Reason must not be empty')
        return v