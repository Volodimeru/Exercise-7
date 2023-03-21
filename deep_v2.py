#get variable from user
answer = input("What is the answer? ")
#different variants of 42 witt "or" removed whitestrips and converted lowercase.
if answer.strip() == "42" or answer.lower().strip() == "forty-two" or answer.lower().strip() == "Forty Two" or answer.lower().strip() == "forty two" :
    print("yes")
else :
    print("no")