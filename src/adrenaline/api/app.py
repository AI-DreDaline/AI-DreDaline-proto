from flask import Flask
from adrenaline.api.routers.health import bp as health_bp
from adrenaline.api.routers.route_generate import bp as gen_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(gen_bp,    url_prefix="/api")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
