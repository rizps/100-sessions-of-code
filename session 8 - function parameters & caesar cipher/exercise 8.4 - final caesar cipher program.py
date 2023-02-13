# caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet2 = alphabet*2
# update the feature
def cipher2():
    repeat = True
    while repeat:
        shift_direction = 'right'
        text_after = ''
        cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").replace(" ", "").lower()
        if cipher_direction != 'encode' and cipher_direction != 'decode':  # to deal with incorrect input
            print('you better type the right word')
            continue  # continue back to the while loop
        start_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))
        shift_amount %= 26  # to deal with too much shift amount
        if cipher_direction == 'decode':
            shift_amount *= -1
            shift_direction = 'left'
        for i in start_text:
            if i in alphabet2:
                alp_shift = alphabet2.index(i) + shift_amount
                i = alphabet2[alp_shift]
            text_after += i

        print(f'the {cipher_direction}d text of "{start_text}" with {abs(shift_amount)} shift to the {shift_direction} is "{text_after}"')
        repeat_again = True
        while repeat_again:  # very perfectionis, make while in a while for yes or no :'
            again = input("type 'yes' if you want to go again. otherwise type 'no': ").replace(" ", "").lower()
            if again != 'yes' and again != 'no':
                print('you better type the right answer')
                continue
            repeat_again = False
            if again == 'no':
                repeat = False  # to stop the while loop
                print('goodbye')

cipher2()