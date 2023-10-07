def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        print(string[i])
        if string[i] in vowels:
            kevin_score += length - i
            print("kevin : ",kevin_score)

            
        else:
            stuart_score += length - i
            print("sturat : ",stuart_score)
        print("----------------------------------------------")

        
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)