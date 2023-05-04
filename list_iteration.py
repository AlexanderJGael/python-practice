import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

counter = 1
for name in order_of_succession:
    print(f'{counter}. {name}')
    counter += 1
