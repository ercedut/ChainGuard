import secrets

class elliptic_curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p  # prime modulus

    def is_on_curve(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

class ecc_keypair:
    def __init__(self, curve, base_point):
        self.curve = curve
        self.base_point = base_point  # (x, y)
        self.private_key = self.gen_private_key()
        self.public_key = self.scalar_mult(self.private_key, self.base_point)

    def gen_private_key(self):
        return secrets.randbelow(self.curve.p)

    def scalar_mult(self, k, point):
        x, y = point
        result = None
        addend = (x, y)

        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1

        return result

    def point_add(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 and y1 != y2:
            return None

        if x1 == x2:
            m = (3 * x1 * x1 + self.curve.a) * self.mod_inv(2 * y1, self.curve.p)
        else:
            m = (y2 - y1) * self.mod_inv(x2 - x1, self.curve.p)

        m = m % self.curve.p
        x3 = (m * m - x1 - x2) % self.curve.p
        y3 = (m * (x1 - x3) - y1) % self.curve.p

        return (x3, y3)

    def mod_inv(self, k, p):
        return pow(k, -1, p)
