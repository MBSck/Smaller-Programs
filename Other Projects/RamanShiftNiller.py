def print_to_file():

    in1,in2 = 0, 0

    while in1 != "stop":
        in1 = float(input("Enter the right hand side mode: "))
        in2 = float(input("Enter the left hand side mode: "))

        print("The result is ", (in1 - in2)/2)

        in_str = input("Do you want to print to file? y/n ")
        if in_str == "y":
            with open("Raman_correction.txt", "w+") as f:
                angle = input("Please input the angle: ")
                f.write("\n" + angle + ": " + str((in1 - in2)/2) + "\n")


if __name__ == "__main__":
    print_to_file()