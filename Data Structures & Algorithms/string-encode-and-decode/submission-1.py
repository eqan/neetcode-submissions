class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            if len(word) == 0:
                result += '#,'
                continue
            current_str = ''
            for s in word:
                ascii = ord(s)
                if ascii == 256:
                    current_str+=chr(0)
                else:
                    current_str+=chr(ascii+1)
            result+= '#,' + current_str
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        words = s.split("#,")
        for word in words:
            if len(word) == 0:
                result.append('')
                continue
            current_str = ''
            for s in word:
                ascii = ord(s)
                if ascii == 0:
                    current_str+=chr(256)
                else:
                    current_str+=chr(ascii-1)
            result.append(current_str)
        return result[1:]