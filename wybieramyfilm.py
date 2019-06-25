"""Program tworzy listę z pobranych od użytkownika nazw. Po wpisaniu "1" program losuje jeden z elementów listy.
Po wpisaniu "2" użytkownik może podać, który element chce usunąć z listy.
Po wpisaniu "0" następuje zakończenie programu."""

import random

choice = None
filmy2 = []
while choice != "0":

    print(
        """
         * Wpisz 1, aby losować filmy z listy
         * Wpisz 2, aby usunąc film z listy
         * Wpisz 0, żeby zakończyć
         
         Wpisz film, który chcesz dodać:
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
        try:
            winner2 = random.choice(filmy2)
            print("Dzisiaj oglądamy " + winner2)
        except IndexError:
            print("Niestety, ale lista jest na razie pusta")
    
    # usuwanie
    elif choice =="2":
        print("Aktualna lista: ", filmy2)
        x=(input("wprowadź film, który chcesz usunąć "))
        if x in filmy2:
            filmy2.remove(x)
        else:
            print("\nNie ma takiego filmu na liście")
            
        print(filmy2)
        
    # dodawanie filmów
    else:
        filmy2.append(choice)
        for f in filmy2:
            print("Dodałeś ", f)




