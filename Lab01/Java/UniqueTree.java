import java.util.Scanner;

public class UniqueTree {
    
    public TreeNode root;

    public UniqueTree(){
        this.root = null;
    }

    public void insertNode(int value) {
        TreeNode newNode = new TreeNode(value);

        if(root == null){
            root = newNode;
            return;
        }

        TreeNode current = root;

        while(current != null){
            if(value < current.data){
                if(current.leftChild == null){
                    current.leftChild = newNode;
                    return;
                }
                current = current.leftChild;
            }
            else{
                if(current.rightChild == null){
                    current.rightChild = newNode;
                    return;
                }
                current = current.rightChild;
            }
        }
    }

    public void displayTree(TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        displayTree(node.leftChild, depth + 1);
        for (int i = 0; i < depth; i++) {
            System.out.print(" ");
        }
        System.out.println(node.data);
        displayTree(node.rightChild, depth + 1);
    }

    public static void main(String[] args){
        UniqueTree uniqueBinaryTree = new UniqueTree();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter a number: ");
            int value = scanner.nextInt();
            if (value == 0) {
                break;
            }
            uniqueBinaryTree.insertNode(value);
            uniqueBinaryTree.displayTree(uniqueBinaryTree.root, 0);
        }
    }  

    public class TreeNode {
        int data;
        TreeNode leftChild;
        TreeNode rightChild;
        
        public TreeNode(int value) {
            this.data = value;
            this.leftChild = null;
            this.rightChild = null;
        }
    }
}

