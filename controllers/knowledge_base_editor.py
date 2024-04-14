from app import app
from flask import render_template, request, session

# from utils import get_db_connection
# from models.knowledge_base_editor_model import *


@app.route('/knowledge_base_editor/', methods=['get', 'post'])
def knowledge_base_editor():
    conn = get_db_connection()
    selected_button = 'defect_button'
    data_defect = get_defect(conn)
    data_features = get_feature(conn)
    data_features_scalar = get_feature_scalar(conn)
    data_features_dim = get_feature_dim(conn)
    
    if request.values.get('defect'):
        selected_button = 'defect_button'
        data_defect = get_defect(conn)

    elif request.values.get('feature'):
        selected_button = 'feature_button'
        
        data_features = get_feature(conn)
    elif request.values.get('possible_values_scalar'):
        selected_button = 'possible_values_scalar_button'
        data_features = get_feature_scalar(conn)

    elif request.values.get('possible_values_dim'):
        selected_button = 'possible_values_dim_button'
        data_features_dim = get_feature_dim(conn)

    elif request.values.get('feature_values_defect'):
        selected_button = 'feature_values_defect_button'

    elif request.values.get('technical_description'):
        selected_button = 'technical_description_button'

    elif request.values.get('completeness_knowledge_check'):
        selected_button = 'completeness_knowledge_check_button'

    html = render_template(
        'knowledge_base_editor.html',
        selected_button = selected_button,
        data_defect = data_defect,
        data_features = data_features,
        data_features_scalar = data_features_scalar,
        data_features_dim = data_features_dim,
        len = len
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)