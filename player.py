class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    
    def introduce(self):
        print(f"Hello! I'm {self.name} and I'm play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    
    def show_player(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player.name)
        print(f"{name} is not a member of {self.team_name}")

    def show_team_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f'The {self.team_name} has a total of {total_xp}XP')

# team_x = Team("Team X")
# team_x.add_player('mia')

# team_blue = Team("Team Blue")
# team_blue.add_player('nico')

# team_x.show_player()
# team_blue.show_player()

# team_x.show_team_xp()
# team_blue.show_team_xp()
team_x.remove_player('mia')
team_blue.remove_player('nico')
