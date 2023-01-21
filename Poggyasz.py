class Poggyasz:
    def __init__(self, sor):
        self.a = int(sor[0])
        self.b = int(sor[1])
        self.c = int(sor[2])
        self.m = int(sor[3])

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}, {self.m}"
