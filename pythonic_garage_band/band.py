class Band:

    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        # why does this return line not work????
        # return map(lambda instance: instance.play_solo(), self.members)

        solos_list = []
        for instant in self.members:
            solos_list.append(instant.play_solo())
        return solos_list

    @classmethod
    def to_list(cls):
        return cls.instances


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


if __name__ == "__main__":

    # Just trying to test the last test case here
    print(Band.to_list() == [])
    Band("The Nobodies", [])
    print(len(Band.to_list()) == 1)
