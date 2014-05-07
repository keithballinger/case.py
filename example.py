from __future__ import print_function

from case_object import ANY, CaseObject, case, default


class Person(CaseObject):
    pass


def main():
    keith = Person(name="Keith", age=37)
    bob = Person(name="Bob", age=24)

    p1 = Person(name="Keith")

    p1.best_match(
        case(keith, lambda x: print("Matched Keith")),
        case(bob, lambda x: print("Matched Bob")),
        default = lambda: print("No match")
    )

    p2 = Person(name="Bob", age=50)

    p2.first_exact_match(
        case(Person(name=ANY, age=50), lambda x: print("Matched Bob with ANY")),
        case(Person(name="Bob", age=50), lambda x: print("Matched Bob2")),
        default = lambda: print("No match")
    )


if  __name__ =='__main__':
    main()
