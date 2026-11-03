class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        priority_queue<int>q;
        for (int n : nums) q.push(n);
        int mx = 1;
        int counter = 1;
        int number = q.top();
        //cout << q.top() << endl;
        q.pop();
        while (!q.empty()) {
            //cout << q.top() << endl;
            if (q.top() == number) {
                q.pop();
                continue;
            }
           if(q.top() + 1 == number) {
               counter++;
               number = q.top();
               //cout << "Inside" << endl;
           }
           else {
               mx = max (mx, counter);
               number = q.top();
               counter = 1;
           }
            q.pop();
        }
        mx = max(mx, counter);
        return mx;

    }
};

