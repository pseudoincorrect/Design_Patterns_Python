import unittest


class Mediator:
    def __init__(self):
        self.participants = []

    def broadcast(self, source, value):
        for p in self.participants:
            if p != source:
                p.increase(value)


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.participants.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)

    def increase(self, value):
        self.value += value


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)


if __name__ == "__main__":
    unittest.main()
