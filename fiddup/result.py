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
        ) or (
            self.base_file == other.base_file
            and self.compared_file == other.compared_file
        )


class FiddupNameResult(FiddupResultBase):
    similarity: float

    def __init__(self, similarity, base_file, compared_file):
        super().__init__(base_file, compared_file)
        self.similarity = round(similarity, 2)

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file, self.similarity]


class FiddupHashResult(FiddupResultBase):
    file_hash: str
    base_size: int
    compared_size: int

    def __init__(self, base_size, compared_size,
                 file_hash, base_file, compared_file):
        super().__init__(base_file, compared_file)
        self.file_hash = file_hash
        self.base_size = base_size
        self.file_compared_size = compared_size

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file,
                self.file_hash, self.base_size]
