class Constant:
    @classmethod
    def choices(cls):
        choice_list = []
        for attr in dir(cls):
            if attr.isupper():
                value = getattr(cls, attr)
                choice_list.append((value, attr))
        return choice_list


class ItemCategory(Constant):
    PHYSICS = 'physics'
    CHEMISTRY = 'chemistry'
    CHEMICALS = 'chemicals'
    BIOLOGY = 'biology'
    SAFETY = 'safety'
    MISCELLANEOUS = 'miscellaneous'


class Currency(Constant):
    USD = 'USD'
    LD = 'LD'
