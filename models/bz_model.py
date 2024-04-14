import pandas

def get_types(conn):
    return pandas.read_sql(f'''select * from type''', conn)
def get_features(conn):
    return pandas.read_sql(f'''select * from feature''', conn)

def get_features_sc(conn):
    return pandas.read_sql(f'''select * from feature where type=0''', conn)
def get_features_num(conn):
    return pandas.read_sql(f'''select * from feature where type=1''', conn)

def get_possible_value_sc(id, conn):
    return pandas.read_sql(f'''select * from possible_value where feature_id={id}''', conn)
def get(id, conn):
    return pandas.read_sql(f'''select value from possible_value where possible_value_id={id}''', conn)
def get_possible_value_num(id, conn):
    return pandas.read_sql(f'''select * from num_possible_value where feature_id={id}''', conn)

def get_type_features(id, conn):
    return pandas.read_sql(f'''select features_list_id, feature_name, feature_id 
    from feature natural join features_list natural join type where type_id={id};
    ''', conn)
def get_type_values(type_id, feature_id, conn):
    return pandas.read_sql(f'''select value_id, value, type, features_list_id, feature_id
    from value natural join features_list natural join feature natural join type
    where type_id='{type_id}' and feature_id='{feature_id}';
    ''', conn)


def add_type(name, conn):
    cur = conn.cursor()
    sql = f"insert into type (type_name) values ('{name}');"
    cur.execute(sql)
    conn.commit()
def del_type(id, conn):
    cur = conn.cursor()
    sql = f"delete from type where type_id='{id}';"
    cur.execute(sql)
    conn.commit()

def add_feature(name, type, conn):
    cur = conn.cursor()
    sql = f"insert into feature (feature_name, type) values ('{name}', {type});"
    cur.execute(sql)
    conn.commit()
def del_feature(id, conn):
    cur = conn.cursor()
    sql = f"delete from feature where feature_id='{id}';"
    cur.execute(sql)
    conn.commit()

def add_possible_value(id, value, conn):
    cur = conn.cursor()
    sql = f"insert into possible_value (value, feature_id) values ('{value}', {id});"
    cur.execute(sql)
    conn.commit()
def del_possible_value(id, conn):
    cur = conn.cursor()
    sql = f"delete from possible_value where possible_value_id={id};"
    cur.execute(sql)
    conn.commit()

def add_possible_value_num(id, value, conn):
    cur = conn.cursor()
    sql = f"insert into num_possible_value (value, feature_id) values ('{value}', {id});"
    cur.execute(sql)
    conn.commit()
def del_possible_value_num(id, conn):
    cur = conn.cursor()
    cur.execute(f"delete from num_possible_value where feature_id={id};")
    conn.commit()

def add_features_list(type_id, feature_id, conn):
    cur = conn.cursor()
    sql = f"insert into features_list (type_id, feature_id) values ({type_id}, {feature_id});"
    cur.execute(sql)
    conn.commit()
def del_features_list(id, conn):
    cur = conn.cursor()
    sql = f"delete from features_list where features_list_id={id};"
    cur.execute(sql)
    conn.commit()

def add_value(value, type_id, feature_id, conn):
    cur = conn.cursor()
    buf = f'(select features_list_id from features_list where type_id={type_id} and feature_id={feature_id})'
    sql = f"insert into value (value, features_list_id) values ('{value}', {buf});"
    cur.execute(sql)
    conn.commit()
def del_value(id, conn):
    cur = conn.cursor()
    sql = f"delete from value where value_id='{id}';"
    cur.execute(sql)
    conn.commit()

    
def get_empty_types(conn):
    return pandas.read_sql(
        '''SELECT type_name FROM type
            WHERE type_id NOT IN (SELECT type_id FROM features_list)''',
        conn)

def get_empty_features(conn):
    return pandas.read_sql(
        '''SELECT feature_name FROM feature 
        WHERE feature_id NOT IN (SELECT feature_id FROM possible_value)
        AND feature_id NOT IN (SELECT feature_id FROM num_possible_value )''',
        conn)

def get_empty_all(conn):
    return pandas.read_sql(
        '''SELECT type_name, feature_name 
            FROM features_list natural join feature natural join type
            WHERE features_list_id NOT IN (SELECT features_list_id FROM value)''',
        conn)
