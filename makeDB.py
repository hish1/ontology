import sqlite3


con = sqlite3.connect("dinos.sqlite")
con.execute('PRAGMA foreign_keys = ON')
cursor = con.cursor()

con.executescript('''
DROP TABLE IF EXISTS type;
CREATE TABLE type(
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
	type_name VARCHAR(60)
);

INSERT INTO type(type_name) VALUES 
('Анкилозавр'),
('Стегозавр'),
('Орнитопод'),
('Пахицефалозавр'),
('Цератопс'),
('Прозавропод'),
('Завропод'),
('Теропод');
''')

con.executescript('''
DROP TABLE IF EXISTS feature;
CREATE TABLE feature (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
	feature_name VARCHAR(50),
	type INTEGER
);

INSERT INTO feature(feature_name, type)  VALUES 
('Строение таза', 0),
('Тип питания', 0),
('Опорные конечности', 0),
('Размер', 1),
('Период', 0);
''')

con.executescript('''
DROP TABLE IF EXISTS possible_value;
CREATE TABLE possible_value(
    possible_value_id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(30),
    feature_id INTEGER,
    FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE
);

INSERT INTO possible_value(value, feature_id)  VALUES
('Птицетазовое', 1),
('Ящеротазовое', 1),
('Растительноядное', 2),
('Хищник', 2),
('2', 3),
('4', 3),
('ран Триас', 5),
('ср Триас', 5),
('позд Триас', 5),
('ран Юра', 5),
('ср Юра', 5),
('позд Юра', 5),
('ран Мел', 5),
('ср Мел', 5),
('позд Мел', 5);
''')

con.executescript('''
DROP TABLE IF EXISTS num_possible_value;
CREATE TABLE num_possible_value(
    possible_value_id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(30),
    feature_id INTEGER,
    FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE
);

INSERT INTO num_possible_value(value, feature_id)  VALUES
('1', 4),
('50', 4);
''')

con.executescript('''
DROP TABLE IF EXISTS features_list;
CREATE TABLE features_list(
    features_list_id INTEGER PRIMARY KEY AUTOINCREMENT,
	type_id INTEGER,
    feature_id INTEGER,
    FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES type (type_id) ON DELETE CASCADE
);

INSERT INTO features_list(type_id, feature_id)  VALUES 
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5),
(5, 1),
(5, 2),
(5, 3),
(5, 4),
(5, 5),
(6, 1),
(6, 2),
(6, 3),
(6, 4),
(6, 5),
(7, 1),
(7, 2),
(7, 3),
(7, 4),
(7, 5),
(8, 1),
(8, 2),
(8, 3),
(8, 4),
(8, 5);
''')

con.executescript('''
DROP TABLE IF EXISTS value;
CREATE TABLE value(
    value_id INTEGER PRIMARY KEY AUTOINCREMENT,
	value VARCHAR(30),
    features_list_id INTEGER,
    FOREIGN KEY (features_list_id) REFERENCES features_list (features_list_id) ON DELETE CASCADE
);

INSERT INTO value(value, features_list_id)  VALUES
('Птицетазовое', 1),
('Растительноядное', 2),
('4', 3),
('2', 4),
('9', 4),
('ср Юра', 5),
('позд Юра', 5),
('ран Мел', 5),
('ср Мел', 5),
('позд Мел', 5),
('Птицетазовое', 6),
('Растительноядное', 7),
('4', 8),
('9', 9),
('12', 9),
('ср Юра', 10),
('позд Юра', 10),
('ран Мел', 10),
('ср Мел', 10),
('Птицетазовое', 11),
('Растительноядное', 12),
('2', 13),
('9', 14),
('12', 14),
('ран Юра', 15),
('ср Юра', 15),
('позд Юра', 15),
('ран Мел', 15),
('ср Мел', 15),
('позд Мел', 15),
('Птицетазовое', 16),
('Растительноядное', 17),
('2', 18),
('2', 19),
('6', 19),
('ран Мел', 20),
('ср Мел', 20),
('позд Мел', 20),
('Птицетазовое', 21),
('Растительноядное', 22),
('2', 23),
('1', 24),
('9', 24),
('позд Юра', 25),
('ран Мел', 25),
('ср Мел', 25),
('позд Мел', 25),
('Ящеротазовое', 26),
('Растительноядное', 27),
('2', 28),
('6', 29),
('12', 29),
('позд Триас', 30),
('ран Юра', 30),
('Ящеротазовое', 31),
('Растительноядное', 32),
('4', 33),
('25', 34),
('40', 34),
('позд Триас', 35),
('ран Юра', 35),
('ср Юра', 35),
('позд Юра', 35),
('ран Мел', 35),
('ср Мел', 35),
('позд Мел', 35),
('Ящеротазовое', 36),
('Хищник', 37),
('2', 38),
('2', 39),
('13', 39),
('ран Триас', 40),
('ср Триас', 40),
('позд Триас', 40),
('ран Юра', 40),
('ср Юра', 40),
('позд Юра', 40),
('ран Мел', 40),
('ср Мел', 40),
('позд Мел', 40);
''')


# con.executescript('''
# CREATE TABLE IF NOT EXISTS subject(
# subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
# subject_name VARCHAR(30)
# );
#
# INSERT INTO subject (subject_name)
# VALUES
# ('Русский язык'),
# ('Математика'),
# ('Математика профильная'),
# ('Физика'),
# ('Химия'),
# ('История'),
# ('Обществознание'),
# ('Информатика'),
# ('Биология'),
# ('География'),
# ('Иностранный язык'),
# ('Литература');
# ''')


# con.executescript('''
# CREATE TABLE IF NOT EXISTS applicant(
# applicant_id INTEGER PRIMARY KEY AUTOINCREMENT,
# applicant_name VARCHAR(100)
# );
#
# INSERT INTO applicant (applicant_name)
# VALUES
# ('Богданов Артём Гордеевич'),
# ('Иванов Александр Иванович'),
# ('Ковалев Борис Никитич'),
# ('Чумаков Андрей Юрьевич'),
# ('Яковлев Артём Тимурович'),
# ('Николаев Георгий Маратович'),
# ('Столяров Серафим Максимович'),
# ('Глебов Александр Иванович'),
# ('Петров Кирилл Даниилович'),
# ('Богданов Роман Иванович'),
# ('Гуляев Никита Тимофеевич'),
# ('Яковлев Тимур Константинович'),
# ('Филиппов Даниил Максимович'),
# ('Новиков Илья Елисеевич'),
# ('Дементьев Данила Матвеевич'),
# ('Никитин Михаил Тимофеевич'),
# ('Демин Михаил Владиславович'),
# ('Румянцев Александр Иванович'),
# ('Поляков Даниэль Филиппович'),
# ('Краснов Иван Кириллович'),
# ('Лазарев Тихон Матвеевич'),
# ('Козлов Алексей Сергеевич'),
# ('Волкова Анастасия Ивановна'),
# ('Федорова Вероника Данииловна'),
# ('Зайцева Александра Дмитриевна'),
# ('Петровская Ольга Матвеевна'),
# ('Логинова Диана Максимовна'),
# ('Пономарева Ника Арсентьевна'),
# ('Николаева Александра Львовна'),
# ('Герасимова Анна Артёмовна'),
# ('Левина Мария Даниловна'),
# ('Ефимова Ясмин Данииловна'),
# ('Чернова Анна Матвеевна'),
# ('Михеева Стефания Кирилловна'),
# ('Бородина Алиса Арсентьевна'),
# ('Логинова Валерия Андреевна'),
# ('Тихонова Анастасия Александровна'),
# ('Виноградова София Егоровна'),
# ('Егорова Маргарита Борисовна'),
# ('Тарасова Виктория Васильевна'),
# ('Антонова Эмилия Александровна'),
# ('Лаврентьева Мелисса Сергеевна'),
# ('Ковалева Софья Леоновна'),
# ('Чернова София Алексеевна');
# ''')


# con.executescript('''
# CREATE TABLE IF NOT EXISTS direction(
# direction_id INTEGER PRIMARY KEY AUTOINCREMENT,
# direction_name VARCHAR(100)
# );
#
# INSERT INTO direction (direction_name)
# VALUES
# ('Социально-экономические науки'),
# ('Гуманитарные науки'),
# ('Инженерные науки и технологии'),
# ('Естественные науки'),
# ('Медицина и здравоохранение'),
# ('Педагогические науки'),
# ('IT и математика');
# ''')


# con.executescript('''
# CREATE TABLE IF NOT EXISTS applicant_subjects(
# applicant_subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
# applicant_id INTEGER,
# subject_id INTEGER,
# result INTEGER,
# FOREIGN KEY (applicant_id) REFERENCES applicant (applicant_id) ON DELETE CASCADE,
# FOREIGN KEY (subject_id) REFERENCES subject (subject_id) ON DELETE CASCADE
# );
#
# INSERT INTO applicant_subjects (applicant_id, subject_id, result)
# VALUES
# (2, 1, 93),
# (2, 3, 86),
# (2, 4, 65),
# (2, 8, 82);
# ''')

# con.executescript('''
# CREATE TABLE IF NOT EXISTS applicant_choice(
# applicant_choice_id INTEGER PRIMARY KEY AUTOINCREMENT,
# applicant_id INTEGER,
# specialization_id INTEGER,
# choice priority INTEGER,
# FOREIGN KEY (applicant_id) REFERENCES applicant (applicant_id) ON DELETE CASCADE,
# FOREIGN KEY (specialization_id) REFERENCES specialization (specialization_id) ON DELETE CASCADE
# );
# ''')


# con.executescript('''
# CREATE TABLE IF NOT EXISTS specialization(
# specialization_id INTEGER PRIMARY KEY AUTOINCREMENT,
# direction_id INTEGER,
# specialization_name VARCHAR(100),
# specialization_description TEXT,
# specialization_duration INTEGER,
# specialization_study_form VARCHAR(30),
# specialization_study_lang VARCHAR(30),
# specialization_price INTEGER,
# specialization_budget INTEGER,
#
#specialization_last_budget_score INTEGER,
# FOREIGN KEY (direction_id) REFERENCES direction (direction_id) ON DELETE CASCADE
# );
#
# INSERT INTO specialization (direction_id, specialization_name, specialization_description,
# specialization_duration, specialization_study_form, specialization_study_lang,
# specialization_price, specialization_budget, specialization_last_budget_score)
# VALUES
# (3, 'Интегрированные системы летательных аппаратов', 'Область профессиональной деятельности специалиста включает
# интегрированные бортовые системы летательных аппаратов (самолетов, вертолетов, ракет), обеспечивающие их нормальное,
# целевое функционирование: системы управления вооружением летательных аппаратов, включая прицельно-навигационные
# системы, механизмы и системы управления для решения задач доставки, подготовки к боевому использованию и применению
# авиационных средств поражения, системы автоматизированных приводов и исполнительных механизмов, методы и средства
# анализа эффективности боевого применения авиационных комплексов, а также процессов разработки
# программно-математического обеспечения бортовых систем.', 5, 'Очная', 'Русский', '-', '-', '-'),
# (3, 'Горное дело', 'Образовательная программа предусматривает теоретическую и практическую подготовку, позволяющую
# сформировать специалиста широкого профиля, востребованного не только на предприятиях горнодобывающего комплекса,
# но и в других отраслях народного хозяйства. Горный инженер-технолог организует и обеспечивает безопасную добычу
# полезных ископаемых и на поверхности и под землей, проектирует новые рудники, шахты, подземные сооружения,
# эксплуатирует сложную горнодобывающую технику.', 4, 'Очная', 'Русский', '-', '-', '-'),
# (3, 'Мехатроника и робототехника', 'Направление осуществляет подготовку специалистов в области современного
# проектирования, исследования, производства и эксплуатации мехатронных и робототехнических систем.
# Программа подготовки сбалансированно сочетает в себе необходимые теоретические аспекты и современные практические
# навыки для работы будущего квалифицированного специалиста.', 4, 'Очная', 'Русский', '-', '18', '149'),
# (3, 'Конструкторско-технологическое обеспечение машиностроительных производств', 'Программа ориентирует выпускников
# на активное участие и инициативу в прорывном развитии классических машиностроительных производств, на освоение новой
# техники, внедрение новых технологий, изменение культуры производства, следование основным направлениям развития
# четвертой промышленной революции.', 4, 'Очная', 'Русский', '-', '-', '-'),
# (5, 'Медицинская биофизика', 'Программа обучения предоставляет комплексную подготовку, объединяя теоретические
# знания и практические навыки диагностики организма человека. Выпускники могут трудоустроиться в качестве врачей
# функциональной диагностики без ординатуры. Практический опыт, полученный в процессе обучения, делает их
# востребованными специалистами.', 6, 'Очная', 'Русский', '305000', '20', '136'),
# (7, 'Цифровые двойники и киберфизические системы', 'Цифровые двойники и киберфизические системы рассматривают
# представление реальности в виртуальных компьютерных моделях и оптимизацию объектов и процессов реального мира на
# основе постоянного получения от них данных. Целью образовательной программы является подготовка специалистов по
# разработке систем, основанных на этих новых технологических платформах, и предназначенных для решения широкого
# класса задач автоматизации и управления.', 4, 'Очная', 'Русский', '245000', '25', '-'),
# (7, 'Организация и технология защиты информации в сфере коммерческой деятельности', 'В рамках этой программы
# ты узнаешь, как выявлять угрозы безопасности на этапе проектирования информационных систем, освоишь безопасную
# разработку и тестирование безопасности в соответствии с российскими и международными требованиями в данной области.
# В ходе обучения ты получишь навыки работы со специализированными программными средами, научишься технике
# тестирования систем в рамках парадигмы Red/Blue Team, освоишь
#методики этичного хакинга, на основе которой в
# дальнейшем сможешь сдать экзамены на международный сертификат CEH. Также в данной программе особое внимание
# уделяется обучению по международным программам CISCO с возможностью получения соответствующих сертификатов.',
# 4, 'Очная', 'Русский', '250000', '50', '223'),
# (7, 'Программирование робототехнических систем', 'Курс для студентов, интересующихся программированием и
# робототехникой. Вы познакомитесь с 3D-моделированием, тестированием программ и математическими основами
# робототехники. Научитесь создавать и отлаживать программы для управления роботами.', 4, 'Очная', 'Русский',
# '245000', '-', '195'),
# (7, 'Аналитика цифрового следа', 'Программа ориентирована на подготовку специалистов к новому, перспективному
# направлению профессиональной деятельности — моделированию, сбору и анализу данных цифрового следа. Основная цель
# данной профессиональной деятельности — повышение качества управленческих решений на основе результатов комплексного
# анализа цифрового следа человека (групп людей). Программа подойдет для тех, кто интересуется современными
# информационными системами и технологиями, в частности технологиями сбора, хранения и анализа больших объемов
# разнородных данных, программированием, методами искусственного интеллекта.', 4, 'Очная', 'Русский',
# '245000', '50', '195'),
# (4, 'Электроника и наноэлектроника', 'Получи базовые знания по физике, математике и информатике, а углуби и расширь
# их с помощью специальных курсов по электротехнике, физике конденсированных сред и программированию. Пройди
# теоретические занятия вместе с практическими и научной работой на современном электровакуумном оборудовании.', 4,
# 'Очная', 'Русский', '225000', '20', '178'),
# (4, 'Цифровая физика', '"Цифровая физика" - это программа для обучения физике, математике и информатике.
# Здесь ты сможешь научиться программированию на современных языках и применять их для решения научных задач.
# Получи полезный опыт и будь готов к работе в науке и технологиях.', 4, 'Очная', 'Русский', '225000', '-', '134'),
# (4, 'Технологии и менеджмент материалов', 'Станьте экспертом в области контроля качества материалов и изделий,
# используемых в энергетике, строительстве, медицине и других сферах. Получите знания о современных технологиях
# производства и получения материалов. Программа подготовит вас к успешной карьере в промышленности.', 4, 'Очная',
# 'Русский', '225000', '20', '147'),
# (4, 'Химия и химическая инженерия (совместно с АО НЗМУ)', 'Изучайте химию и технологию производства материалов,
# работайте с современными методами исследований в нашей программе. Станьте экспертом в области органических и
# неорганических веществ, готовьтесь к карьере в промышленности. Наш партнер - Находкинский завод минеральных
# удобрений.', 4, 'Очная', 'Русский', '225000', '20', '149');
# ''')



# con.executescript('''
# CREATE TABLE IF NOT EXISTS specialization_subjects(
# specialization_subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
# specialization_id INTEGER,
# subject_id INTEGER,
# min_result INTEGER,
# level INTEGER,
# FOREIGN KEY (specialization_id) REFERENCES specialization (specialization_id) ON DELETE CASCADE,
# FOREIGN KEY (subject_id) REFERENCES subject (subject_id) ON DELETE CASCADE
# );
#
# INSERT INTO specialization_subjects (specialization_id, subject_id, min_result, level)
# VALUES
# (1, 1, 40, 1),
# (1, 4, 39, 2),
# (1, 5, 39, 2),
# (1, 11, 30, 2),
# (1, 8, 44, 2),
# (1, 3, 39, 3),
# (2, 1, 40, 1),
# (2, 4, 39, 2),
# (2, 5, 39, 2),
# (2, 11, 30, 2),
# (2, 8, 44, 2),
# (2, 3, 39, 3),
# (3, 1, 40, 1),
# (3, 4, 39, 2),
# (3, 5, 39, 2),
# (3, 11, 30, 2),
# (3, 8, 44, 2),
# (3, 3, 39, 3),
# (4, 1, 40, 1),
# (4, 4, 39, 2),
# (4, 5, 39, 2),
# (4, 11, 30, 2),
# (4, 8, 44, 2),
# (4, 3, 39, 3),
# (5, 1, 40, 1),
# (5, 3, 39, 2),
# (5, 5, 39, 2),
# (5, 11, 30, 2),
# (5, 8, 44, 2),
# (5, 9, 39, 2),
# (5, 4, 39, 3),
# (6, 1, 40, 1),
# (6, 4, 39, 2),
# (6, 8, 44, 2),
# (6, 3, 39, 3),
# (7, 1, 40, 1),
# (7, 4, 39, 2),
#
#(7, 8, 44, 2),
# (7, 3, 39, 3),
# (8, 1, 40, 1),
# (8, 4, 39, 2),
# (8, 8, 44, 2),
# (8, 3, 39, 3),
# (9, 1, 40, 1),
# (9, 4, 39, 2),
# (9, 8, 44, 2),
# (9, 3, 39, 3),
# (10, 1, 40, 1),
# (10, 4, 39, 2),
# (10, 5, 39, 2),
# (10, 8, 44, 2),
# (10, 3, 39, 3),
# (11, 1, 40, 1),
# (11, 3, 39, 2),
# (11, 5, 39, 2),
# (11, 11, 30, 2),
# (11, 8, 44, 2),
# (11, 4, 39, 3),
# (12, 1, 40, 1),
# (12, 4, 39, 2),
# (12, 5, 39, 2),
# (12, 11, 30, 2),
# (12, 8, 44, 2),
# (12, 3, 39, 3),
# (13, 1, 40, 1),
# (13, 3, 39, 2),
# (13, 4, 39, 2),
# (13, 8, 44, 2),
# (13, 9, 39, 2),
# (13, 5, 39, 3);
# ''')

con.commit()
con.close()