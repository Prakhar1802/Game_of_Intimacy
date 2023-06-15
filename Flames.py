# print("############## ##           #############  ####       ####  ###########  ############  ")
# print("##             ##           ##         ##  ## ##    ##  ##  ##           ##            ")
# print("##             ##           ##         ##  ##   ####    ##  ##           ##            ")
# print("#########      ##           #############  ##    #      ##  ########     ############  ")
# print("##             ##           ##         ##  ##           ##  ##                     ##  ")
# print("##             ##           ##         ##  ##           ##  ##                     ##  ")
# print("##             ############ ##         ##  ##           ##  ###########  ############  ")
#
# print("\n\nWelcome to the game of love, let's find the relationship with your closer ones by FLAMES\n")


def Flame_fun(name1, name2):
    # code for taking the input by the user

    # n1 = str(input("Enter the first name:")).lower()
    # n2 = str(input("Enter the second name:")).lower()
    n1 = str(name1).lower()
    n2 = str(name2).lower()

    n1 = n1.replace(" ", "")
    n2 = n2.replace(" ", "")

    # code for finding the common character and make it cancel

    for i in n1:
        for j in n2:
            if i == j:
                n1 = n1.replace(i, "", 1)
                n2 = n2.replace(j, "", 1)
                break

    # code for count the number

    count = len(n1 + n2)

    # code for finding the relationship

    if count > 0:
        l1 = ["Friends", "Lover", "Affectionate", "Marriage", "Enemies", "Siblings"]
        while len(l1) > 1:
            c = count % len(l1)
            s_index = c - 1
            if s_index >= 0:
                left = l1[:s_index]
                right = l1[s_index + 1:]
                l1 = right + left
            else:
                l1 = l1[:len(l1) - 1]
        return l1[0]
    else:
        return "sorry i am not able to calculate it Please try again"
