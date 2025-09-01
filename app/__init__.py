# app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(
        __name__,
        static_folder="static",       
        template_folder="templates"  
    )

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "gizli_anahtar")

    
    from .routes.home_routes import home_bp
    from .routes.auth_routes import auth_bp
    from .routes.brand_routes import brand_bp
    from .routes.influencer_routes import influencer_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(brand_bp, url_prefix="/brand")
    app.register_blueprint(influencer_bp, url_prefix="/influencer")


    @app.get("/healthz")
    def healthz():
        return "ok", 200

    return app
