from app import app
from flask import render_template, request, session

from utils import get_db_connection
from models.bz_model import *

global value_checked
global checked
checked, value_checked = [], []

@app.route('/solver/', methods=['get', 'post'])
def solver():
    global checked
    global value_checked
    conn = get_db_connection()
    data_features = get_features(conn)
    data_checked = checked
    data_features_sc = get_features_sc(conn)
    data_features_num = get_features_num(conn)
    data_possible_sc = []
    data_possible_num = []
    data_value_checked = value_checked
    data_all = []
    result = ''


    if request.values.getlist('get_checkbox'):
        checked = request.values.getlist('get_checkbox')
        data_checked = checked


    if request.values.get('feature_selector'):
        feature_id = int(request.values.get('features_selector'))
        data_possible_sc = get_possible_value_sc(feature_id, conn)
        session['feature_id'] = feature_id
        

    if request.values.get('value_checker'):
        feature_id = int(session.get('feature_id'))
        value_checked = request.values.get('value_checker')
        data_value_checked = value_checked
        

    if request.values.get('get_result'):
        a=1



    html = render_template(
        'solver.html',
        data_features = data_features,
        data_checked = data_checked,
        data_features_sc = data_features_sc,
        data_features_num = data_features_num,
        data_possible_sc = data_possible_sc,
        data_possible_num = data_possible_num,
        data_all = data_all,
        result = result,
        feature_id = session['feature_id'],
        len = len
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)