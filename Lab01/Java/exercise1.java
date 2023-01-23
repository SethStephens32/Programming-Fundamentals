package Java;
// Build, in any language, a linked list for integers. 
// a) The list should be ordered all the time.  
// b) It should accept new numbers and insert them where they should be. 
// c) The linked list should be displayed when a change (insertion) occurs. 

import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

class LinkedList {
    Node head;

    LinkedList() {
        head = null;
    }

    void insert(int data) {
        Node newNode = new Node(data);
        if (head == null || head.data >= newNode.data) {
            newNode.next = head;
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null && current.next.data < newNode.data) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
        display();
    }

    void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the integers you want to insert into the list, separated by space:");
        String[] input = scanner.nextLine().split(" ");
        for (String s : input) {
            list.insert(Integer.parseInt(s));
        }
        scanner.close();
    }
}


