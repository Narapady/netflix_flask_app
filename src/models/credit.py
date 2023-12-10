class Credit:
    columns = ["id", "credit_id", "title_id", "name", "character", "role"]

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
