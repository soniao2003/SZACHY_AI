class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto

    def getx_from(self):
        return self.xfrom

    def setx_from(self, x):
        self.xfrom=x

    def gety_from(self):
        return self.yfrom

    def sety_from(self, y):
        self.yfrom = y

    def getx_to(self):
        return self.xto

    def setx_to(self, x):
        self.xto = x

    def gety_to(self):
        return self.yto

    def sety_to(self, y):
        self.yto = y

    def to_string(self):
        string_x_from = chr(ord('a') + self.xfrom)
        string_y_from = str(8 - self.yfrom)
        string_x_to = chr(ord('a') + self.xto)
        string_y_to = str(8 - self.yto)
        return string_x_from + string_y_from + "->" + string_x_to + string_y_to

    def equals(self, checking_move):
        return (
                self.getx_from() == checking_move.getx_from()
                and self.gety_from() == checking_move.gety_from()
                and self.getx_to() == checking_move.getx_to()
                and self.gety_to() == checking_move.gety_to()
        )