class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

  def __str__(self):
    return f'val={self.val}, left={self.left}, right={self.right}'


class Binary_Tree:

  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, item):
    return NotImplemented

  def delete(self):
    pass

  def make_empty(self, node):
    if node:
      self.make_empty(node.right)
      self.make_empty(node.left)
    del node

  def print_in_postorder(self, order='in_order'):
    self._print_in_postorder(self.root)

  def _print_in_postorder(self, node):
    if node is None:
      return
    self._print_in_postorder(node.left)
    self._print_in_postorder(node.right)
    print(f'{node.val} ')

  def print_in_preorder(self, order='in_order'):
    self._print_in_preorder(self.root)

  def _print_in_preorder(self, node):
    if node is None:
      return
    print(f'{node.val} ')
    self._print_in_preorder(node.left)
    self._print_in_preorder(node.right)

  def print_in_order(self):
    self._print_in_order(self.root)

  def _print_in_order(self, node):
    if node is None:
      return
    else:
      self._print_in_order(node.left)
      print(node.val)
      self._print_in_order(node.right)

  def print_in_levelorder(self):
    self._print_in_levelorder([self.root])

  def _print_in_levelorder(self, nodes):
    if not nodes:
      return
    new_nodes = []
    for node in nodes:
      if node is None:
        continue
      print(node.val)
      new_nodes.extend([node.left, node.right])
    self._print_in_levelorder(new_nodes)