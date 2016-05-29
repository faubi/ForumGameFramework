class Frontend:

    def __init__(self, instance_id):
        self.id = instance_id
    
    # Receive event from corresponding game instance
    def receive_event(self):
        raise NotImplementedError
    
    # Setup connection to agent. Used for subscribing to events, etc.
    def setup(self, agent):
        self.agent = agent
    
    # The name of the agent this frontend is for
    agent = None
