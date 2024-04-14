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
def get_possible_value_num(id, conn):
    return pandas.read_sql(f'''select * from num_possible_value where feature_id={id}''', conn)
