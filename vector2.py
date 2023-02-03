from math import sqrt, atan

class Vector2:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def __sub__(self, secondVector):
        NEW_X = secondVector.X - self.X
        NEW_Y = secondVector.Y - self.Y
        return Vector2(NEW_X, NEW_Y)
    def __iter__(self):
        yield self.X
        yield self.Y
    def __str__(self):
        return str(tuple(self))
    def magnitude(self):
        TOTAL_DISTANCE = sqrt((self.X * self.X) + (self.Y * self.Y))
        return TOTAL_DISTANCE
    def dir(self, secondVector):
        DIR_X = self.X - secondVector.X
        DIR_Y = self.Y - secondVector.Y
        return atan(DIR_Y/DIR_X)
        
if __name__ == "__main__":
    pass