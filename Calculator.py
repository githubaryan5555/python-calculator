from datetime import datetime

results = []  # Initialize an empty list to store previous results

while True:
    print('What do you want to do?:')
    print('1: Addition')
    print('2: Subtraction')
    print('3: Multiplication')
    print('4: Division')
    print('5: Print previous results')
    print('6: Save previous results to a text file')
    print('Type the number')
    choice = input()

    if choice == "1":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) + int(b)
        print("The sum of", a, "and", b, "is", c)
        results.append("The sum of {} and {} is {}".format(a, b, c))

    elif choice == "2":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) - int(b)
        print("The difference of", a, "and", b, "is", c)
        results.append("The difference of {} and {} is {}".format(a, b, c))

    elif choice == "3":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) * int(b)
        print("The product of", a, "and", b, "is", c)
        results.append("The product of {} and {} is {}".format(a, b, c))

    elif choice == "4":
        print('First number:')
        a = input()
        print('Second number:')
        b = input()
        c = int(a) / int(b)
        print("The division result of", a, "and", b, "is", c)
        results.append("The division result of {} and {} is {}".format(a, b, c))

    elif choice == "5":  # Print previous results
        print("Previous results:")
        for result in results:
            print(result)

    elif choice == "6":  # Save previous results to a text file with dynamically generated filename
        current_time = datetime.now().strftime("%I-%M-%S-%p")  # Format: hour-minute-second-AM/PM
        filename = "result{}.txt".format(current_time)

        with open(filename, "w") as file:
            file.write("Previous results:\n")
            for result in results:
                file.write(result + "\n")
        print("Results saved to", filename)

    else:
        print('Invalid operation')

    print("Do you want to continue? (y/n)")
    n = input()
    if n != "y":
        break
