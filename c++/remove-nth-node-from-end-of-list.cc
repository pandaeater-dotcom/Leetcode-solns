/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr)
            return nullptr;
        ListNode* temp = head;
        ListNode* tempEnd = head;
        for (int i = 0; i < n; i++)
            tempEnd = tempEnd->next;
        if (tempEnd == nullptr)
            return head->next;
        while (tempEnd->next != nullptr)
        {
            tempEnd = tempEnd->next;
            temp = temp->next;
        }
        temp->next = temp->next->next;
        return head;
    }
};
