class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
