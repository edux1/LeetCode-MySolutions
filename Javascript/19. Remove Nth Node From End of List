/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let l = head;
    let r = head;
    let count = 0;
    while(r.next) {
        count++;
        r = r.next;
    }
    count -= n
    for(let i=0; i<count; i++) {
        l = l.next;
    }
    if(!l.next)
        return null;
    if(count == -1) 
        return l.next
    l.next = l.next.next;
    return head;
};