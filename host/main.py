import sqlite3, os, argparse, asyncio

from .gamemanager import GameManager

argparser = argparse.ArgumentParser(description='Host for running games')
argparser.add_argument('--game-dir', default='games', help='Directory to load games from')
argparser.add_argument('--database-path', default='gamehost.db', help='Sqlite database file to use')

games = load_games()

# TODO maybe move game loading code elsewhere, merge with agent loader?
def load_games(game_dir='games'):
    if not os.path.exists(game_dir):
        os.mkdir(game_dir)
    if not os.path.isdir(game_dir):
        return []
    games = {}
    for subdir in os.listdir(game_dir):
        try:
            game = load_game(subdir)
            if game.id in games:
                raise ValueError('Duplicate id!')
            games[game.id] = games
        except LoaderError:
            continue
    return games
            game
        
game_manager = GameManager(args.database_path)

game_manager.loaded_gamed(games)

# TODO figure out agent loading stuff

for instance in game_manager.all_instances():
    # TODO call frontend setup function with corresponding agent

eventloop = asyncio.get_event_loop()
agent_loops = [agent.loop() for agent in agents]
eventloop.run_until_complete(asyncio.wait(agent_loops))
