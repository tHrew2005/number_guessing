#Ko es atkārtoju? :

#1 citu bibliotēku importi un izmantosana
#2 Loops(while)
#3 If/elif/else kontrukcija
#4 sintakse
#5 nedaudz sarakstus ([])


import random
from time import process_time_ns


computer_guessed_number = random.randint(1,100)
continue_game = True
user_guesses = []
start_time = time.time()



while(continue_game):

    user_guess = int(input("uzmini skaitli starp 1 un 100: "))
    user_guesses.append(user_guess)

    if user_guess == computer_guessed_number:
        print('you win!')
        continue_game = False

    elif user_guess <= computer_guessed_number:
        print('vairāk')

    elif user_guess >= computer_guessed_number:
        print('mazāk')

    else:
        print('notika kļūda')


#uzdevums:aprekinat videjo
sum_of_difference = 0
for n in user_guesses:
    sum_of_difference += abs(n-computer_guessed_number)
ave_of_difference = sum_of_difference/len(user_guesses)
print(f"Vidējā starpība bija {ave_of_difference}")

#laiks
print("Tu spēlēji %s sekundes" % (time.time() - start_time))
