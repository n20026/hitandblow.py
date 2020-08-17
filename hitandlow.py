from random import randint


def hinting(correct, guess):
    def conv(condition): return ['B', 'H'][condition]
    result = [conv(e == correct[i])
              if e in correct else 'X' for i, e in enumerate(guess)]
    return ''.join(result)


answer = f'{randint(0, 9999):0=4}'

for remain in range(10, 0, -1):
    print(f'chance remain {remain} times')
    if answer == (guess := input('type 4 digit number:')):
        break
    print(hinting(answer, guess))


print(f'correct is {answer}')
