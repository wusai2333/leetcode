1.Iterative
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while(head != null) {
            ListNode curr = head;
            head = head.next;
            curr.next = prev;
            prev =curr;
        }
        return prev;
    }
}

2.Recursive
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        return reverse(head, null);
    }
    
    private ListNode reverse(ListNode node, ListNode prev) {
        if(node == null) return prev;
        ListNode next = node.next;
        node.next = prev;
        return reverse(next, node);
    }
}