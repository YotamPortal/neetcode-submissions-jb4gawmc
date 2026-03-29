class Solution:
    sep = "#"
    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            s_len = len(s)
            encode_str += str(s_len) + self.sep + s
        
        print(encode_str)
        return encode_str
    
    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != self.sep:
                j += 1
            
            s_len = int(s[i:j])
            word = s[j + 1 : j + 1 + s_len]
            decode_list.append(word)

            i = j + 1 + s_len

        print(decode_list)
        return decode_list
