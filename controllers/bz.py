from app import app
from flask import render_template, request, session

from utils import get_db_connection
from models.bz_model import *


@app.route('/bz/', methods=['get', 'post'])
def bz():
    conn = get_db_connection()
    selected_button = 'types'
    data_types = get_types(conn)
    data_features = get_features(conn)
    data_features_sc = get_features_sc(conn)
    data_features_num = get_features_num(conn)
    data_possible_sc = []
    data_possible_num = []
    data_type_features = []
    data_type_values = []
    empty_types = []
    empty_features = []
    empty_all = []
    


    # ------------------------- 1й таб -------------------------
    if request.values.get('types'):
        selected_button = 'types'

    elif request.values.get('del_type'):
        selected_button = 'types'
        del_type(request.values.get('del_type'), conn)
        data_types = get_types(conn)

    elif request.values.get('add_type'):
        selected_button = 'types'
        add_type(request.values.get('add_type'), conn)
        data_types = get_types(conn)


    # ------------------------- 2й таб -------------------------
    elif request.values.get('features'):
        selected_button = 'features'
        
    elif request.values.get('del_feature'):
        selected_button = 'features'
        del_feature(request.values.get('del_feature'), conn)
        data_features = get_features(conn)

    elif request.values.get('add_feature'):
        selected_button = 'features'
        a = request.values.get('add_feature')
        b = request.values.get('feature_type')
        add_feature(a, b, conn)
        data_features = get_features(conn)


    # ------------------------- 3й таб -------------------------
    elif request.values.get('possible_values_sc'):
        selected_button = 'possible_values_sc'
        if not data_features_sc.empty:
            session['feature_sc_id'] = int(data_features_sc.loc[0, 'feature_id'])
            data_possible_sc = get_possible_value_sc(int(session.get('feature_sc_id')), conn)
        else:
            session['feature_sc_id'] = -1

    elif request.values.get('features_sc_selector'):
        selected_button = 'possible_values_sc'
        feature_sc_id = int(request.values.get('features_sc_selector'))
        data_possible_sc = get_possible_value_sc(feature_sc_id, conn)
        session['feature_sc_id'] = feature_sc_id

    elif request.values.get('add_possible_sc'):
        selected_button = 'possible_values_sc'
        feature_sc_id = int(session.get('feature_sc_id'))
        val = request.values.get('add_possible_sc')
        add_possible_value(feature_sc_id, val, conn)
        data_possible_sc = get_possible_value_sc(feature_sc_id, conn)

    elif request.values.get('del_possible_sc'):
        selected_button = 'possible_values_sc'
        feature_sc_id = int(session.get('feature_sc_id'))
        val = request.values.get('del_possible_sc')
        del_possible_value(val, conn)
        data_possible_sc = get_possible_value_sc(feature_sc_id, conn)
        

    # ------------------------- 4й таб -------------------------
    elif request.values.get('possible_values_num'):
        selected_button = 'possible_values_num'
        if not data_features_num.empty:
            session['feature_num_id'] = int(data_features_num.loc[0, 'feature_id'])
            data_possible_num = get_possible_value_num(int(session.get('feature_num_id')), conn)
        else:
            session['feature_num_id'] = -1

    elif request.values.get('features_num_selector'):
        selected_button = 'possible_values_num'
        feature_num_id = int(request.values.get('features_num_selector'))
        data_possible_num = get_possible_value_num(feature_num_id, conn)
        session['feature_num_id'] = feature_num_id

    elif request.values.get('add_possible_num'):
        selected_button = 'possible_values_num'
        feature_num_id = int(session.get('feature_num_id'))
        start = int(request.values.get('num_start'))
        end = int(request.values.get('num_end'))
        add_possible_value_num(feature_num_id, start, conn)
        add_possible_value_num(feature_num_id, end, conn)
        data_possible_num = get_possible_value_num(feature_num_id, conn)

    elif request.values.get('del_possible_num'):
        selected_button = 'possible_values_num'
        feature_num_id = int(session.get('feature_num_id'))
        del_possible_value_num(feature_num_id, conn)
        data_possible_num = get_possible_value_num(feature_num_id, conn)


    # ------------------------- 5й таб -------------------------
    elif request.values.get('types_features'):
        selected_button = 'types_features'
        if not data_types.empty:
            session['type_id'] = int(data_types.loc[0, 'type_id'])
            data_type_features = get_type_features(int(session.get('type_id')), conn)
        else:
            session['type_id'] = -1

    elif request.values.get('types_for_features_selector'):
        selected_button = 'types_features'
        type_id = int(request.values.get('types_for_features_selector'))
        data_type_features = get_type_features(type_id, conn)
        session['type_id'] = type_id
        
    elif request.values.get('types_features_add'):
        selected_button = 'types_features'
        type_id = int(session.get('type_id'))
        feature = int(request.values.get('types_features_add'))
        add_features_list(type_id, feature, conn)
        data_type_features = get_type_features(type_id, conn)
        
    elif request.values.get('types_features_del'):
        selected_button = 'types_features'
        type_id = int(session.get('type_id'))
        feature_list = int(request.values.get('types_features_del'))
        del_features_list(feature_list, conn)
        data_type_features = get_type_features(type_id, conn)


    # ------------------------- 6й таб -------------------------
    elif request.values.get('types_values'):
        selected_button = 'types_values'
        if not data_types.empty:
            session['type_id'] = int(data_types.loc[0, 'type_id'])
            data_type_features = get_type_features(int(session.get('type_id')), conn)

            if not data_type_features.empty:
                session['feature_id'] = int(data_type_features.loc[0, 'feature_id'])
                data_type_values = get_type_values(session['type_id'], session['feature_id'], conn)
                data_possible_sc = get_possible_value_sc(session['feature_id'], conn)
                data_possible_num = get_possible_value_num(session['feature_id'], conn)
            else: 
                session['feature_id'] = -1
        else:
            session['type_id'] = -1

    elif request.values.get('types_for_values_selector'):
        selected_button = 'types_values'
        type_id = int(request.values.get('types_for_values_selector'))
        data_type_features = get_type_features(type_id, conn)
        session['type_id'] = type_id

        if not data_type_features.empty:
            session['feature_id'] = int(data_type_features.loc[0, 'feature_id'])
            data_type_values = get_type_values(session['type_id'], session['feature_id'], conn)
            data_possible_sc = get_possible_value_sc(session['feature_id'], conn)
            data_possible_num = get_possible_value_num(session['feature_id'], conn)
        else: 
            session['feature_id'] = -1

    elif request.values.get('features_for_values_selector'):
        selected_button = 'types_values'
        type_id = int(session.get('type_id'))
        data_type_features = get_type_features(type_id, conn)

        feature_id = int(request.values.get('features_for_values_selector'))
        data_type_values = get_type_values(type_id, feature_id, conn)
        session['feature_id'] = feature_id

        data_possible_sc = get_possible_value_sc(session['feature_id'], conn)
        data_possible_num = get_possible_value_num(session['feature_id'], conn)

    elif request.values.get('types_values_add'):
        selected_button = 'types_values'
        type_id = int(session.get('type_id'))
        data_type_features = get_type_features(type_id, conn)
        
        feature_id = int(session.get('feature_id'))
        val = get(request.values.get('types_values_add'), conn).loc[0, 'value']
        add_value(val, type_id, feature_id, conn)
        data_type_values = get_type_values(type_id, feature_id, conn)
        
        data_possible_sc = get_possible_value_sc(session['feature_id'], conn)
        data_possible_num = get_possible_value_num(session['feature_id'], conn)
        
    elif request.values.get('types_values_del'):
        selected_button = 'types_values'
        type_id = int(session.get('type_id'))
        data_type_features = get_type_features(type_id, conn)

        feature_id = int(session.get('feature_id'))
        del_value(request.values.get('types_values_del'), conn)
        data_type_values = get_type_values(type_id, feature_id, conn)

        data_possible_sc = get_possible_value_sc(session['feature_id'], conn)
        data_possible_num = get_possible_value_num(session['feature_id'], conn)
        

    # ------------------------- 7й таб -------------------------
    elif request.values.get('check'):
        selected_button = 'check'
        empty_types = get_empty_types(conn)
        empty_features = get_empty_features(conn)
        empty_all = get_empty_all(conn)
    

    
    html = render_template(
        'bz.html',
        selected_button = selected_button,
        data_types = data_types,
        data_features = data_features,
        data_features_sc = data_features_sc,
        data_features_num = data_features_num,
        data_possible_sc = data_possible_sc,
        data_possible_num = data_possible_num,
        data_type_features = data_type_features,
        data_type_values = data_type_values,
        empty_types = empty_types,
        empty_features = empty_features,
        empty_all = empty_all,
        feature_sc_id = session['feature_sc_id'],
        feature_num_id = session['feature_num_id'],
        type_id = session['type_id'],
        feature_id = session['feature_id'],
        len = len,
        max = max,
        min = min
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)