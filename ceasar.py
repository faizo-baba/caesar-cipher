print ("""welcome to message encryption and decryption through ceasar cipher method """)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
]
direction = input("type encode for encryption, and decode for decryption\n")
text = input("enter the text\n")
shift = int(input("enter the number by you want shifting\n"))

def ceasar (orignal_text, shift_amount, encode_decode):
    output_text = ""
    for letter in orignal_text:

        if encode_decode == "decode" :
            shift_amount *= -1    
            
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

            # else :
            #     output_text += letter

    print(f"Here is the {encode_decode}d text: {output_text}")        

ceasar(orignal_text=text, shift_amount=shift, encode_decode=direction)        