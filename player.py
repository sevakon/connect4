class Player:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return 'Player #{}'.format(self.id)
