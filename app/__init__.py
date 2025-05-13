from flask import Flask
from app.routes.home_routes import home_bp
from app.routes.auth_routes import auth_bp
from app.routes.brand_routes import brand_bp
from app.routes.influencer_routes import influencer_bp
from flask import Flask
from flask import session

app = Flask(__name__)
app.secret_key = "gizli_anahtar"  # oturum verilerini şifrelemek için

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gizli_anahtar'
    
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(brand_bp, url_prefix="/brand")
    app.register_blueprint(influencer_bp, url_prefix="/influencer")

    return app
