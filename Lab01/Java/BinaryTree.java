import java.util.Scanner;

public class BinaryTree {
    private Node root;
    
    public BinaryTree() {
        this.root = null;
    }
    
    public void insert(int value) {
        root = insert(root, value);
    }
    
    private Node insert(Node node, int value) {
        if (node == null) {
            return new Node(value);
        }
        if (value < node.value) {
            node.left = insert(node.left, value);
        } else if (value > node.value) {
            node.right = insert(node.right, value);
        }
        return node;
    }
    
    public void display() {
        if (root == null) {
            System.out.println("Tree is empty.");
        } else {
            display(root, 0);
        }
    }
    
    private void display(Node node, int depth) {
        if (node == null) {
            return;
        }
        for (int i = 0; i < depth; i++) {
            System.out.print(" ");
        }
        System.out.println(node.value);
        display(node.left, depth + 1);
        display(node.right, depth + 1);
    }
    
    private class Node {
        int value;
        Node left;
        Node right;
        
        public Node(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }
        public static void main(String[] args) {
            BinaryTree bt = new BinaryTree();
            // get the user input for the node count
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the number of nodes: ");
            int nodeCount = scanner.nextInt();
             
            // get user input for the data for each node
            for (int i = 0; i < nodeCount; i++) {
                System.out.print("Enter the data for node " + (i + 1) + ": ");
                int data = scanner.nextInt();
                bt.insert(data);
                // print the tree
                bt.display();
            }
        }
    }
