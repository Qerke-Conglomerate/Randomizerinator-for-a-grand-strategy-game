while True:
    prompt1 = input('What do you want? ').lower()
    #The thing above, it asks for input. The thing below asks if the prompt equals "war" if it does it prints the list of 1 & 2.
    if prompt1 == 'war':
        import random
        list1 = [1, 2]
        print(random.choice(list1))
#checks if the thing is "reources" if it is again it chooses from the list of 1-10.
    elif prompt1 == 'resources':
        import random
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        print(random.choice(list2))
    elif prompt1 == 'resources amount':
        import random
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(random.choice(list2))
    elif prompt1 == 'combat':
        import random
        list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
        print(random.choice(list2))
    elif prompt1 == 'good stuff':
      print("what kind of stuff :winky:")
#asks it if it is not "war", "resources", "amount", or "combat" it prints "illegal action".
    else:
        print('Illegal action?')  #an answer that wouldn't be yes or no
