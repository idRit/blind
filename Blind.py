#pishorikhuzaima@gmail.com
import time
from LD import levenshtein_ratio_and_distance

list_of_dialogues = [
    "",
    ""
]

list_of_movies = [
    "CAPTAIN AMERICA CIVIL WAR",
    "JUMANJI WELCOME TO THE JUNGLE",
    "AVENGERS AGE OF ULTRON",
    "ZINDAGI NA MILEGI DOBARA",
    "YEH JAWANI HAI DEEWANI",
    "SPIDER MAN FAR FROM HOME",
    "THE DARK KNIGHT RISES",
    "MISSION IMPOSSIBLE FALL OUT",
    "DILWALE DULHANIA LE JAYENGE",
    "YAMLA PAGLA DEEWANA PHIR SE"
]

def movies_func(input_guess):

    # first = time.time()
    # input_guess = input('enter movie\n')
    # second = time.time() - first

    accuracies = []

    for i in list_of_movies:
        accuracies.append(levenshtein_ratio_and_distance(i, input_guess, ratio_calc=True))

    flag = False

    for i in accuracies:
        if i > 0.4:
            # print(second)
            # return(second)
            flag = True
            return i

    if not flag:
        print("nope")
        return "nope"