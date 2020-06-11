from binary_tree import Node, Binary_Tree

class BST(Binary_Tree):

  def __int__(self):
    super(BST, self).__init__()

  def insert(self, item):
    if self.root is None:
      self.root = Node(item)
    else:
      self.add_item(Node(item), self.root)

  def add_item(self, new_node, node):
    if new_node.val > node.val:
      if node.right is None:
        node.right = new_node
      else:
        self.add_item(new_node,node.right)
    if new_node.val < node.val:
      if node.left is None:
        node.left = new_node
      else:
        self.add_item(new_node, node.left)


if __name__ == '__main__':
  tree = BST()
  tree.insert(3)
  tree.insert(1)
  tree.insert(2)
  tree.insert(4.5)
  tree.insert(4)
  #tree.print_tree()
  tree.print_in_order()
  print('\n***'*2)
  tree.print_in_postorder()
  print('\n***' * 2)
  tree.print_in_preorder()
  print('\n***' * 2)
  tree.print_in_levelorder()