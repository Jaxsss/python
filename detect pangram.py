# calculator to drink at least 1 glass of water not to be hungover

import re
def hydrate(drink_string):
    numbers = re.findall(r'\d+', str(drink_string))
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    all = sum(numbers)
    if all == 1:
        return (str(all) + ' glass of water')
    else:
        return (str(all) + ' glasses of water')


