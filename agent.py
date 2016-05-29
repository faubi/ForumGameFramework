class Agent:
    
    def __init__(self, host):
        self.host = host

    async def loop(self):
        raise NotImplementedError
