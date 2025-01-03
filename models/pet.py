from config.config import Config


class Pet:
    def __init__(self, name, mood=100, health=100):
        self.name = name
        self.mood = mood
        self.health = health
        self.id = None

    @classmethod
    def from_db(cls, data):
        pet = cls(data[1], data[2], data[3])
        pet.id = data[0]  # id
        return pet

    def update_status(self):
        self.mood = max(Config.MIN_MOOD,
                        min(self.mood - Config.MOOD_DECAY_RATE,
                            Config.MAX_MOOD))
        self.health = max(Config.MIN_HEALTH,
                          min(self.health - Config.HEALTH_DECAY_RATE,
                              Config.MAX_HEALTH))

    def get_expression(self):
        if self.mood >= 80 and self.health >= 80:
            return "1"
        elif self.mood >= 50 and self.health >= 50:
            return "1"
        elif self.mood >= 30 or self.health >= 30:
            return "1"
        else:
            return "1"

    def get_action(self):
        if self.mood >= 80 and self.health >= 80:
            return "1"
        elif self.mood >= 50 and self.health >= 50:
            return "2"
        elif self.mood >= 30 or self.health >= 30:
            return "3"
        else:
            return "4，4"

    def feed(self):
        self.health = min(self.health + 10, Config.MAX_HEALTH)
        self.mood = min(self.mood + 5, Config.MAX_MOOD)

    def play(self):
        self.mood = min(self.mood + 15, Config.MAX_MOOD)
        self.health = max(self.health - 5, Config.MIN_HEALTH)

    def cure(self):
        self.health = min(self.health + 20, Config.MAX_HEALTH)