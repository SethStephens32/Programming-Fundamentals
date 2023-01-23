// linked list: apples --> bananas --> oranges --> grapes --> null

// creating a simple pointer
// doesn;t create a new object in memory instead it points to the same object
// var list = {
//     data: "apples",
// };

// const list2 = list;

// console.log(list2.data); // apples
// console.log(list.data); // apples

// 10 --> 5 --> 16

// let myLinkedList = {
//     head: {
//         value: 10,
//         next: {
//             value: 5,
//             next: {
//                 value: 16,
//                 next: null,
//             },
//         },
//     },
// };

class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
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
        };
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
        };
        newNode.next = this.head;
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
        };
        const leader = this.traverseToIndex(index - 1);
        const holdingPointer = leader.next;
        leader.next = newNode;  
        newNode.next = holdingPointer;
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
    reverse() {
        if (!this.head.next) {
            // equivalent to this.length === 1
            return this.head;
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while (second) {
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
        return this.printList();
    }
}


const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
console.log(myLinkedList.printList());
myLinkedList.prepend(1);
console.log(myLinkedList.printList());
myLinkedList.insert(2, 99);
console.log(myLinkedList.printList());
myLinkedList.remove(2);
console.log(myLinkedList.printList());
myLinkedList.reverse();
console.log(myLinkedList.printList());