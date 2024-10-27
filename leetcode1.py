class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        l_str = [i for i in s]
        alpha =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ab']
        for i in range(t):
            for i in range(len(s)):
                if l_str[i] == 'z':
                    l_str[i] = 'ab'
                else:
                    index = alpha.index(l_str[i])
                    l_str[i] = alpha[index+1]
        return len(''.join(l_str))