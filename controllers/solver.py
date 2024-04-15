from math import isnan
from app import app
from flask import render_template, request, session

from utils import get_db_connection
from models.solver_model import *

chosen_data = {}

@app.route('/solver/', methods=['get', 'post'])
def solver():
    global chosen_data
    conn = get_db_connection()
    data_features = get_features(conn)
    data_features_sc = []
    data_features_num = []
    data_possible_sc = []
    data_possible_num = []
    flag = False
    result_good = []
    result_bad = []


    if request.values.get('feature_selector'):
        feature_id = int(request.values.get('feature_selector'))
        session['feature_id'] = feature_id
        session['checked_id'] = -1

        sc = get_features_sc_id(feature_id, conn)
        num = get_features_num_id(feature_id, conn)
        
        data_possible_sc = get_possible_value_sc(feature_id, conn)
        data_possible_num = get_possible_value_num(feature_id, conn)


    elif request.values.get('value_choose'):
        feature_id = int(session.get('feature_id'))
        data_possible_num = get_possible_value_num(feature_id, conn)
        data_possible_sc = get_possible_value_sc(feature_id, conn)

        sc = get_features_sc_id(feature_id, conn)
        num = get_features_num_id(feature_id, conn)
        if not sc.empty:
            option = int(request.values.get('value_choose'))
            for i in data_possible_sc.values:
                if i[0]==option:
                    chosen_data[feature_id] = i[1]
            # chosen_data[feature_id] = option
            session['checked_id'] = option
        # elif not num.empty:
        #     option = request.fvalues.ge('value_choose')
        #     chosen_data[feature_id] = int(option)
        #     session['checked_id'] = int(request.values.get('label'))



    elif request.values.get('types_num_value'):
        feature_id = int(session.get('feature_id'))
        checked_id = int(session.get('checked_id'))

        sc = get_features_sc_id(feature_id, conn)
        num = get_features_num_id(feature_id, conn)
        # if not sc.empty:
        #     option = int(request.values.get('types_num_value'))
        #     for i in data_possible_sc.values:
        #         if i[0]==option:
        #             chosen_data[feature_id] = i[1]
        #     # chosen_data[feature_id] = option
        #     session['checked_id'] = option
        if not num.empty:
            option = int(request.values.get('types_num_value'))
            chosen_data[feature_id] = option
            session['checked_id'] = option

        data_possible_sc = get_possible_value_sc(feature_id, conn)
        data_possible_num = get_possible_value_num(feature_id, conn)


    elif request.values.get('get_result'):
        flag = True

        types = get_types(conn)
        types = types.values
        res_bad = []
        res_good = []

        for type in types:
            res = []
            for v in chosen_data:
                t = type[0]
                n = chosen_data[v]
                val = get_features_id(v, conn).values[0]
                if val[2] == 1:
                    num = get_type_values_num(t, v, conn).values
                    if n not in range(int(num[0][1]), int(num[1][1])):
                        res.append(f''' - значение признака «{val[1]}» не подходит\n''')
                elif get_type_values(t, v, n, conn).empty:
                    res.append(f''' - значение признака «{val[1]}» не подходит\n''')

            if res != []:
                res_bad.append(f'''\nКласс «{type[1]}» не подходит так как:\n''')
                res_bad += res
            else:
                res_good.append(f'«{type[1]}»\n')
            
        if res_good == []:
            result_good.append('Нет классов\n')
        elif chosen_data == {}:
            result_good.append('Не выбрано ни одного признака.\n')
        else:
            result_good = res_good
            result_bad = res_bad


    elif not data_features.empty:
        session['feature_id'] = int(data_features.loc[0, 'feature_id'])
        feature_id = session['feature_id']
        session['checked_id'] = -1

        sc = get_features_sc_id(feature_id, conn)
        num = get_features_num_id(feature_id, conn)
        
        data_possible_sc = get_possible_value_sc(feature_id, conn)
        data_possible_num = get_possible_value_num(feature_id, conn)

        



    html = render_template(
        'solver.html',
        data_features = data_features,
        data_features_sc = data_features_sc,
        data_features_num = data_features_num,
        data_possible_sc = data_possible_sc,
        data_possible_num = data_possible_num,
        result_good = result_good,
        result_bad = result_bad,
        flag = flag,
        feature_id = session['feature_id'],
        checked_id = session['checked_id'],
        len = len,
        min = min,
        max = max
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)