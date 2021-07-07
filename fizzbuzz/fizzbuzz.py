def fizzbuzz(limit):
    rules = {
        'fizz': 3,
        'buzz': 5
    }
    for i in range(0, limit):
        output = ''
        for word, num in rules.items():
            output += word if i % num == 0 else ''
        print(output if output else i)


if __name__ == '__main__':
    fizzbuzz(100)
