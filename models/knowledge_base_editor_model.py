import pandas


def get_defect(conn):
    return pandas.read_sql(
        '''SELECT * FROM defect''',
        conn)

def get_feature(conn):
    return pandas.read_sql(
        '''SELECT * FROM feature''',
        conn)

def get_feature_scalar(conn):
    return pandas.read_sql(
        '''SELECT * FROM feature
                WHERE feature_id in (
                SELECT DISTINCT feature_id FROM possible_values_scalar)''',
        conn)

def get_feature_dim(conn):
    return pandas.read_sql(
        '''SELECT * FROM feature
                WHERE feature_id in (
                SELECT DISTINCT feature_id FROM possible_values_dimensional)''',
        conn)

def get_applicant_name(conn, id):
    result = pandas.read_sql(
        '''SELECT applicant_name
                FROM applicant
                WHERE applicant_id = :id''',
        conn, params={'id': id})
    if not result.empty:
        return result['applicant_name'].iloc[0]
    else:
        return None

def get_app_results(conn, id):
    result = pandas.read_sql(
        '''SELECT subject.subject_name, applicant_subjects.result
            FROM subject
            JOIN applicant_subjects USING(subject_id)
            JOIN applicant USING(applicant_id)
            WHERE applicant_id = :id;''',
        conn, params={'id': id})
    if not result.empty:
        app_results = []
        for index, row in result.iterrows():
            app_results.append([row['subject_name'], row['result']])
        return app_results
    else:
        return None


def get_direction(conn):
    return pandas.read_sql(
        '''SELECT * FROM direction''',
        conn)


def get_applicant_specializations(conn, applicant_id):
    return pandas.read_sql('''
        SELECT DISTINCT s.*
        FROM specialization s
        JOIN specialization_subjects ss ON s.specialization_id = ss.specialization_id
        JOIN subject sub ON ss.subject_id = sub.subject_id
        JOIN applicant_subjects asub ON sub.subject_id = asub.subject_id
        JOIN applicant a ON asub.applicant_id = a.applicant_id
        WHERE a.applicant_id = :id AND asub.result >= ss.min_result
        AND s.specialization_id NOT IN (
            SELECT ac.specialization_id
            FROM applicant_choice ac
            WHERE ac.applicant_id = :id
        );
        ''', conn, params={'id': applicant_id})


def get_filter_applicant_specializations(conn, applicant_id, directions):
    if directions == []:
        directions = get_direction(conn)['direction_id'].tolist()
    sql_query = '''
        SELECT DISTINCT s.*
        FROM specialization s
        JOIN specialization_subjects ss ON s.specialization_id = ss.specialization_id
        JOIN subject sub ON ss.subject_id = sub.subject_id
        JOIN applicant_subjects asub ON sub.subject_id = asub.subject_id
        JOIN applicant a ON asub.applicant_id = a.applicant_id
        WHERE a.applicant_id = ? AND asub.result >= ss.min_result
        AND s.specialization_id NOT IN (
            SELECT ac.specialization_id
            FROM applicant_choice ac
            WHERE ac.applicant_id = ?
        )
        AND s.direction_id IN ({});
        '''.format(','.join('?' * len(directions)))
    params = (applicant_id,) + (applicant_id,) + tuple(directions)
    return pandas.read_sql(sql_query, conn, params=params)


def get_chosen_applicant_specializations(conn, applicant_id):
    return pandas.read_sql('''
        SELECT DISTINCT s.*, ac.priority
        FROM specialization s
        JOIN applicant_choice ac USING(specialization_id)
        WHERE ac.applicant_id = :id
        ORDER BY ac.priority;
        ''', conn, params={'id': applicant_id})


def get_applicant_available_priority(conn, applicant_id):
    return pandas.read_sql('''
        SELECT number
            FROM (SELECT 1 AS number
                    UNION
                    SELECT 2
                    UNION
                    SELECT 3) AS numbers
                    WHERE number NOT IN (SELECT priority FROM applicant_choice
                    WHERE applicant_id = :id);
        ''', conn, params={'id': applicant_id})


def add_chosen_applicant_specialization(conn, applicant_id, specialization_id, priority):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO applicant_choice (applicant_id, specialization_id, priority)
        VALUES
        (:app, :spec, :pr);
        ''', {'app': applicant_id, 'spec': specialization_id, 'pr': priority})
    conn.commit()


def del_chosen_applicant_specialization(conn, applicant_id, specialization_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM applicant_choice
        WHERE applicant_id = :app AND specialization_id = :spec;''', {'app': applicant_id, 'spec': specialization_id})
    conn.commit()