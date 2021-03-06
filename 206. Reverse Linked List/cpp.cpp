1.Iterative
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        while(head) {
            ListNode* curr = head;
            head = head->next;
            curr->next = prev;
            prev = curr;
        }
        return prev;
    }
};

2.Recursive
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
       return reverse(head, NULL); 
    }
private:
    ListNode* reverse(ListNode* node, ListNode* prev) {
        if (node == NULL) return prev;
        ListNode* next = node->next;
        node->next = prev;
        return reverse(next, node);
    }
};