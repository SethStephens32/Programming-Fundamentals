class Node {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  class BinaryTree {
    constructor() {
      this.root = null;
    }
  
    insert(value) {
      if (this.root === null) {
        this.root = new Node(value);
      } else {
        this.insertNode(this.root, value);
      }
    }
  
    insertNode(node, value) {
      if (node.value > value) {
        if (node.left === null) {
          node.left = new Node(value);
        } else {
          this.insertNode(node.left, value);
        }
      } else {
        if (node.right === null) {
          node.right = new Node(value);
        } else {
          this.insertNode(node.right, value);
        }
      }
    }
  
    traversePreOrder() {
      this.preOrder(this.root);
    }

    preOrder(node) {
        if (node !== null) {
            // console.log it to where it appears either to the left or the right of the node above it
            // using spaces to indicate the level of the tree
            console.log(node.value);
            this.preOrder(node.left);
            this.preOrder(node.right);
        }
        }

    traverseInOrder() {
        this.inOrder(this.root);
    }

    inOrder(node) {
        if (node !== null) {
            this.inOrder(node.left);
            console.log(node.value);
            this.inOrder(node.right);
        }
    }
}

    const tree = new BinaryTree();
    tree.insert(2);
    tree.insert(3);
    tree.insert(4);
    tree.insert(5);
    tree.insert(7);
    tree.insert(9);
    tree.insert(10);
    tree.insert(11);
    tree.traversePreOrder();
    console.log("-----------------");
    tree.traverseInOrder();
    console.log("-----------------");