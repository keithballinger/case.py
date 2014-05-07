class CaseObject(object):
    """
    Base class for objects that can be constructed
    and matched against each other.

    TODO: enforce immutability
    """
    def __init__(self, **kwargs):
        self.list = []
        for name, value in kwargs.items():
            setattr(self, name, value)
            self.list.append(name)

    def match(self, *args, **kwargs):
        winner = None
        winner_score = 0
        for case in args:
            if(self.__match_num(case.obj) > winner_score):
                winner = case
                winner_score += 1
        if winner:
            winner.function(self)
        else:
            default = kwargs['default']
            if default:
                default()

    def __match_num(self, obj):
        """
        Number of fields that match. For instance, if self
        has attrs for Name, Age, Gender, and obj has matching
        fields for Name and Gender, then 2 is returned.
        """
        score = 0
        for attr in self.list:
            try:
                if getattr(obj, attr) == getattr(self, attr):
                    score += 1
            except AttributeError:
                pass
        return score


class Case(object):
    def __init__(self, obj, function):
        self.obj = obj
        self.function = function


def case(obj, f):
    return Case(obj, f)


def default(f):
    return Case(None, f)
