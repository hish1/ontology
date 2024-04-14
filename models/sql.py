import sqlite3
import pandas
conn = sqlite3.connect("dinos.sqlite", check_same_thread=False)
cursor = conn.cursor()

# def get_features(name):
#     arr = []
#     arr.append(pandas.read_sql(f'''
#         select feature_name, value, type
#         from class natural join features
#         where class_name='{name}' and type=='num'
#     ''', conn))
#     arr.append(pandas.read_sql(f'''
#         select feature_name, value, type
#         from class natural join features
#         where class_name='{name}' and type=='scalar'
#     ''', conn))
#     # arr.append(pandas.read_sql(f'''
#     #     select feature_name, value, type
#     #     from class natural join features
#     #     where class_name='{name}' and type=='one'
#     # ''', conn))
#     return arr

def get_types():
    return pandas.read_sql(f'''select type_name from type''', conn)
def get_features():
    return pandas.read_sql(f'''select feature_name, type from feature''', conn)
def get_possible_value(feature_name):
    return pandas.read_sql(f'''select value
    from possible_value natural join feature
    where feature_name='{feature_name}'
    ''', conn)

def get_type_value(type_name, feature_name):
    return pandas.read_sql(f'''select value
    from value natural join features_list natural join feature natural join type
    where type_name='{type_name}' and feature_name='{feature_name}'
    ''', conn)


def add_type(name):
    sql = f"insert into type (type_name) values ('{name}');"
    cursor.execute(sql)
def del_type(name):
    sql = f"delete from type where type_name='{name}';"
    cursor.execute(sql)

def add_feature(name, type):
    sql = f"insert into feature (feature_name, type) values ('{name}', {type});"
    cursor.execute(sql)
def del_feature(name):
    sql = f"delete from feature where feature_name='{name}';"
    cursor.execute(sql)

def add_possible_value(feature, value):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    sql = f"insert into possible_value (value, feature_id) values ('{value}', {feature_id});"
    cursor.execute(sql)
def del_possible_value(feature, value):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    sql = f"delete from possible_value where value='{value}' and feature_id={feature_id};"
    cursor.execute(sql)

def add_features_list(type, feature):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    type_id = f"select type_id from type where type_name='{type}'"
    sql = f"insert into features_list (type_id, feature_id) values ({type_id}, {feature_id});"
    cursor.execute(sql)
def del_features_list(type, feature):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    type_id = f"select type_id from type where type_name='{type}'"
    sql = f"delete from features_list where type_id={type_id} and feature_id={feature_id};"
    cursor.execute(sql)

def add_value(type, feature, value):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    type_id = f"select type_id from type where type_name='{type}'"
    list_id = f"select features_list_id from features_list where feature_id={feature_id} and type_id={type_id}"
    sql = f"insert into value (value, features_list_id) values ('{value}', {list_id});"
    cursor.execute(sql)
def del_value(type, feature, value):
    feature_id = f"select feature_id from feature where feature_name='{feature}'"
    type_id = f"select type_id from type where type_name='{type}'"
    list_id = f"select features_list_id from features_list where feature_id={feature_id} and type_id={type_id}"
    sql = f"delete from value where value='{value}' and features_list_id={list_id};"
    cursor.execute(sql)