class VigenereCipher:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
   
    def process_text(self, text, key, to_encrypt):
        res = []
        ab = self.alphabet
        ab_len = len(ab)
        for i in range(len(text)):
            if (text[i].isalpha()):
                temp = text[i].lower()
                text_index = ab.find(temp)
                key_index = ab.find(key[i % len(key)])
                oper = 1 if to_encrypt else -1
                elem = ab[(text_index + oper * key_index) % ab_len]
                if text[i].isupper():
                    elem = elem.upper()
                res.append(elem)
            else:
                res.append(text[i])
        return ''.join(res)


cipher_master = VigenereCipher()
print(cipher_master.process_text(
    text='Доказательство оставим в качестве упражнения читателю',
    key='олег',
    to_encrypt=True
))
print(cipher_master.process_text(
    text='Тъпгцлчзъзцхръ саюеечш е цеъуэчеу штяллрущнв гнхоюйом',
    key='олег',
    to_encrypt=False
))
