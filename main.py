integers = ['2', '4', '7', '10']
liczby_parzyste = []
liczby_nieparzyste = []

def find_outlier(integers):
    for i in integers:
        i = int(i)
        if i % 2 == 0:
            liczby_parzyste.append(i)
        else:
            liczby_nieparzyste.append(i)
    if len(liczby_parzyste) > len(liczby_nieparzyste):
        print(liczby_nieparzyste)
    else:
        print(liczby_parzyste)

find_outlier(integers)
