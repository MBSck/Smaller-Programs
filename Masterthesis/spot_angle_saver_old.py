import os.path
import datetime
import csv
import pandas

# Additions
# Think about getting all data of different samples into .csv or .json file and then print it out.
# Makes searching and updating easier as well as checking if angles are in dataset.

"""This program writes the number of the spots and then the angle information into a csv file.
Also simplifies the process and does some calculation so the data is easier to read.
Can also output a txt file if need be."""

path = input("Please enter path: ")

# Configures the paths that are to be used for saving, and the name of the .txt and .json file
file_txt = "Spot_Angles.txt"
file_csv = "Spot_Angle_data.csv"
file_path_csv = os.path.join(path, file_csv)
file_path_txt = os.path.join(path, file_txt)

# Global variables predefined for some functions
cond = True
spot_name_inp = []
angle_inp = 0.
measuring_error = 1
error = 1


class CSV:
    """The class that creates and updates the '.csv' file.
    Also performs some functions like recalculating the angles and checking which are still missing"""
    def __init__(self):
        self.sample, self.spots = "", [""]
        self.org_twist_angle, self.twist_angle = None, None
        self.error = None
        self.tr1_side_1, self.tr1_side_2, self.tr1_side_3 = None, None, None
        self.tr2_side_1, self.tr2_side_2, self.tr2_side_3 = None, None, None
        self.tr1_error, self.tr2_error = None, None

    def create_file(self, save_path):
        """Creates the file if it doesn't exist already"""
        if not os.path.isfile(save_path):
            with open(save_path, "w+") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["Sample", "Spots", "Original Twist Angle", "Twist Angle", "Error",
                                     "Tr1SideA_1", "Tr1SideA_2", "Tr1SideA_3", "Tr1SideError",
                                     "Tr2SideA_1", "Tr2SideA_2", "Tr2SideA_3", "Tr2SideError"])

    def format_angles(self, degree_range_end):
        """Formats the angles to they lie between 0 degrees and a certain degree input"""
        ...

    def check_needed_angles(self, save_path):
        """Checks all the angles and looks for angles still missing in sample series"""
        ...

    def update_file(self, save_path):
        """Updates the file with a new row"""
        with open(save_path, "a") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([self.sample, self.spots, self.org_twist_angle, self.twist_angle, self.error,
                                 self.tr1_side_1, self.tr1_side_2, self.tr1_side_3, self.tr1_error,
                                 self.tr2_side_1, self.tr2_side_2, self.tr2_side_3, self.tr2_error])

    def create_txt_file(self):
        """Creates a '.txt' file from the .csv data for easier readability"""
        ...



# Checks if file is already created in specified path and if not creates and initializes it
def create_file(save_path):
    """Creates a '.txt'  file and if it is already created reads out its data"""
    if not os.path.isfile(save_path):
        with open(save_path, "w+") as f:
            f.write(f"This file was created on {datetime.datetime.now()}, origin angle always at 0.\n")
            f.write("Convention for CVD is on upwards triangle (flat side on the bottom 0°),"
                    " 1:left side, 2:right side, 3:bottom side\n")
            f.close()

        data_already_saved = ""

    else:
        with open(save_path, "r") as f:
            data_already_saved = f.readlines()
            f.close()

    return data_already_saved


def get_counter(data):
    """This gets the latest sample number from the .txt file."""
    counter = 1
    # If no data has been specified in the document counter stays at 1
    if data == "":
        pass
    # If there is already data in the document, counter is being looked for
    else:
        data = data

        for line in data:
            data_copy = line.rsplit(" ")

            for word in data_copy:
                if "sample" in word:
                    if int(word[-1]) + 1 > counter:
                        counter = int(word[-1]) + 1

    return counter


def angle_reformat(angle_input):
    """This formats the angle so it is in an area between 0-60°,
    as after that the angles will have the same behaviour."""
    if ((type(angle_inp) != float) or (angle_inp > 360) or
            (angle_inp < 0)):
        raise ValueError("Angle is not in the right format")

    if (angle_input > 0) and (angle_input < 60):
        angle_zero_to_sixty = angle_input

    elif (angle_inp < 120) and (angle_inp > 60):
        angle_zero_to_sixty = 120 - angle_inp

    elif (angle_inp > 120) and (angle_inp < 180):
        angle_zero_to_sixty = angle_inp - 120

    elif (angle_inp < 240) and (angle_inp > 180):
        angle_zero_to_sixty = 240 - angle_inp

    elif (angle_inp > 240) and (angle_inp < 300):
        angle_zero_to_sixty = angle_inp - 240

    else:
        angle_zero_to_sixty = 360 - angle_inp

    return angle_zero_to_sixty


def check_needed_angles(angle_data):
    """This checks if the angles that are needed have been measured already and
    checks which angles are already measured and which still needed."""
    # Data of twist angle moiré paper for MoS2
    needed_angles_list = [0, 9, 12, 18, 27, 29, 36,
                          38, 41, 45, 49, 60]
    needed_angles_list_data = []
    angle_number_counter = 0

    print(angle_data)
    """
    # This checks if angles of data are in the list needed and takes some approx.
    for angle in angle_data:
        for angle_check in needed_angles_list:
            if (angle == angle_check) or (angle == angle_check + 1)\
                    or (angle == angle_check - 1):
                print(f"Angle {angle}")
                needed_angles_list_copy.pop(angle_number_counter)
                angle_number_counter += 1
    """
    if angle_number_counter == len(needed_angles_list):
        print("All angles needed for comparison have been measured")

    else:
        print(f"Angles that still need to be measured:\n{needed_angles_list_copy}")


def writing_loop(data, save_path):
    """This begins the writing and saves data to the document as well as formating it and quitting it."""
    global cond, spot_name_inp, angle_inp, error

    # Initializes the counter from saved data
    counter = get_counter(data)

    # Determines the sample name, if specific one is required (Gets skipped sometimes)
    sample_name = input("Enter sample name (leave empty for enumerate, enter with '_' as delimiter): ")

    # Gets the sample name to check, if it is CVD or not
    sample_name_read = sample_name.lower()
    sample_name_read = sample_name_read.rsplit("_")

    print("'Enter quit int the spot name to quit the program'")

    while cond:

        spot_name_inp = input("Enter all spot names of sample (separated by comma): ")

        # Checks if user wants to quit program
        if spot_name_inp == "quit":
            cond = False
            break

        # Checks if the name of the sample has cvd in it
        if "cvd" in sample_name_read:

            cond_triangle = True
            triangle_sides_1 = []
            triangle_sides_2 = []
            side = 0

            while cond_triangle:
                if side < 3:
                    side += 1
                    angles_of_sides_triangle_1 = float(
                        input(f"Enter the {side} side of the first triangle (angle): "))
                    triangle_sides_1.append(angles_of_sides_triangle_1)

                if (side >= 3) and (side < 6):
                    side += 1
                    angles_of_sides_triangle_2 = float(
                        input(f"Enter the {side-3} side of the second triangle (angle): "))
                    triangle_sides_2.append(angles_of_sides_triangle_2)

                if side >= 6:
                    error_triangle_1 = float(input("Enter the error of the first triangle: "))
                    error_triangle_2 = float(input("Enter the error of the seocnd triangle: "))
                    # Calculates the mean error
                    error_triangle = error_triangle_1 + error_triangle_2
                    error = error_triangle + measuring_error

                    cond_triangle = False
                    side = 0
                    continue

        angle_inp = float(input("Enter twist angle of sample (in degrees): "))
        angle_inp_unaltered = angle_inp

        # This returns angle in format 0-60°
        angle_inp_reformatted = angle_reformat(angle_inp)

        # Parses the spots in order to print them
        spot_name_inp = spot_name_inp.rsplit(",")

        # Writes data to file
        with open(save_path, "a") as f:
            if sample_name != "":
                f.write(f"\nThe sample_{sample_name}_{counter} has the spots:\nSpot {spot_name_inp[0]}")
            else:
                f.write(f"\nThe sample_{counter} has the spots:\nSpot {spot_name_inp[0]}")
            # For-loop to get all the spots
            for i in range(1, len(spot_name_inp)):
                f.write(f" & spot {spot_name_inp[i]}")

            if "cvd" in sample_name_read:
                f.write(f"\nWith the first triangle sides of ")
                for i in triangle_sides_1:
                    side += 1
                    f.write(f"{side}:{str(i)}° ")

                side = 0

                f.write(f"and the second triangle sides are ")
                for i in triangle_sides_2:
                    side += 1
                    f.write(f"{side}:{str(i)}° ")

                side = 0

            if angle_inp_unaltered == angle_inp_reformatted:
                f.write(f"\nThe twist angle is {angle_inp}° with an error of {error}%\n")

            else:
                f.write(f"\nThe twist angle is {angle_inp_reformatted}° with an error of {error}%"
                        f" (Original Angle: {angle_inp_unaltered}°)\n")

            f.close()

        print("Data confirmed!")
        counter += 1

csv_file = CSV()
csv_file.create_file(file_path_csv)

data_ang = create_file(file_path_txt)
# check_needed_angles(data_ang)
writing_loop(data_ang, file_path_txt)