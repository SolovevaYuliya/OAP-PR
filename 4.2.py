n1 = input("Введите первую строку: ")
n2 = input("Введите вторую строку: ")
n3 = input("Введите третью строку: ")
def main():

    set1 = set(map(int, n1.split(', ')))
    set2 = set(map(int, n2.split(', ')))
    set3 = set(map(int, n3.split(', ')))

    peresechenie = set1.intersection(set2).intersection(set3)

    if peresechenie:
        list_num = sorted(peresechenie)
        print(" ".join(map(str, list_num)))
        print(max(list_num))
    else:
        print("Нет общих чисел")

main()