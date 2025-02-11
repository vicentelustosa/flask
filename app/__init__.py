from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Inicialização das extensões
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='views')
    app.config.from_object(Config)

    # Inicializar extensões com a aplicação
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Configuração do Flask-Login
    login_manager.login_view = 'auth.login'

    # Importação dos Blueprints
    from app.controllers.auth import auth_bp
    from app.controllers.post import post_bp

    # Registro dos Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(post_bp, url_prefix='/')

    return app

# Importação do modelo de usuário e definição da função user_loader
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
