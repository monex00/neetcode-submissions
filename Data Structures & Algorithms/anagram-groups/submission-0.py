class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # naive solution: sort the string use it as key save in value all the strings thas sorted matches with the key

        table = {}
        res = []
        for i, s in enumerate(strs):
            sorted_str = ''.join(sorted(s))
            if sorted_str in table:
                table[sorted_str].append(s)
            else:
                table[sorted_str] = [s]

        for key in table:
            res.append(table[key])

        return res