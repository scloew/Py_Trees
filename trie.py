class TrieNode:

  def __init__(self, char):
    self.char = char
    self.is_word_end = False
    self.children={}

  def __str__(self):
    return f'char={self.char}; word_end={self.is_word_end}; children={self.children}'

class Trie:

  def __init__(self):
    self.root = {}

  def insert(self, item):
    if item[0] not in self.root.keys():
      self.root[item[0]] = TrieNode(item[0])
    self._add_item(self.root[item[0]], item[1:])

  def _add_item(self, trie_node, item):
    if not item:
      trie_node.is_word_end = True
    else:
      if item[0] not in trie_node.children.keys():
        trie_node.children[item[0]] = TrieNode(item[0])
      self._add_item(trie_node.children[item[0]], item[1:])

  def print_words(self):
    for key, val in self.root.items():
      self._print_helper(val, key)

  def _print_helper(self, trie_node, word):
    # print(f'debug: node val is {trie_node.char}')
    # print(trie_node)
    # print(f'word is {word}')
    # # print('****\n')
    # input('****\n')
    if trie_node.is_word_end:
      print(word)
    for key, val in trie_node.children.items():
      self._print_helper(val, word+key)

if __name__=='__main__':
  tree = Trie()
  tree.insert('word')
  tree.print_words()
  tree.insert('or')
  tree.print_words()
  print('-----')
  tree.insert('a')
  tree.insert('worlds')
  tree.print_words()