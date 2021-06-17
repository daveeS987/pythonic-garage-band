class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.role} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"
        self.role = "Guitarist"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"
        self.role = "Bassist"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"
        self.role = "Drummer"

    @staticmethod
    def play_solo():
        return "rattle boom crash"
