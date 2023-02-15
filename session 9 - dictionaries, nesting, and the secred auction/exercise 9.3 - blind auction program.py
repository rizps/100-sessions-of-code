from art import logo
print(logo)


def blind_auction():
  bids = {}
  biggest = 0
  biggest_str = ''
  repeat = True
  while repeat:
    repeat_again = True
    name = input('what is your name? ')
    bid = int(input('how many your bid? $'))
    bids[name] = bid
    while repeat_again:
      repeat = input('anyone want to bid again? yes or no? ').replace(" ", '').lower()
      if repeat == 'no':
        repeat = False
      elif repeat == 'yes':
        repeat = True
      else:
        print('you better type the right word!')
        continue
      repeat_again = False
  # print(bids)
  for i in bids:
    if bids[i] > biggest:
      biggest_str = i
  print(f"the winner is {biggest_str} with ${bids[biggest_str]}")

# blind_auction()

# other way
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    continue