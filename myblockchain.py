import hashlib
import os, binascii
k = False

while  k == False:
    nonce = binascii.b2a_hex(os.urandom(20))
    sha = hashlib.sha256(str(nonce).encode()).hexdigest()

    c = [n for n in sha]
    print(c)
    if (((c[0]) == '0') and ((c[1]) == '0') and ((c[2]) == '0') and ((c[3]) == '0')):
        k = True
    else:
        k = False
print("this is it", c)