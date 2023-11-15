class PostBaseException(Exception):
    def __init__(self, post_id: int):
        self.post_id = post_id


class ThereIsNoStatisticsForPostException(PostBaseException):
    pass
