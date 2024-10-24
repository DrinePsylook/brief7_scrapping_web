import os

from flask import Flask

def create_app(test_config=None):
    #créer et configure l'appli
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # charge l'instance config s'il existe, quand il n'est pas testé
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Charge le teste de config 
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World ! I\'m trying Flask'
    
    def create_app():
        app=...

        from.import db
        db.init_app(app)
    
    return app