import sympy


class RSACipher:

    @staticmethod
    def open_key(euler):
        for i in range(3, euler, 2):
            candidate = sympy.gcd(i, euler)
            if candidate == 1:
                return i

    def generate_keys(self):
        randprime_1 = sympy.randprime(2 ** (20 - 1), 2 ** 20)
        randprime_2 = sympy.randprime(2 ** (20 - 1), 2 ** 20)
        n = randprime_1 * randprime_2
        euler = (randprime_1 - 1) * (randprime_2 - 1)
        e = RSACipher.open_key(euler)
        d = sympy.mod_inverse(e, euler)
        
        f = open('public.txt', 'w')
        f.write(str(n) + '\n')
        f.write(str(e) + '\n')
        f.close()

        f = open('private.txt', 'w')
        f.write(str(n) + '\n')
        f.write(str(d) + '\n')
        f.close()

    def encrypt(self, text):
        f = open('public.txt', 'r')
        n = int(f.readline())
        e = int(f.readline())
        f.close()
        return pow(text, e, n)

    def decrypt(self, text):
        f = open('private.txt', 'r')
        n = int(f.readline())
        d = int(f.readline())
        f.close()
        return pow(text, d, n)


cipher_master = RSACipher()
cipher_master.generate_keys()
message = 1000000
print(message)
encrypt = cipher_master.encrypt(message)
print(encrypt)
decrypt = cipher_master.decrypt(encrypt)
print(decrypt)
