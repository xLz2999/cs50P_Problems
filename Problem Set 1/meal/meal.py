def main() :
    yourtime = input("What time is it? ")
    abs_time = convert(yourtime)
    if 7 <= abs_time <= 8 :
        print("breakfast time")
    elif 12 <= abs_time <= 13 :
        print("lunch time")
    elif 18 <= abs_time <= 19 :
        print("dinner time")

def convert(x) :
    return int(x.split(":")[0]) + float(x.split(":")[1])/60

if __name__ == "__main__" :
    main()

