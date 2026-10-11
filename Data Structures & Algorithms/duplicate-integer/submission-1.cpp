class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        
        std::unordered_map<int, int> counter_map;

        for(auto num : nums) {
            if (counter_map.contains(num)) {
                return true;
            }
            counter_map.insert({num, 1});
        }

        return false;
    }
};