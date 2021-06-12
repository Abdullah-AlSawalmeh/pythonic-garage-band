from abc import ABC, abstractmethod

class Band():
    instances= []
    def __init__(self,name,members):
        self.name = name
        self.members = members
        self.instances.append(self)
    def play_solos(self):
        appended_solos=[]
        for i in self.members:
            appended_solos.append(i.play_solo())
        return appended_solos
    @classmethod
    def to_list(cls):
        return cls.instances
    def __str__(self) -> str:
        return "Great Band"
    def __repr__(self) -> str:
        return "Nothong can beat us"
        
class Musician(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def get_instrument(self):
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass
    @abstractmethod
    def __repr__(self) -> str:
        pass

class Guitarist(Musician):
    instrunment = "guitar"
    def __str__(self) -> str:
        return f"My name is {self.name} and I play {self.instrunment}"
    def __repr__(self) -> str:
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return self.instrunment

class Drummer(Musician):
    instrunment = "drums"
    def __str__(self) -> str:
        return f"My name is {self.name} and I play {self.instrunment}"
    def __repr__(self) -> str:
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return self.instrunment

class Bassist(Musician):
    instrunment = "bass"
    def __str__(self) -> str:
        return f"My name is {self.name} and I play {self.instrunment}"
    def __repr__(self) -> str:
        return f"Bassist instance. Name = {self.name}"
    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self):
        return self.instrunment

if __name__ == "__main__":
    members = [
        Guitarist("Kurt Cobain"),
        Bassist("Krist Novoselic"),
        Drummer("Dave Grohl"),
    ]
    some_band = Band("Nirvana", members)
    joan = Guitarist("Joan Jett")
    print(str(joan))
    the_nobodies = Band("The Nobodies", [])
    print(Band.instances[0])
