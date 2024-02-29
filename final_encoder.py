alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from artEncoder import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

from artEncoder import logo
print(logo)
def badmoshi():
    new_string=""
    string_len=len(text)
    for i in text:
        if i==" ":
            continue
        org_pos=alphabet.index(i)
        if direction=="encode":
            new_pos=org_pos+shift
            if new_pos>len(alphabet):
                new_pos=new_pos-len(alphabet)
            new_string+=alphabet[new_pos]
        else:
            new_pos=org_pos-shift
            new_string+=alphabet[new_pos]
    print(new_string)
badmoshi()