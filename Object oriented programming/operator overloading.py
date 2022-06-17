class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return "M1: {}, M2: {}".format(self.m1, self.m2)


s1 = student(58, 69)
s2 = student(60, 65)
s4 = student(100, 80)

s3 = s1+s2+s4
print(s3.m1, s3.m2)

s5 = s1 > s2
if s1 > s2:
    print("s1 is greater")
else:
    print("s2 is greater")

a = 9
print(a.__str__())
print(s1)
