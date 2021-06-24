import random, uuid, json, string


def get_random_words(words_list, total=1):
    ran_words = []
    while len(ran_words) < total:
        ran_words += [words_list[random.randint(0, len(words_list)-1)]]
    return ran_words

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def create_postgres_json(size):
    records = []
    words = ["finanzas", 'tecnologia', "ropa",
    "apparel", "movilidad", "belleza", "hogar", "deportes", "educacion"]

    for rec_id in range(size):
        new_record = {}
        data_dict = {}
        
        data_dict['name'] = get_random_string(8)
        data_dict['brand'] = get_random_string(12)
        data_dict['minAmount'] = random.randint(0, 30)
        data_dict['maxAmount'] = random.randint(50, 100)
        data_dict['discount'] = random.uniform(1.5, 99.9)
        data_dict['tags'] = get_random_words(words, 3)
        data_dict['credentials'] = None
        
        new_record[ 'id' ] = uuid.uuid4().hex
        new_record[ 'data' ] = data_dict

        records += [ new_record ]

    return records

def create_insert_records( json_array, table_name ):

    columns = json_array[0].keys()

    columns = [str(col).lower().replace(" ", "_") for col in columns]
    columns = [str(col).lower().replace("-", "_") for col in columns]

    # concatenate a string for the SQL 'INSERT INTO' statement
    sql_string = "INSERT INTO {}".format(table_name)
    sql_string = sql_string + " (" + ', '.join(columns) + ")\nVALUES "

    record_list = []
    for i, record in enumerate( json_array ):
        values = record.values()
        record = list(values)

        for i, val in enumerate(record):
            if type(val) == str:
                if "'" in val:
                    record[i] = "'" + record[i].replace("'", "''") + "'"
            if type(val) == dict:
                record[i] = json.dumps(record[i])

        record = str(record)[1:len(str(record))-1]
        record = record.replace("''", '"')

        record_list += [ record ]
    for i, record in enumerate(record_list):
        sql_string = sql_string + "(" + record + "),\n"

    sql_string = sql_string[:-2] + ";"

    return sql_string

