class Solution:

    def encode(self, strs: List[str]) -> str:
        
        wordList = []
        for word in strs:
            encWord = []
            for let in word:
                encWord.append(chr(ord(let) + 1))
            temp = "".join(encWord)
            wordList.append(temp)
            wordList.append(" ")
        encoded_string = "".join(wordList)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        wordList = []
        enc = []
        for let in s:
            
            if( let != " "):
                enc.append(chr(ord(let) - 1))
            else:
                temp = "".join(enc)
                wordList.append(temp)
                enc.clear()
        return wordList



