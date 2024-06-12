class WiiSports:
    def __init__(self, save_number, campaign):
        self.save_number = save_number
        self.games = 5
        self.training = 15
        self._connected_remotes = 0
        self.campaign = campaign

    @property
    def connected_remotes(self):
        return self._connected_remotes

    @connected_remotes.setter
    def connected_remotes(self, value):
        if not isinstance(value, int):
            raise ValueError("Connected remotes must be an integer")
        if value < 0 or value > 4:
            raise ValueError("Number of connected remotes must be between 0 and 4")
        self._connected_remotes = value

new_save = WiiSports(save_number=1, campaign=15.0)

print(new_save.connected_remotes)  # Output: 0

new_save.connected_remotes = 2
print(new_save.connected_remotes)  # Output: 2

new_save.connected_remotes = -1  # Raises ValueError: Number of connected remotes must be between 0 and 4


new_save.connected_remotes = 5  # Raises ValueError: Number of connected remotes must be between 0 and 4

new_save.connected_remotes = 'three'  # Raises ValueError: Connected remotes must be an integer
