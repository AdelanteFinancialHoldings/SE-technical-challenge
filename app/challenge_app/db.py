import psycopg2
import psycopg2.extras
import click
from flask import current_app, g
from flask.cli import with_appcontext
import random, uuid, time, json, sys,string

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



@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

#Random data generation:

def get_random_words(words_list, total=1):
    ran_words = []
    # enumerate over specified number of words
    while len(ran_words) < total:
        ran_words += [words_list[random.randint(0, len(words_list)-1)]]

    # return a string by joining the list of words
    return ' '.join(ran_words)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

def create_postgres_json(size):
    # list to store JSON records
    records = []
    # random words to inject into records
    words = ["finanzas", 'tecnologia', "ropa",
    "apparel", "movilidad", 'belleza', 'hogar', 'deportes', 'educacion']
    # iterate over the number of records being created
    for rec_id in range(size):

        # create a new record dict
        new_record = {}

        # input a value for each table column
        data_dict = {}
        data_dict['name'] = get_random_string(8)
        data_dict['brand'] = get_random_string(12)
        data_dict['minAmount'] = random.randint(0, 30)
        data_dict['maxAmount'] = random.randint(50, 100)
        data_dict['discount'] = random.uniform(1.5, 99.9)
        data_dict['tags'] = {get_random_words( words, 3)}
        data_dict['credentials'] = None
        
        new_record[ 'id' ] = uuid.uuid4().hex
        new_record[ 'data' ] = data_dict

        # append the new record dict to the list
        records += [ new_record ]

    # return the list of JSON records
    return records


def create_mock_data():
    json_records = create_postgres_json(100)
    json_records_str = json.dump(json_records, indent=4)
    return 0

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
