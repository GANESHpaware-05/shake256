import hashlib as hsl
from pyscript import document

def shake256_converter(event):      
    pwd = document.getElementById('shake_256_input').value
    key = hsl.shake_256(pwd.encode('utf-8'))
    # Specify the length of the hash value you want, e.g., 64 bytes
    raja = key.digest(32)
    print(raja.hex())
    output_div = document.getElementById('shake_256_output')
    output_div.innerText = raja.hex()
