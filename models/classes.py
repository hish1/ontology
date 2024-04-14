import models.sql as sql
import json


class BZ:
    types, features, num_features, possible_values, num_possible_values, values = [], [], [], {}, {}, {}

    # possible_values = {
    #     classes = ['Анкилозавр', 'Стегозавр', 'Орнитопод', 'Пахицефалозавр',
    #                'Цератопс', 'Прозавропод', 'Завропод', 'Теропод']
    #     features = ['Строение таза', 'Тип питания', 'Опорные конечности', 'Размер', 'Период']
    #     'Строение таза' = ['Птицетазовое', 'Ящеротазовое']
    #     'Тип питания' = ['Растительноядное', 'Хищник']
    #     'Опорные конечности' = ['2', '4']
    #     'Размер' = [i for i in range(50)]
    #     'Период' = ['ран Триас', 'ср Триас', 'позд Триас',
    #            'ран Юра', 'ср Юра', 'позд Юра',
    #            'ран Мел', 'ср Мел', 'позд Мел']
    # }

    # values = {
    #     'Анкилозавр': {
    #         'Строение таза': 'Птицетазовое',
    #         'Тип питания': 'Растительноядное',
    #         'Опорные конечности': '4',
    #         'Размер': [i for i in range(2, 9)],
    #         'Период': ['ср Юра', 'позд Юра', 'ран Мел', 'ср Мел', 'позд Мел']
    #     },
    #     ...
    # }

    def __init__(self):
        types = sql.get_types()
        for t in types.values:
            self.types.append(t[0])

        features = sql.get_features()
        for f in features.values:
            if f[1] == 0:
                self.features.append(f[0])
            else:
                self.num_features.append(f[0])

        for f in self.features:
            val = sql.get_possible_value(f)
            arr = []
            for v in val.values:
                arr.append(v[0])
            self.possible_values[f] = arr

        for f in self.num_features:
            val = sql.get_possible_value(f)
            arr = []
            for v in val.values:
                arr.append(int(v[0]))
                if len(arr) == 2:
                    arr.sort()
                    self.num_possible_values[f] = [i for i in range(arr[0], arr[1])]

        for t in self.types:
            self.values[t] = {}
            a = []
            for f in self.features:
                val = sql.get_type_value(t, f)
                arr = []
                for v in val.values:
                    arr.append(v[0])
                self.values[t][f] = arr
            for f in self.num_features:
                val = sql.get_type_value(t, f)
                arr = []
                for v in val.values:
                    arr.append(int(v[0]))
                    if len(arr) == 2:
                        arr.sort()
                self.values[t][f] = [i for i in range(arr[0], arr[1])]


    # def check(self, a):

    def identify(self, dino):
        yes = self.types
        no = ''

        for t in self.values:
            f = True
            n = f'Класс «{t}» не подходит так как:\n'
            for d in dino:
                if isinstance(dino[d], list):
                    for l in dino[d]:
                        if l not in self.values[t][d]:
                            f = False
                            n += f'- признак «{d}» не подходит\n'
                            if t in yes:
                                yes.remove(t)
                            break
                elif dino[d] not in self.values[t][d]:
                    f = False
                    n += f'- признак «{d}» не подходит\n'
                    if t in yes:
                        yes.remove(t)
            if not f:
                no += n + '\n'

        l = ''
        if len(yes) > 1:
            l = 'Подходящие классы динозавров: '
            for y in yes:
                l += f'«{y}», '
            l = l[:-2] + '.\n\n' + no
        elif len(yes) == 1:
            l = f'Подходящий класс динозавров: «{yes[0]}».\n\n' + no
        else:
            l = 'Класс динозавра не удалось определить.\n\n' + no

        return l


bz = BZ()
def get_bz():
    return BZ()

if __name__ == '__main__':
    bz = BZ()

    dino = {
        'Строение таза': 'Птицетазовое',
        'Тип питания': 'Растительноядное',
        'Опорные конечности': '4',
        'Размер': [i for i in range(2, 9)],
        'Период': ['ср Юра', 'позд Юра', 'ран Мел', 'ср Мел', 'позд Мел']
    }

    l = bz.identify(dino)
    # print(l)

    j = json.dumps(bz.possible_values)
    print(j)


