class CaesarCipher:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, to_encrypt):
        res = []
        for i in range(0, len(text)):
            if (text[i].isalpha()):
                temp = text[i].lower()
                index = self.alphabet.find(temp)
                oper = 1 if to_encrypt else -1
                elem = self.alphabet[(index + oper * shift) % 33]
                if text[i].isupper():
                    elem = elem.upper()
                res.append(elem)
            else:
                res.append(text[i])
        return ''.join(res)


cipher_master = CaesarCipher()
print(cipher_master.process_text(
    text='Доказательство оставим в качестве упражнения читателю',
    shift=2,
    to_encrypt=True
))
print(cipher_master.process_text(
    text='Ёрмвйвфжнюуфдр руфвдко д мвщжуфдж хствипжпкб щкфвфжна',
    shift=2,
    to_encrypt=False
))
