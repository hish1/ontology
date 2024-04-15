import pandas

def get_types(conn):
    return pandas.read_sql(f'''select * from type''', conn)
def get_features(conn):
    return pandas.read_sql(f'''select * from feature''', conn)

def get_features_sc(conn):
    return pandas.read_sql(f'''select * from feature where type=0''', conn)
def get_features_num(conn):
    return pandas.read_sql(f'''select * from feature where type=1''', conn)

def get_features_id(id, conn):
    return pandas.read_sql(f'''select * from feature 
                           where feature_id={id}''', conn)
def get_features_type(type, conn):
    return pandas.read_sql(f'''select * from feature 
                           where type={type}''', conn)
def get_features_sc_id(id, conn):
    return pandas.read_sql(f'''select * from feature where type=0 and feature_id={id}''', conn)
def get_features_num_id(id, conn):
    return pandas.read_sql(f'''select * from feature where type=1 and feature_id={id}''', conn)

def get_possible_value_sc(id, conn):
    return pandas.read_sql(f'''select * from possible_value where feature_id={id}''', conn)
def get_possible_value_num(id, conn):
    return pandas.read_sql(f'''select * from num_possible_value where feature_id={id}''', conn)

def get_type_values(type_id, feature_id, value_n, conn):
    return pandas.read_sql(f'''select feature_id, value_id
                           from type
                           natural join feature
                           natural join features_list
                           natural join value
                           where type_id={type_id} and feature_id={feature_id} and value='{value_n}'
                           ''', conn)
def get_type_values_num(type_id, feature_id, conn):
    return pandas.read_sql(f'''select value_id, value
                           from type
                           natural join feature
                           natural join features_list
                           natural join value
                           where type_id={type_id} and feature_id={feature_id}
                           ''', conn)