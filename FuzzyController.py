class FuzzyController:
    def __init__(self):
        pass

    # Треугольная функция принадлежности
    def _trimf(self, a, b, c):
        def helper(x):
            if a <= x <= b:
                return (x - a) / (b - a)
            elif b <= x <= c:
                return (c - x) / (c - b)
            else:
                return 0
        return helper

    # Трапецевидная функция принадлежности
    def _trapmf(self, x, a, b, c, d):
        if a <= x <= b:
            return (x - a) / (b - a)
        elif b <= x <= c:
            return 1
        elif c <= x <= d:
            return (c - x) / (c - b)
        else:
            return 0

    # Z-образная феункия принадлежности
    def _zmf(self, x, a, b):
        if x <= a:
            return 1
        elif a < x <= (a+b)/2:
            return 1 - 2 * ((x-a)/(b-a))**2
        elif (a+b) / 2 < x < b:
            return 2 * ((b-x)/(b-a))**2
        else:
            return 0

    def setMembership(self, functionName):





reg1 = FuzzyController()
mf = reg1._trimf(4, 7, 8)

print(mf(7.7))

