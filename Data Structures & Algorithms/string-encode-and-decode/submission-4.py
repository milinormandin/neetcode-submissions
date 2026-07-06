class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        encoded = []
        for s in strs:
            chars = []
            if len(s) > 1:
                for c in s:
                    chars.append(str(ord(c)))
                chars = '%'.join(chars)
                encoded.append(chars)
            elif len(s) == 1:
                encoded.append(str(ord(s)))
            else:
                encoded.append('&')
        return '*'.join(encoded)


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        encoded = s.split('*')
        decoded = []
        
        for e_word in encoded:
            chars = []
            # check for char delimiter
            if '%' in e_word:
                chars = e_word.split('%')
                decoded.append(''.join([chr(int(c)) for c in chars]))
            # check for empty sring delimeter
            elif '&' in e_word:
                decoded.append("")
            else:
                decoded.append(chr(int(e_word)))
        return decoded



