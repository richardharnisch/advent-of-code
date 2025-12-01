import sys

input = sys.stdin.read().strip()
# input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

max_colors = {"red": 12, "green": 13, "blue": 14}


class Game:
    def __init__(self, game):
        name, colors = game.split(":")
        self.idx = int(name.split()[1])
        self.draws = [_.strip() for _ in colors.split(";")]
        self.min_colors = {"red": 0, "green": 0, "blue": 0}

        for draw in self.draws:
            colors = draw.split(", ")
            for color in colors:
                count, name = color.split()
                if int(count) > self.min_colors[name]:
                    self.min_colors[name] = int(count)

    def isPossible(self):
        for draw in self.draws:
            colors = draw.split(", ")
            for color in colors:
                count, name = color.split()
                if int(count) > max_colors[name]:
                    return False
        return True

    def power(self):
        out = 1
        for color in self.min_colors:
            out *= self.min_colors[color]
        return out

    def __repr__(self):
        return f"{self.idx}: {self.draws}"


games = [Game(_) for _ in input.split("\n")]

print(sum([game.power() for game in games]))
