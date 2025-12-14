# Write an implementation of Huffman coding, which is a 
# greedy implementation of assigning prefix codes. This 
# will require a program that does the following:
# 1. Read through a simple ASCII text file (passed as an argument),
# determining the frequency of each character in the file
# 2. Use these frequencies to calculate the optimal prefix 
# codes for each character (Huffman)
#   Print a complete table of prefix codes for the 
#   characters in the document (print only 
#   characters with frequencies > 0)
# 3. Normally, you would then encode each character using its prefix code
#   However, actually implementing this requires some trick 
#   bit manipulation (which, for some languages, is difficult to do)
#   Instead, calculate the length of the entire document 
#   before and after using the prefix codes

class Node:
    def __init__(self, char=None, frequency=None, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.char}: {self.frequency})"

# frequencies is a dictionary of char:frequency pairs
# codes is a dictionary of char:code pairs
class Heap_tree:
    def __init__(self, filename):
        self.root = None
        self.frequencies = {}
        self.filename = filename
        self.codes = {}

        self.set_frequencies()
        self.huffman()
        self.generate_codes()

    def set_frequencies(self):
        # count the frequency of each character
        for char in self.read_file():
            if char in self.frequencies:
                self.frequencies[char] += 1
            else:
                self.frequencies[char] = 1

    def huffman(self):
        nodes = []
        for char, freq in self.frequencies.items():
            nodes.append(Node(char=char, frequency=freq))

        while len(nodes) > 1:
            nodes.sort(key=lambda node: node.frequency)
            x = nodes.pop(0) # smallest frequency node
            y = nodes.pop(0) # smallest frequency node
            # make a parent node for the smaller nodes
            z = Node(left=x, right=y, frequency=x.frequency + y.frequency)
            nodes.append(z)
        self.root = nodes[0]
    
    # generate the huffman codes from the heap tree
    def generate_codes(self):
        self.codes = {}
        self.traversal(self.root, "")

    # traverse to and store leaf nodes by code
    def traversal(self, node, code):
        if node.left is None and node.right is None:
            self.codes[node.char] = code
        else:
            self.traversal(node.left, code + "0")
            self.traversal(node.right, code + "1")
    
    def print_codes(self):
        print("Huffman Codes:")
        for char, code in self.codes.items():
            print(f"'{char}': {code}")

    def read_file(self):
        with open(file=self.filename, mode='r') as file:
            return file.read().strip()

    def print_frequencies(self):
        print("Frequencies:")
        for char,value in self.frequencies.items():
            print(f"'{char}': {value}")

    def print_tree(self):
        depth = 0
        index = 0
        self.print_tree_rec(index, depth, self.root)

    def print_tree_rec(self, index, depth, node):
        if node.right:
            self.print_tree_rec(2*index + 2, depth + 6, node.right)
        print(" "*depth + f"{node}")
        if node.left:
            self.print_tree_rec(2*index + 1, depth + 6, node.left)

    def print_doc_lengths(self):
        n = len(self.frequencies)
        document_length = 0
        variable_encoding_length = 0
        for char,value in self.frequencies.items():
            document_length += value
            variable_encoding_length += value * len(self.codes[char])
        # length of largest number in binary * document length
        fixed_encoding_length = len(f"{n:b}") * document_length

        print(f"ascii document length: {document_length}")
        print(f"fixed encoding length: {fixed_encoding_length}")
        print(f"variable encoding length: {variable_encoding_length}")


# TESTING: basic call to ascii file

ht = Heap_tree("ascii.txt")
ht.print_frequencies()
ht.print_tree()
ht.print_codes()
ht.print_doc_lengths()
