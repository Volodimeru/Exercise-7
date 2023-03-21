#get input from user
answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
if answer == "42":
    print("yes")
elif answer.lower() == "forty-two":
    print("yes")
elif answer.lower() == "forty two":
    print("yes")
else:
    print("No")