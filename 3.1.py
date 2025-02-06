string = input('Введите текст: ')
n = int(input('Введите число: '))
def main():

    words = string.split(': ')

    filter = [
        word.capitalize()
        for word in words
        if len(word) > n and len(word) % n != 0
]

    output_string = ', '.join(filter)
    print(output_string)
main()

