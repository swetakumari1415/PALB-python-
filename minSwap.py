class Solution {
  public:
    int minSwap(vector<int>& arr, int k) {
        int n = arr.size();

        // Find the count of elements which are less than or equal to k
        int count = 0;
        for (int i = 0; i < n; ++i)
            if (arr[i] <= k)
                ++count;

        // Find the unwanted elements in the current window of size 'count'
        int bad = 0;
        for (int i = 0; i < count; ++i)
            if (arr[i] > k)
                ++bad;

        // Initialize answer with 'bad' value of the current window
        int ans = bad;
        for (int i = 0, j = count; j < n; ++i, ++j) {

            // Decrement count of previous window
            if (arr[i] > k)
                --bad;

            // Increment count of current window
            if (arr[j] > k)
                ++bad;

            // Update answer if 'bad' is less in the current window
            ans = min(ans, bad);
        }
        return ans;
    }
};
