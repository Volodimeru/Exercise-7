#get variable from user.
answer = input()
# different answers with match case statement.
match answer:
    case "42" | "Forty Two" | "forty two" | "forty-two" | "Forty-two" | "FORTY TWO" :
        print("yes")
    case _:
        print("no")