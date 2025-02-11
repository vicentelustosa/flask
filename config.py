import os

class Config:
    SECRET_KEY = 'minha_chave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mural.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/profile_pics')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Limite de 2MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
