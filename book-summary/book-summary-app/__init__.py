from flask import Flask
# from flask import url_for
# from flask import request
# from flask import redirect
# from flask import session
# from flask import render_template
# from markupsafe import escape

import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'book-summary-app.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

     # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # To Do: Why is this code placed here?
    #   If this is placed at the top, outside of this function
    #   will it still work thesame?
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app