from importlib.machinery import SourceFileLoader

class Game:
    
    def __init__(self, name, id, frontends, core):
        self.name = name
        self.id = id
        self.frontends = frontends
        self.core = core
    
    @staticmethod
    def load(path):
        # TODO figure out game format and loader
