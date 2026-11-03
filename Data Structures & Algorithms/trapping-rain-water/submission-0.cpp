

class Solution {
public:
    int trap(vector<int>& height) {
        int l=0;
        int r=l+1;
        int counter = 0;

        while (l < height.size() - 1) {
            bool found = false;
            while (r < height.size() ) {
                if (height[l] <= height[r]) {
                    int index = l+1;
                    while (index < r) {
                        counter += height[l] - height[index++];
                    }
                    l = r;
                    r++;
                    found = true;
                    break;
                }
                r++;
            }
            if (!found) l++;

        }
        r = height.size() - 1;
        l = r-1;

        while (r >= 0) {
            bool found = false;
            while (l >= 0 ) {
                if (height[r] < height[l]) {
                    int index = r-1;
                    while (index > l) {
                        counter += height[r] - height[index--];
                    }
                    r = l;
                    l--;
                    found = true;
                    break;
                }
                l--;
            }
            if (!found) r--;
        
        }

        return counter;

    }
};





