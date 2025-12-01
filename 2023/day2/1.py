import sys

input = sys.stdin.read().strip()

max_colors = {"red": 12, "green": 13, "blue": 14}


class Game:
    def __init__(self, game):
        name, colors = game.split(":")
        self.idx = int(name.split()[1])
        self.draws = [_.strip() for _ in colors.split(";")]

    def isPossible(self):
        for draw in self.draws:
            colors = draw.split(", ")
            for color in colors:
                count, name = color.split()
                if int(count) > max_colors[name]:
                    return False
        return True

    def __repr__(self):
        return f"{self.idx}: {self.draws}"


games = [Game(_) for _ in input.split("\n")]

print(sum([game.idx for game in games if game.isPossible()]))
