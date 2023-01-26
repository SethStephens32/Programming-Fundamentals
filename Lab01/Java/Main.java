import java.util.Scanner;


public class Main {
    
    class Node {
        int data;
        Node next;
    }

    class SortedLinkedList {
        Node head;
        Node tail;

        public SortedLinkedList() {
            head = null;
            tail = null;
        }

        public void add(int data) {
            Node newNode = new Node();
            newNode.data = data;
            newNode.next = null;

            if (head == null) {
                head = newNode;
                tail = newNode;
            } else {
                Node current = head;
                Node previous = null;

                while (current != null && current.data < data) {
                    previous = current;
                    current = current.next;
                }

                if (previous == null) {
                    newNode.next = head;
                    head = newNode;
                } else {
                    newNode.next = current;
                    previous.next = newNode;
                }
            }
        }

        public void print() {
            Node current = head;
            while (current != null) {
                System.out.print(current.data + " ");
                current = current.next;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // get the user input for the node count
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of nodes: ");
        int nodeCount = scanner.nextInt();
        
        // create an instance of the Main class
        Main main = new Main();
        // create an instance of the SortedLinkedList class
        SortedLinkedList list = main.new SortedLinkedList();
        for (int i = 0; i < nodeCount; i++) {
            System.out.print("Enter the data for node " + (i + 1) + ": ");
            int data = scanner.nextInt();
            list.add(data);

            System.out.print("The list is: ");
            list.print();
        }
    }
}