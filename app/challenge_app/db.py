import psycopg2
import psycopg2.extras
import click
from flask import current_app, g
from flask.cli import with_appcontext

from . import data_gen

def get_db():
    if 'db' not in g:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="1234")
        g.db = connection
    return g.db
    

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('generateData.sql') as f:
        with db:
            with db.cursor() as curs:
                curs.execute(f.read())

    
def create_mock_data():
    db = get_db()
    json_records = data_gen.create_postgres_json(100)
    sql_str = data_gen.create_insert_records(json_records,'public.stores')
    with db:
        with db.cursor() as curs:
            curs.execute(sql_str)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    create_mock_data()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
