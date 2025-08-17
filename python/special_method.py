# special, magic, dunder, __xx__

class Tesla(object):

    def __init__(self, owner, color):
        self.owner = owner
        self.color = color
    
    def __str__(self):
        return f"This is {self.color} color {self.owner}'s car"
    
    def __len__(self):
        return len(self.owner)
    
    # def __del__(self):
    #     print("This cas has been deleted")

    def __eq__(self, other):
        return self.color == other.color
    
tesla = Tesla("Mia", "Grey")
# print(len(tesla))
# del tesla
tesla1 = Tesla("Hee", "Red")
print(tesla == tesla1)
