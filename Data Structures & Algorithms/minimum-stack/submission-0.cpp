class MinStack {
    vector<int>v;
public:
    MinStack() {

    }

    void push(int val) {
        v.push_back(val);
    }

    void pop() {
        if (!v.empty()) {
            v.pop_back();
        }
    }

    int top() {
        return v.back();
    }

    int getMin() {
        int min = v.front();
        for (int i = 1; i < v.size(); i++) {
            min = min < v[i] ? min : v[i];
        }
        return min;
    }
};