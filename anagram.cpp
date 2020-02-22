vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    int n = A.size();
    vector<vector<int> > ans;
    map<string, vector<int>> mp;
    for (int i=0; i<n; i++) {
        string org = A[i];
        sort(org.begin(), org.end());
        mp[org].push_back(i);
    }
    int i = 0;
    for (auto it=mp.begin(); it != mp.end(); it++) {
        vector<int> x;
        for (auto temp = (it->second).begin(); temp != (it->second).end(); temp++) {
            x.push_back((*temp) + 1);
            // cout<<(*temp)+1<<" "; 
        }
        ans.push_back(x);
    }
    return ans;
}
