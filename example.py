from __future__ import print_function

from case_object import CaseObject, case, default


class Person(CaseObject):
    pass


def main():
    keith = Person(name="Keith", age=37)
    bob = Person(name="Bob", age=24)

    p1 = Person(name="Keith")

    p1.match(
        case(keith, lambda x: print("Matched Keith")),
        case(bob, lambda x: print("Matched Bob")),
        default = lambda: print("No match")
    )

    p2 = Person(name="Bob", age=50)

    p2.match(
        case(Person(name="Bob"), lambda x: print("Matched Bob1")),
        case(Person(name="Bob", age=50), lambda x: print("Matched Bob2")),
        default = lambda: print("No match")
    )


if  __name__ =='__main__':
    main()
