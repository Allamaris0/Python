import random

choice = None
filmy2 = []
while choice != "0":

    print(
        """
         * Dodaj film
         * Wpisz 1, aby losować filmy z podanej listy
         * Wpisz 0, żeby zakończyć
        """
    )

    choice = input("")
    print()

    # wyjdź
    if choice == "0":
        print("             Żegnaj \\ Goodbye")
        quit()

    # losowanie
    elif choice == "1":
        winner2 = random.choice(filmy2)
        print("Dzisiaj oglądamy " + winner2)
        

    # dodawanie filmów
    else:
        filmy2.append(choice)
        for f in filmy2:
            print("Dodałeś ", f)



