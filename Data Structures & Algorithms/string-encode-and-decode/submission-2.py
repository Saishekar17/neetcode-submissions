class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # find '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])  # get length
            word = s[j+1:j+1+length]  # get word

            res.append(word)
            i = j + 1 + length  # move pointer

        return res
