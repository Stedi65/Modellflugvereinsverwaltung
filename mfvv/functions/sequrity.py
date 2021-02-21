from passlib.context import CryptContext
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


def generate_sk():
    key = RSA.generate(16384)
    with open("secret_key.pem", "wb") as f_out:
        f_out.write(key.export_key(format='PEM'))
    return key

def import_key(file_name):
    with open(file_name, 'rb') as f_in:
        key = RSA.import_key(f_in.read())
    return key

def generate_pk(sk):
    pk = sk.publickey()
    with open("public_key.pem", "wb") as f_out:
        f_out.write(pk.export_key(format='PEM'))
    return pk

def encrypt(pk_receiver, message):
    cipher = PKCS1_OAEP.new(pk_receiver)
    c = cipher.encrypt(message)
    return c

def decrypt(sk, c):
    cipher = PKCS1_OAEP.new(sk)
    m = cipher.decrypt(c)
    return m

def footprint(pk):
    hasher = SHA256.new(pk)
    return hasher.digest()

#key = generate_sk()
key = import_key('secret_key.pem')
pk = generate_pk(key)
c = encrypt(pk, b"Hallo Welt")
print(c)
m = decrypt(key, c)
print(m)
print(footprint(pk.export_key(format='PEM')))