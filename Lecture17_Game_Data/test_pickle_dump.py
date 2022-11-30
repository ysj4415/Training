import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y
    def show(self):
        print(f'Name:{self.name} @ ({self.x},{self.y})')

yuri = NPC('Yuri', 100, 200)
print(yuri.__dict__)


yuri.__dict__.update({"name": "jeni", "x":100, "y": 100})

print(yuri.__dict__)