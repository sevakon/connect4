class Player:
    def __init__(self, id):
        self.player_id = id

    def __str__(self):
        return 'Player #{}'.format(self.player_id)
