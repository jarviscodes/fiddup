class FiddupResult(object):
    base_file: str
    compared_file: str
    similarity: float

    def __init__(self, base_file, compared_file, similarity):
        self.base_file = base_file
        self.compared_file = compared_file
        self.similarity = round(similarity, 2)

    def __str__(self):
        return f"{self.base_file: <40}{self.compared_file: <40}{self.similarity: <15}"

    def __eq__(self, other):
        return self.base_file == other.compared_file and self.compared_file == other.base_file

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file, self.similarity]
