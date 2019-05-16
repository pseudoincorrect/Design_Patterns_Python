import unittest


# class Event():
#     def __init__(self):
#         self.rats = 0


class Game:
    def __init__(self):
        self.rats = 0


class Rat:
    def __init__(self, game):
        self.game = game
        # self.attack = 1
        self.game.rats += 1

    @property
    def attack(self):
        return self.game.rats

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rats -= 1


class Evaluate(unittest.TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        # with Rat(game) as rat3:
        #     self.assertEqual(3, rat.attack)
        #     self.assertEqual(3, rat2.attack)
        #     self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == "__main__":
    unittest.main()
