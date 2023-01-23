class DoublyLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
            prev: null,
        };
        // tail = head because there is only one node
        this.tail = this.head;
        this.length = 1;
    }
    append(value) {
        // create a new node
        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        newNode.prev = this.tail;
        // point the tail to the new node
        this.tail.next = newNode;
        // update the tail to the new node
        this.tail = newNode;
        this.length++;
        return this;
    }
    prepend(value) {
        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        this.length++;
        return this;
    }
    printList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    insert(index, value) {
        if (index >= this.length) {
            return this.append(value);
        }
        const newNode = {
            value: value,
            next: null,
            prev: null,
        };
        const leader = this.traverseToIndex(index - 1);
        const follower = leader.next;
        leader.next = newNode;  
        newNode.prev = leader;
        newNode.next = follower;
        follower.prev = newNode;
        this.length++;
        return this.printList();
    }
    traverseToIndex(index) {
        // check params
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }
    remove(index) {
        // check params
        const leader = this.traverseToIndex(index - 1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        this.length--;
        return this.printList();
    }
}


const myLinkedList = new DoublyLinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
console.log(myLinkedList.printList());
myLinkedList.prepend(1);
console.log(myLinkedList.printList());
myLinkedList.insert(2, 99);
// console.log(myLinkedList.printList());
// myLinkedList.remove(2);
console.log(myLinkedList.printList());

