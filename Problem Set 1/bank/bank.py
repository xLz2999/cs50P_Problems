greet = input("Greeting: ").lstrip().lower()
if greet[:5] == "hello" :
    print("$0")
elif greet[:1] == "h" :
    print("$20")
else :
    print("$100")
