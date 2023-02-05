/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    
    if(root === null)
        return null
    
    let cur = root
    let next = root.left
    
    while(next !== null) {
        cur.left.next = cur.right

        if(cur.next !== null) {
            cur.right.next = cur.next.left
            cur = cur.next
        }
        else {
            cur = next
            next = cur.left
        }
    }
    return root
};