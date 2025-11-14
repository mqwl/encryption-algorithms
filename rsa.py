import random
import sympy


class RSACipher:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    @staticmethod
    def eea(a, b):
        old_c, c = 1, 0
        old_d, d = 0, 1
        while b != 0:
            res = a // b
            a, b = b, a - res * b
            old_c, c = c, old_c - res * c
            old_d, d = d, old_d - res * d
        return a, old_c, old_d
    @staticmethod
    def open_exp(e):
        while True:
            num = random.randint(1, e)
            if sympy.gcd(e, num) == 1:
                return num

    def generate_keys(self):
        randprime_1 = sympy.ntheory.generate.randprime(2 ** (1024 - 1), 2 ** 1024)
        randprime_2 = sympy.ntheory.generate.randprime(2 ** (1024 - 1), 2 ** 1024)
        rand_module = randprime_1 * randprime_2
        euler = (randprime_1 - 1) * (randprime_2 - 1)
        # open_exp = RSACipher.open_exp(euler)
        open_exp = 17
        gcd, x, y = RSACipher.eea(open_exp, euler)
        d = x + euler if x < 0 else x
        f = open('public.txt', 'w')
        f.write(str(rand_module) + '\n')
        f.write(str(open_exp) + '\n')
        f.close()
        f_priv = open('private.txt', 'w')
        f_priv.write(str(rand_module) + '\n')
        f_priv.write(str(d) + '\n')
        f_priv.close()
    
    def encrypt(self, text):
        f = open('public.txt', 'r')
        n = int(f.readline())
        e = int(f.readline())
        f.close()
        res = []
        for i in range(len(text)):
            res.append(str(ord(text[i])))
        res = ''.join(res)
        print(res)
        cipher = int(res) ** e % n
        return cipher
    
    def decrypt(self, text):
        f = open('private.txt', 'r')
        n = int(f.readline())
        d = int(f.readline())
        f.close()
        res = []
        for i in range(len(text)):
            res.append(str(ord(text[i])))
        res = ''.join(res)
        cipher = int(res) ** d % n
        return cipher


cipher_master = RSACipher()
#print(cipher_master.encrypt('welcome'))
cipher_master.generate_keys()
