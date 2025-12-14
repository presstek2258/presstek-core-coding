# Time Complexity: O(n log n) for all cases

class heap_tree:
    def __init__(self, ht_array):
        self.ht_array = ht_array[:]

    def printAsArray(self):
        print(self.ht_array)

    def printAsTree(self):
        depth = 0
        index = 0
        self.printAsTreeRec(index, depth)

    def printAsTreeRec(self, index, depth):
        # for exiting the array
        if index >= len(self.ht_array):
            return None

        # right middle left traversal
        self.printAsTreeRec(2*index + 2, depth + 4)
        print(" "*depth + f"{self.ht_array[index]}")
        self.printAsTreeRec(2*index + 1, depth + 4)

    def parent(self, index):
        return (index - 1)//2

    def right(self, index):
        return 2*index + 2

    def left(self, index):
        return 2*index + 1

    # takes a node and ensures thats its children form a 
    # max heap. (children are always smaller)
    def max_heapify(self, index, heap_size = None):
        if heap_size != None:
            n = heap_size
        else:
            n = len(self.ht_array)

        left = self.left(index)
        right = self.right(index)

        # compare the left and the middle to see which is larger = largest
        if left < n and self.ht_array[left] > self.ht_array[index]:
            largest = left
        else:
            largest = index

        # compare the largest to the right to see which is larger
        if right < n and self.ht_array[right] > self.ht_array[largest]:
            largest = right

        # put the largest at the parent if its not already
        if largest != index:
            temp = self.ht_array[index]
            self.ht_array[index] = self.ht_array[largest]
            self.ht_array[largest] = temp
            self.max_heapify(largest, n) # continue checking further down the tree

    # applies max_heapify() to the entire tree from the bottom-up
    def build_max_heap(self):
        n = len(self.ht_array)
        for index in range((n//2)-1, -1, -1):
            self.max_heapify(index)

    # return the max element (always the root)
    def heap_maximum(self):
        if not self.ht_array:
            return None
        return self.ht_array[0]
    
    # return the max element (always the root)
    # also removes the element
    def heap_extract_max(self):
        if len(self.ht_array) < 1:
            return None # Error: heap underflow
        
        max_value = self.ht_array[0]
        if len(self.ht_array) == 1:
            self.ht_array.pop()
            return max_value

        self.ht_array[0] = self.ht_array.pop()
        self.max_heapify(0) # fix the top
        return max_value
        
    # insert an element at the bottom 
    # then move it up to its correct postition 
    def max_heap_insert(self, value):
        self.ht_array.append(value)
        index = len(self.ht_array)-1

        while index > 0 and self.ht_array[index] > self.ht_array[self.parent(index)]:
            temp = self.ht_array[index]
            self.ht_array[index] = self.ht_array[self.parent(index)]
            self.ht_array[self.parent(index)] = temp

            index = self.parent(index)

    # sorts the array, heap_tree
    def heapsort(self):
        self.build_max_heap()
        n = len(self.ht_array)

        for index in range(n-1, 0, -1):
            temp = self.ht_array[index]
            self.ht_array[index] = self.ht_array[0]
            self.ht_array[0] = temp

            self.max_heapify(0, index)


arr = [3,4,5,6,7,5,4,3,5,2,3,2,2]
ht = heap_tree(arr)
ht.heapsort()
ht.printAsArray()
print()
ht.printAsTree()
