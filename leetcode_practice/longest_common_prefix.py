# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        min_length = min([len(s) for s in strs])
        modified_strs = [s[:min_length] for s in strs]
        prefix_list = []
        for i in range(min_length):
            prefix_list.append((list(set([s[: i + 1] for s in modified_strs])), 
                                len(list(set([s[: i + 1] for s in modified_strs])))))
        curated_prefix_list = [e[0][0] for e in prefix_list if e[1] == 1]
        if len(curated_prefix_list) == 0:
            return ''
        return  max(curated_prefix_list)