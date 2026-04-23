import random



def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(seznam):
    novy_seznam = seznam.copy()




    for hodnota in range(len(novy_seznam)):
        nejmensi_id = hodnota
        nejmensi = novy_seznam[hodnota]


        for i in range(hodnota+1,len(novy_seznam)):
            if novy_seznam[i] < nejmensi:
                nejmensi = novy_seznam[i]
                nejmensi_id = i

        novy_seznam[hodnota], novy_seznam[nejmensi_id] = novy_seznam[nejmensi_id], novy_seznam[hodnota]
    return novy_seznam

if __name__ == "__main__":

    small = random_numbers(5, low=0, high=20)
    print(small)
    sort = selection_sort(small)
    print(sort)