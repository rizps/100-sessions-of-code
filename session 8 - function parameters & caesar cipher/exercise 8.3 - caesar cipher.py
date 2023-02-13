# caesar cipher program
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").replace(" ", "")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def d_encrypt(text_to_convert, shift_amount):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     d_encode = []
#     text_after = ''
#     if direction == 'encode':
#         for i in text:
#           if i in alphabet:
#             alp_shift = alphabet.index(i) + shift
#             if alp_shift >= 26:
#               alp_shift -= 26
#             i = alphabet[alp_shift]
#           d_encode.append(i)
#     elif direction == 'decode':
#         for i in text:
#             if i in alphabet:
#               alp_shift = alphabet.index(i) - shift
#               if alp_shift <= -1:
#                   alp_shift += 26
#               i = alphabet[alp_shift]
#             d_encode.append(i)
#     for i in d_encode:
#       text_after += i
#     if direction == 'encode':
#       print(f'the encoded text of "{text}" with {shift} shift to the right is "{text_after}"')
#     elif direction == 'decode':
#       print(f'the decoded text of "{text}" with {shift} shift is "{text_after}"')

    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛 # 5 shift -> hnanqnefynts

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# d_encrypt(text_to_convert=text, shift_amount=shift)


# other way
alphabet2 = alphabet*2  # double the amount of alphabet to simply the code, cause we should'nt use if statement
def cipher(start_text, shift_amount, cipher_direction):
    shift_direction = 'right'
    text_after = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
        shift_direction = 'left'
    for i in start_text:
        if i in alphabet2:
            alp_shift = alphabet2.index(i) + shift_amount
            i = alphabet2[alp_shift]
        text_after += i

    print(f'the {cipher_direction}d text of "{text}" with {shift} shift to the {shift_direction} is "{text_after}"')

cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

