import random
import collections


def create_deck():

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    return deck

def get_hand(deck, num_cards):
    for _ in range(num_cards):
        random.shuffle(deck)
    hand = random.sample(deck, num_cards)
    return hand

def run():

    trys = int(input('how many times? '))

    deck = create_deck()

    high = 0
    one_pair = 0 
    two_pair = 0
    three_of_a_kind = 0
    full_house = 0
    four_of_a_kind = 0
    flush = 0
    straight = 0
    straight_flush = 0
    royal_flush = 0

    for _ in range(trys):

        print(f'{_}/{trys} \t {round((_/trys)*100,2)}%' , end='\r')

        hand = get_hand(deck, 5)
        values = []

        for card in hand:
            values.append(card[0])
        
        counter = dict(collections.Counter(values))


        if len(counter) == 5:

            hand_suits = []
            for card in hand:
                hand_suits.append(card[1])

            if len(set(hand_suits)) == 1:
                is_flush = True
            else:
                is_flush = False
            
            straight_counter = 0
            
            for i in range(len(values)):

                if values[i] == 'Ace':
                    if 2 in values:
                        straight_counter += 1
                elif values[i] == 'King':
                    if 'Ace' in values:
                        straight_counter += 1
                elif values[i] == 'Queen':
                    if 'King' in values:
                        straight_counter += 1
                elif values[i] == 'Jack':
                    if 'Queen' in values:
                        straight_counter += 1
                elif values[i] == '10':
                    if 'Jack' in values:
                        straight_counter += 1
                else:
                    next_value = int(values[i]) + 1
                    if str(next_value) in values:
                        straight_counter += 1
            
            if straight_counter == 4 and is_flush:
                if 10 in values and 'Jack' in values and 'Queen' in values and 'King' in values and 'Ace' in values:
                    royal_flush += 1
                else:
                    straight_flush += 1
            elif is_flush:
                flush += 1
            elif straight_counter == 4:
                straight += 1
            else:
                high += 1

        else:
            for value in counter.values():
                if value == 2 and len(counter) == 4:
                    one_pair += 1
                    break
                elif value == 2 and len(counter) == 3:
                    two_pair += 1
                    break
                elif value == 3 and len(counter) == 3:
                    three_of_a_kind += 1
                    break
                elif (value == 3 or value == 2) and len(counter) == 2:
                    full_house += 1
                    break
                elif value == 4 and len(counter) == 2:
                    four_of_a_kind += 1
                    break
                
            

        
    print(f'the probability of getting high card is {(high/trys)*100}%')
    print(f'the probability of getting one pair is {(one_pair/trys)*100}%')
    print(f'the probability of getting two pair is {(two_pair/trys)*100}%')
    print(f'the probability of getting three of a kind is {(three_of_a_kind/trys)*100}%')
    print(f'the probability of getting straight is {(straight/trys)*100}%')
    print(f'the probability of getting flush is {(flush/trys)*100}%')
    print(f'the probability of getting full house is {(full_house/trys)*100}%')
    print(f'the probability of getting four of a kind is {(four_of_a_kind/trys)*100}%')
    print(f'the probability of getting straight flush is {(straight_flush/trys)*100}%')
    print(f'the probability of getting royal flush is {(royal_flush/trys)*100}%')
    


if __name__ == "__main__":
    run()