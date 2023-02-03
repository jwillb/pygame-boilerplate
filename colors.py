import colorsys

class Color():
    def __init__(self):
        pass

    def __iter__(self):
        yield self.A
        yield self.B
        yield self.C

    def __str__(self):
        return str(tuple(self))

class RGB(Color):
    def __init__(self, R=0, G=0, B=0):
        super().__init__()
        self.A = R
        self.B = G
        self.C = B

    def toHSV(self):
        return HSV(*colorsys.rgb_to_hsv(self.A, self.B, self.C))

class HSV(Color):
    def __init__(self, H, S, V):
        super().__init__()
        self.A = H
        self.B = S
        self.C = V

    def toRGB(self):
        return RGB(*colorsys.hsv_to_rgb(self.A, self.B, self.C))

if __name__ == "__main__":
    RGB_COLOR = RGB(255, 255, 255)
    HSV_COLOR = HSV(0, 1, 1)

    print(RGB_COLOR.toHSV())