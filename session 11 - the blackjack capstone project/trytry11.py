# blackjack v.1
# from art import logo
# import random
#
# print(logo)
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card_user = []
# card_com = []
#
#
# def card_random(c):
#     c.append(random.choice(cards))
#
#
# card_user_sum = 0
# card_com_sum = 0
#
# start = input("do you want to play blackjack game? type 'y' or 'n': ")
# max = 21
# if start == 'y':
#     card_random(card_user)
#     card_random(card_user)
#     card_random(card_com)
#     want = True
#     while want:
#         for c in card_user:
#             card_user_sum += c
#             if card_user_sum > 21:
#                 print(f"your final hand: {card_user}, final score: {card_user_sum}")
#                 while card_com_sum < card_user_sum:
#                     card_random(card_com)
#                     for cc in card_com:
#                         card_com_sum += cc
#                 print(f"computer's final hand: {card_com}, final score: {card_com_sum}")
#                 if card_user_sum > card_com_sum:
#                     print("you win")
#                 else:
#                     print("you lose")
#                 want = False
#                 break
#
#         print(f"    your cards is {card_user}, current score: {card_user_sum} ")
#         print(f"    coumputer's first cards: {card_com}")
#         want = input(f"type 'y' to get another card, type 'n' to pass: ")
#         if want == 'y':
#             card_random(card_user)
#         else:
#             want = False
#
#     print(f"your final hand: {card_user}, final score: {card_user_sum}")
#     while card_com_sum < card_user_sum:
#         card_random(card_com)
#         for cc in card_com:
#             card_com_sum += cc
#     print(f"computer's final hand: {card_com}, final score: {card_com_sum}")
#     if card_user_sum < 22:
#         if card_user_sum > card_com_sum and card_com_sum < 22:
#             print("you win")
#     else:
#         print("you lose")


# black jack v1.1
# from art import logo
# import random
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# card_user = []
# card_com = []
# def card_random(c):
#     c.append(random.choice(cards))
#
# card_user_sum = 0
# card_com_sum = 0
# def card_sum(c, c_sum):
#     for i in c:
#         c_sum += i
#     return c_sum
#
# start = input("do you want to play blackjack game? type 'y' or 'n': ")
#
# def start_play():
#     print(logo)
#     card_random(card_user)
#     card_random(card_user)
#     card_random(card_com)
#     card_random(card_com)
#     print(f"    your card: {card_user}, current score: {card_sum(card_user, card_user_sum)}")
#     print(f"    computer's first card: {card_com}")
#
# def want_again():
#     repeat = True
#     while repeat:
#         want = input("type 'y' to get another card, or 'n' to pass: ")
#         if want == 'y':
#             card_random(card_user)
#             print(f"    your card: {card_user}, current score: {card_sum(card_user, card_user_sum)}")
#             print(f"    computer's first card: {card_com[0]}")
#             if card_user_sum > 21:
#                 repeat = False
#         else:
#             repeat = False
# def compare(card_c_s, card_u_s):
#     if card_u_s < 22 and card_u_s > card_c_s:
#         print('you win')
#     else:
#         print('you lose')
#
# if start == 'y':
#     start_play()
#
# want_again()
# compare(card_com_sum, card_user_sum)
