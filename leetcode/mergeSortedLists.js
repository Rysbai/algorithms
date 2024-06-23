/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode{
    constructor(val, next){
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}


function linkedListRepr(node){
    let resultText = "";

    while (node){
        resultText += `-> ${node.val}`
        node = node.next
    }

    return resultText;
}


function arrayToLinkedList(arr){
    let head = null
    let tail = null

    for (let i = 0; i < arr.length; i++){
        node = new ListNode(arr[i])
        if (!head){
            head = node
            tail = node
            continue
        }

        tail.next = node
        tail = node
    }

    return head
}


function mergeTwoLists(list1, list2) {
    console.log("list1: " + linkedListRepr(list1))
    console.log("list2: " + linkedListRepr(list2)) 
    let head;
    let tail;


    console.log("start ....")

    while (list1 || list2) {
        let min;
        if ((list1 ? list1.val : Infinity) <= (list2 ? list2.val : Infinity)) {
            min = list1;
            list1 = min?.next;
        } else {
            min = list2;
            list2 = min?.next;
        }
        min.next = null;

        if (head == null) {
            head = min;
            tail = min;
        } else if (tail !== null) {
            tail.next = min;
            tail = min;
        }
        console.log("list1: " + linkedListRepr(list1))
        console.log("list2: " + linkedListRepr(list2))
        console.log("head: " + linkedListRepr(head))
        console.log("----")
    }
    return head
};

console.log("result: " + linkedListRepr(mergeTwoLists(arrayToLinkedList([1,2,4]), arrayToLinkedList([1,3,4]))))
