class Comparator:
    def __init__(self, compareFunction=None) -> None:
        self.compare = compareFunction or Comparator.defaultCompareFunction

    @staticmethod
    def defaultCompareFunction(a, b):
        if type(a or b) is dict:
            if a == b:
                return 0

            return -1

        if a == b:
            return 0

        return -1 if (a < b) else 1

    def equal(self, a, b):
        return self.compare(a, b) == 0

    def lessThan(self, a, b):
        return self.compare(a, b) < 0

    def greaterThan(self, a, b):
        return self.compare(a, b) > 0

    def lessThanOrEqual(self, a, b):
        return self.lessThan(a, b) or self.equal(a, b)

    def greaterThanOrEqual(self, a, b):
        return self.greaterThan(a, b) or self.equal(a, b)

    def reverse(self):
        compareOriginal = self.compare
        self.compare = lambda a, b: compareOriginal(b, a)
