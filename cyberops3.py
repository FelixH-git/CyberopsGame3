import math


class Solver():
    def __init__(self, cipher: str):
        self.cipher = cipher
        
    def decrypt_ceasar(self,text_encrypted:str, key: int, alpha_len=26) -> str:
        res = ""
        for i in range(len(text_encrypted)):
            char = text_encrypted[i]
            res += chr((ord(char) + (alpha_len-key)-65) % 26 + 65)   

        return res
    
    def split_two(self, key: int) -> tuple:
        h2 = self.cipher[len(self.cipher)//2:]
        h1 = self.cipher[:len(self.cipher)//2]

        h1 = self.decrypt_ceasar(h1, key)
        h2 = self.decrypt_ceasar(h2, key)
        
        return h1, h2
          
    def decrypt_transition(self,text_encrypted: str, key: int) -> str:
        res = [""]*len(text_encrypted)
        key_str = str(key)
        for letterpos in range(len(text_encrypted)):     
            res[int(key_str[letterpos]) - 1] = text_encrypted[letterpos]
        
        res_str = ""
        for i in res:
            res_str += i
        
        return res_str
                         


if __name__ == "__main__":
    t = Solver("DUALVHYARW")
    
    X = t.split_two(7)
    
    print(t.decrypt_transition(X[0], 41325))
    print(t.decrypt_transition(X[1], 41325))
