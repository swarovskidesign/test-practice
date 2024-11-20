import json

class Solution:

    def encrypt_char(self, char):
        char = char.lower()
        if char == 'j':
            char = 'i'
        row = (ord(char) - ord('a')) // 5 + 1
        col = (ord(char) - ord('a')) % 5 + 1
        return f"{row}{col}"

    def decrypt_pair(self, pair):
        row, col = int(pair[0]), int(pair[1])
        char_code = ord('a') + (row - 1) * 5 + (col - 1)
        char = chr(char_code)
        if char == 'i' and pair == '24':
            return 'i/j'
        return char

    def encrypt(self, text):
        encrypted_text = ''.join([self.encrypt_char(char) for char in text])
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ''.join([self.decrypt_pair(encrypted_text[i:i+2]) for i in range(0, len(encrypted_text), 2)])
        return decrypted_text

if __name__ == '__main__':
    sol = Solution()
    text = input('txt for encrypto ')
    encrypted_text = sol.encrypt(text)
    print(f'encrypto txt -  {encrypted_text}')

    with open('crypto.json', 'w') as file:
        json.dump({'encrypted_text': encrypted_text}, file)
    print('encrypto saved in file')

    with open("crypto.json", "r") as file:
        data = json.load(file)
        encrypted_text_from_file = data['encrypted_text']
        
    decrypted_text = sol.decrypt(encrypted_text_from_file)
    print('decrypto txt - ', decrypted_text)