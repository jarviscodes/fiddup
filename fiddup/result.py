class FiddupResultBase(object):
    base_file: str
    compared_file: str

    def __init__(self, base_file, compared_file):
        self.base_file = base_file
        self.compared_file = compared_file

    def __eq__(self, other):
        return (
            self.base_file == other.compared_file
            and self.compared_file == other.base_file
        )


class FiddupNameResult(FiddupResultBase):
    similarity: float

    def __init__(self, similarity, base_file, compared_file):
        super().__init__(base_file, compared_file)
        self.similarity = round(similarity, 2)

    def __str__(self):
        return f"{self.base_file: <40}{self.compared_file: <40}{self.similarity: <15}"

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file, self.similarity]


class FiddupHashResult(FiddupResultBase):
    file_hash: str

    def __init__(self, file_hash, base_file, compared_file):
        super().__init__(base_file, compared_file)
        self.file_hash = file_hash

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file, self.file_hash]
