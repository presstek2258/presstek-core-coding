import java.util.ArrayList;
import java.util.List;
import javax.swing.SortOrder;

// Node class to represent each element in the tree
public class Node {
  // Node attributes
  int data;
  Node left;
  Node right;

  // Constructor
  public Node(int data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

public class BST {
  // BST Attributes
  Node root;

  // Constructor for the BST
  public BST() { this.root = null; }

  // Insertion method for adding a value to the tree
  public void insert(int data) { this.root = insertRecursive(this.root, data); }

  // Helper method for recursive insertion
  private Node insertRecursive(Node node, int data) {

    // if spot found, insert data as new node
    if (node == null) {
      return new Node(data);

    } else {
      // otherwise check if the data is less than or greater than the current
      // value and insert recursively
      if (data < node.data) {
        // go left
        node.left = insertRecursive(node.left, data);
      } else {
        // go right
        node.right = insertRecursive(node.right, data);
      }
    }
    // return the node
    return node;
  }

  // Depth-First Search (DFS) method for searching a specific value
  public boolean dfsSearch(int target) {
    // begin recursive search at the root
    return dfsSearchRecursive(this.root, target);
  }

  // Recursive DFS Search helper method
  private boolean dfsSearchRecursive(Node node, int target) {
    // if node reached, it is not found in this branch (our base case)
    if (node == null) {
      return false;
    }

    // Check if the current node contains the target value
    if (node.data == target) {
      return true;
      // Recursively search in the left or right subtrees based on value
    } else if (target < node.data) {
      return dfsSearchRecursive(node.left, target);
    } else {
      return dfsSearchRecursive(node.right, target);
    }
  }

  // In-order Traversal method
  public void inOrderTraversal() {
    // begin traversal at the root
    inOrderRecursive(this.root);
  }

  // Helper method for in-order traversal
  private void inOrderRecursive(Node node) {
    // if we're not yet at a leaf, perform in order (left, node, right)
    // traversal
    if (node.left != null) {
      inOrderRecursive(node.left);
    }
    System.out.println(node.data);
    if (node.right != null) {
      inOrderRecursive(node.right);
    }
  }

  // Deletion method for removing a value from the tree
  public void delete(int data) {
    // set the root to be the result of recursively deleting a value
    this.root = deleteRecursive(this.root, data);
  }

  // Helper method for recursive deletion
  private Node deleteRecursive(Node node, int data) {
    // base case: node not found
    if (node == null) {
      return null;
    }

    if (node.data == data) {
      if (node.right != null && node.left != null) {
        // case 1: 2 children
        // go one spot to the right first
        // then dfs to the left
        Node newNode = node.right;
        if (newNode.left == null) {
          // if you cant go left just promote the right node
          // by adding the left branch under newNode
          newNode.left = node.left;
        } else {
          // otherwise continue dfs'ing to the left
          Node leftmost = findMin(newNode);
          // add the branch under leftmost
          leftmost.left = node.left;
        }
        // this attaches the parent to the newNode
        // since node.left/node.right = recursive call
        return newNode;

      } else {
        // case 2: 0 or 1 child
        // returns null if not found
        // otherwise returns the child if 1
        if (node.left != null) {
          return node.left;
        } else {
          return node.right;
        }
      }
    }

    // recursively search for the node
    node.left = deleteRecursive(node.left, data);
    node.right = deleteRecursive(node.right, data);
    // return the current node
    return node;
  }

  // Helper method to find the minimum value in the tree
  private Node findMin(Node node) {

    // keep traversing left until no more children found
    while (node.left != null) {
      node = node.left;
    }
    // return that node
    return node;
  }

  // Balancing method (simplified version)
  public void balance() {
    // Step 1: Store the elements of the BST in a sorted list
    List<Integer> sortedList = new ArrayList<>();
    // helper method call
    storeInOrder(this.root, sortedList);

    // Step 2: Rebuild the tree by recursively inserting the middle element -
    // helper method
    this.root = buildBalancedTree(sortedList, 0, sortedList.size() - 1);
  }

  // Helper method to perform an in-order traversal and store elements in a
  // sorted list
  private void storeInOrder(Node node, List<Integer> list) {
    // using in-order traversal, but rather than print, add to list
    if (node != null) {
      storeInOrder(node.left, list);
      list.add(node.data);
      storeInOrder(node.right, list);
    }
  }

  // Helper method to rebuild the tree from the sorted list
  private Node buildBalancedTree(List<Integer> sortedList, int start, int end) {
    // base case: if the ends of the list pass each other
    if (start > end) {
      return null;
    }

    // Find the middle element and make it the root
    int mid = (start + end) / 2;
    Node node = new Node(sortedList.get(mid));

    // Recursively build the left and right subtrees b providing appropriate
    // side of list
    node.left = buildBalancedTree(sortedList, start, mid - 1);
    node.right = buildBalancedTree(sortedList, mid + 1, end);

    // return the root
    return node;
  }

  // Method to print the tree in a visually hierarchical way
  public void printTree() { printTreeRecursive(root, "", true); }

  // Helper method to print the tree recursively
  private void printTreeRecursive(Node node, String indent, boolean isLeft) {
    if (node == null) {
      return;
    }

    // Print the current node value with its indentation
    System.out.println(indent + (isLeft ? "L--- " : "R--- ") + node.data);

    // Recursively print the left and right subtrees
    printTreeRecursive(node.left, indent + (isLeft ? "|   " : "    "), true);
    printTreeRecursive(node.right, indent + (isLeft ? "|   " : "    "), false);
  }

  public static void main(String[] args) {
    BST bst = new BST();

    // Insertion
    bst.insert(7);
    bst.insert(4);
    bst.insert(11);
    bst.insert(2);
    bst.insert(5);
    bst.insert(1);
    bst.insert(3);
    bst.insert(10);
    bst.insert(14);
    bst.insert(9);

    bst.printTree();

    // DFS Search
    System.out.println("DFS Search for 3: " + bst.dfsSearch(3));     // true
    System.out.println("DFS Search for 100: " + bst.dfsSearch(100)); // false

    // In-order Traversal
    System.out.println("In-order Traversal: ");
    bst.inOrderTraversal();
    System.out.println();

    // Deletion
    bst.delete(3);
    System.out.println("after Deletion of 3: ");
    bst.printTree();

    // In-order Traversal
    System.out.println("In-order Traversal: ");
    bst.inOrderTraversal();
    System.out.println();

    // Balancing
    bst = new BST();
    bst.insert(20);
    bst.insert(10);
    bst.insert(5);
    bst.insert(11);
    bst.insert(2);
    bst.insert(8);
    bst.insert(15);
    bst.insert(14);
    bst.insert(16);
    bst.insert(13);
    bst.insert(17);

    System.out.println("unbalanced tree: ");
    bst.printTree();

    // Balancing
    bst.balance();
    System.out.println("after Balancing: ");
    bst.printTree();
  }
}
