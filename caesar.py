class CaesarCipher:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, to_encrypt):
        res = []
        for i in range(0, len(text)):
            if (text[i].isalpha()):
                temp = text[i].lower()
                index = self.alphabet.find(temp)
                if to_encrypt:
                    res.append(self.alphabet[(index + shift) % 33])
                else:
                    res.append(self.alphabet[(index - shift) % 33])
            else:
                res.append(text[i])
        return ''.join(res)


cipher_master = CaesarCipher()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    to_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    to_encrypt=False
))
