class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" +  string
            # print(s)
        return s


    def decode(self, s: str) -> List[str]:
        l, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i: j])
            word = s[j + 1 : j + 1 + length]
            l.append(word)

            i = j + 1 + length

        return l

        
    

# for c in s:
#     # print(c)
#     if c.isdigit() and word != "":
#         l.append(word)
#         # print(l)
#         word = ""
#     else:
#         word += c




