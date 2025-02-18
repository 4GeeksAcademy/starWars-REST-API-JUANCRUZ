from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user.model_user import User;
from .user.model_character import Character
from .user.model_planet import Planet
from .user.model_favorites import Favorites;