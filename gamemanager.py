# TODO Possible refactor db to separate code?

class GameManager:
    """Manages games and instances"""
    
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.setup_db()
        
    def setup_db(self):
        cursor = db.cursor()
        with open('setup.sql') as sqlfile:
            cursor.executescript(sqlfile.read())
        cursor.close()
        
    def register_game(self, game):
        with self.db:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM games WHERE game_id == ?', (game.id,))
            if not cursor.fetchone():
                cursor.execute('INSERT INTO games (game_id, name) VALUES (?, ?)', (game.id, game.name))
                cursor.execute('DELETE FROM game_agents WHERE game_id=?', (game.id,))
                for agent in game.agents:
                    cursor.execute('INSERT INTO game_agents (game_id, agent_id) VALUES (?, ?)', (game.id, agent))
    
    def get_instance(self, instance_id):
        with self.db:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM instances where id=?', (instance_id,))
            data = cursor.fetchone()
            if not data:
                raise ValueError
            # TODO instance object
            
    def new_instance(self, game, frontends):
        # TODO create instance
        pass
    
    def delete_instance(self, instance_id):
        pass
