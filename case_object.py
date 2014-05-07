
class _ANY(object):
    """
    A helper object that compares equal to everything.
    Shamelessly stolen from Mock.
    """

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    def __repr__(self):
        return '<ANY>'

ANY = _ANY()


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

    def best_match(self, *args, **kwargs):
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

    def first_exact_match(self, *args, **kwargs):
        for case in args:
            if(self.__is_hard_match(case.obj)):
                case.function(self)
                return
        default = kwargs['default']
        if default:
            default()

    def __is_hard_match(self, obj):
        """
        True is the objects are an exact match, defined
        as each attribute matching, or ANY for that attribute.
        """
        for attr in self.list:
            try:
                if getattr(obj, attr) != getattr(self, attr):
                    return False
            except AttributeError:
                pass
        return True


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
