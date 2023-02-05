/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let count = 1;
    let mid = head;
    while(head.next) {
        head = head.next;
        count++;
        if(count % 2 == 0) {
            mid = mid.next;
        }
    }
    return mid;
};