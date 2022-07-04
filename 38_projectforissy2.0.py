def questions101():
    print("What do you think the safest option is?")
    safeone = input(" ")
    print("If you chose", safeone, "will you be satisfied, or will this little debate continue growing inside of you?(Response with 'satisfied' or 'not satisfied' if so)")
    plottwist = input(" ")
    #first use of dictionaries
    first = {"not satisfied":"What option then seems right to you?", "satisfied":"I think you should therefore chose that one!" }
    print(first[plottwist])
    #not working from here on out
    finalresponse = input(" ")
    print("Do you want to chose", finalresponse, "?(Answer with 'yes' or 'no')")
    chosing = input("")
    #second use of dictionaries
    idk = {"No":"Why?", "Yes":"Then I think we have made your decision", "idk":"Then you should probably chose the one you feel safest with"}
    print(idk[chosing])
    #not workin from here on out as well
    print("Why?")
    rant = input("")
    print("Then you should probably chose the one you feel safest with")

y = input("What decision is troubling you today?")
v = input("Number of options (max is 4)?")
if "4" in v:
    opt1 = input("Option 1: ")
    opt2 = input("Option 2: ")
    opt3 = input("Option 3: ")
    opt4 = input("Option 4: ")
    print("What will happen if you chose", opt1)
    reason1 = input(" ")
    print("How about", opt2)
    reason2 = input(" ")
    print(opt3, "?")
    reason3 = input(" ")
    print("Now", opt4)
    reason4 = input(" ")

elif "3" in v:
    opt1 = input("Option 1: ")
    opt2 = input("Option 2: ")
    opt3 = input("Option 3: ")
    print("What will happen if you chose", opt1)
    reason1 = input(" ")
    print("How about", opt2)
    reason2 = input(" ")
    print(opt3, "?")
    reason3 = input(" ")

elif "2" in v:
    opt1 = input("Option 1: ")
    opt2 = input("Option 2: ")
    print("What will happen if you chose", opt1)
    reason1 = input(" ")
    print("How about", opt2)
    reason2 = input(" ")


#if statements not making sense
questions101()
if "What option then seems right to you?" in u:
    riskyoption()
    if "Why?" in y:
        why(safeone)