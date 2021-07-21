class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened

    def is_inside(self, value):
        if value == self.start:
            return not self.start_opened

        if value == self.end:
            return not self.end_opened

        return self.start <= value <= self.end

    def stringify(self):
        if self.start_opened:
            start_symbol = "("
        else:
            start_symbol = "["
        if self.end_opened:
            end_symbol = ")"
        else:
            end_symbol = "]"

        return f"{start_symbol}{self.start}, {self.end}{end_symbol}"

    def __str__(self):
        return self.stringify()

    def __repr__(self):
        return self.stringify()