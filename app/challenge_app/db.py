import psycopg2
import psycopg2.extras
from flask import g

def get_db():
    if 'db' not in g:
        connection = psycopg2.connect(
            host="flask_db",
            database="postgres",
            user="postgres",
            password="postgres")
        g.db = connection
    return g.db
    

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)