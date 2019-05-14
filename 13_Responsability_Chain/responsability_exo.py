import os
import unittest
from abc import ABC
from enum import Enum


class Event(list):
    def __call__(self, *arg, **kwarg):
        for event in self:
            event(*arg, **kwarg)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query(ABC):
    def __init__(self, creature_name, what_to_query, default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Creature:
    def __init__(self, game, name, attack=1, defense=1):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    def perform_query(self, source, query): pass

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source, query): 
        if (self != source and query.what_to_query == WhatToQuery.DEFENSE):
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)

    def query(self, source, query): 
        if (self != source and query.what_to_query == WhatToQuery.ATTACK):
            query.value += 1
        else:
            super().query(source, query)


class Game:
    def __init__(self):
        self.creatures = []


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)
        game.creatures.append(goblin2)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)
        game.creatures.append(goblin3)

        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)


if __name__ == "__main__":
    os.system('clear')
    unittest.main()
