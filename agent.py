# TODO agent-specific config files, also maybe interface for agent-specific APIs

class Agent:
    
    def __init__(self, host):
        self.host = host

    async def loop(self):
        raise NotImplementedError
