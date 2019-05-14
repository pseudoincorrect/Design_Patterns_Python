import unittest

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value
        self.parent = None
        if left:  self.left.parent = self
        if right: self.right.parent = self

    def traverse_preorder(self):
        trav = []
        self.traverse_preorder_rec(trav)
        return trav

    def traverse_preorder_rec(self, trav): 
        if not self.value: return
        if self.value: trav.append(self.value)
        if self.left:  self.left.traverse_preorder_rec(trav)
        if self.right: self.right.traverse_preorder_rec(trav)


class Evaluate(unittest.TestCase):
  def test_exercise(self):
    node = Node('a',
                Node('b',
                     Node('c'),
                     Node('d')),
                Node('e'))
    self.assertEqual(
      'abcde',
      ''.join([x for x in node.traverse_preorder()])
    )

if __name__ == "__main__":
    unittest.main()
