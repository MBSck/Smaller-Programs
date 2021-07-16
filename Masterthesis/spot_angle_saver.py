import os.path
import csv
import pandas as pd
import math

__name__ = "__spotangle_saver__"

"""This program writes the number of the spots and then the angle information into a csv file.
Also simplifies the process and does some calculation so the data is easier to read.
Can also output a txt file if need be."""


class CSV:
    """The class that creates and updates the '.csv' file.
    Also performs some functions like recalculating the angles and checking which are still missing"""
    def __init__(self):
        """This initalizes the variables for the document and sets the condition for the while loop"""
        self.sample, self.spots = "", []
        self.org_twist_angle, self.twist_angle, self.error = None, None, None
        self.tr1_sides, self.tr2_sides = [], []
        self.tr1_error, self.tr2_error = None, None

        # Error from measuring by eye
        self.measuring_error = 1

        # Get path of file
        self.path = input("Please enter path: ")

        # Configure path of files
        self.file_csv, self.file_txt = "Spot_Angles.csv", "Spot_Angles.txt"
        self.file_path_csv, self.file_path_txt = os.path.join(self.path, self.file_csv), \
                                                 os.path.join(self.path, self.file_txt)

        # Creates the '.csv' file
        self.create_file(self.file_path_csv)

        # While loop condition
        self.cond = True

    def create_file(self, save_path):
        """Creates the file if it doesn't exist already"""
        if not os.path.isfile(save_path):
            with open(save_path, "w+") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["Sample", "Spots", "Original Twist Angle", "Twist Angle", "Error",
                                     "Triangle1Sides", "Triangle2Sides", "Triangle1SidesError", "Triangle2SidesError"])

    def enumerate_sample_names(self, save_path, sample_name):
        """This gets the name of the sample and counts up"""
        data = pd.read_csv(save_path)
        set_name = ""

        # Sets the name to sample if no name is given or checks if given name is already stored in data
        if sample_name == "":
            if data["Sample"].empty:
                set_name = "Sample_1"

            else:
                for declaration in data["Sample"]:
                    if "Sample" not in declaration:
                        set_name = "Sample_1"

                    else:
                        counter = int(declaration[-1]) + 1
                        if int(declaration[-1]) >= 9:
                            ...
                        else:
                            set_name = f"Sample_{counter}"

        else:
            if data["Sample"].empty:
                set_name = f"{sample_name}_1"

            else:
                for declaration in data["Sample"]:
                    if sample_name not in declaration:
                        set_name = f"{sample_name}_1"

                    else:
                        counter = int(declaration[-1]) + 1
                        set_name = f"{sample_name}_{counter}"

        return set_name

    def reformat_angles(self, angle_input, degree_range_end):
        """Formats the angles to they lie between 0 degrees and a certain degree input"""
        angle_steps = 360//degree_range_end
        angle_output = 0

        for step in range(0, angle_steps + 1, 2):
            if (angle_input >= step * degree_range_end) and (angle_input <= degree_range_end * (step + 1)):
                angle_output = angle_input - step * degree_range_end
                break

            if (angle_input <= degree_range_end * (step + 2)) and (angle_input >= degree_range_end * (step + 1)):
                angle_output = degree_range_end * (step + 2) - angle_input
                break

        return angle_output

    def reformat_light_sides(self, angle_input):
        """Reformats the sides of the triangle, so it is either above or below sixty"""
        if angle_input > 100:
            if angle_input == 120:
                angle_output = 60

            if angle_input > 120:
                overshoot = angle_input - 120
                angle_output = 60 - overshoot

            if angle_input < 120:
                overshoot = 120 - angle_input
                angle_output = 60 + overshoot

        else:
            angle_output = angle_input

        return round(angle_output)

    def check_needed_angles(self, save_path):
        """Checks all the angles and looks for angles still missing in sample series"""
        # Data of twist angle moiré paper for MoS2
        needed_angles_list = [0, 9, 12, 18, 27, 29, 36,
                              38, 41, 45, 49, 60]
        angles_still_needed = needed_angles_list
        angles_already_checked = []

        # Gets the '.csv' data with pandas
        data = pd.read_csv(save_path)

        # Adds the angles to the list and removes from the needed list
        for angle in data["Twist Angle"]:
            if (int(angle+1) in needed_angles_list) or (int(angle-1) in needed_angles_list)\
                    or (int(angle) in needed_angles_list):
                angles_already_checked.append(int(angle))

        angles_already_checked.sort()

        for angle in needed_angles_list:
            if (angle+1 in angles_already_checked) or (angle-1 in angles_already_checked)\
                    or (angle in angles_already_checked):
                angles_still_needed.remove(angle)

        print("Angles already measured: ")
        print(", ".join((str(x) for x in angles_already_checked)))
        print("Angles yet to craft/measure: ")
        print(", ".join(str(x) for x in needed_angles_list))

    def calculate_error(self, tr_side_list):
        """This function calculates the errors of each triangle side.
        It then adds the measure error and gives out the complete error"""
        mean, error = 0, 0

        for num in tr_side_list:
            mean += num

        mean = mean/len(tr_side_list)

        for i in tr_side_list:
            error += math.sqrt((i - mean)**2)

        error = error/len(tr_side_list)

        return round(error, 1)

    def update_file(self, save_path):
        """Updates the file with a new row"""
        with open(save_path, "a") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([self.sample, self.spots, self.org_twist_angle, self.twist_angle, self.error,
                                    self.tr1_sides, self.tr2_sides, self.tr1_error, self.tr2_error])

    def create_txt_file(self):
        """Creates a '.txt' file from the .csv data for easier readability"""
        ...

    def writing_loop(self):
        """This begins the writing and saves data to the document as well as formating it and quitting it."""
        # Sets variables for the CVD loop
        cond_triangle = False
        side = 0

        # Checks the documents for the needed angles
        self.check_needed_angles(self.file_path_csv)

        # Determines the sample name, if specific one is required (Gets skipped sometimes)
        sample_name = input("Enter sample name (leave empty for simple enumerate): ")

        # Sets the range of valid degrees
        degree_range = 60

        # Gets the sample name to check, if it is CVD or not
        sample_name_read = sample_name.lower()
        sample_name_read = sample_name_read.rsplit("_")

        # Checks if the name of the sample has cvd in it
        if "cvd" in sample_name_read:
            degree_range = int(input("Input the degree range end integer(e.g. from 0-60° input is '60'): "))

        print("'Enter quit in the spot name input to quit the program'")

        while self.cond:

            # Updates the writing information for the sample and numerates the sample name if it is already in the data
            self.sample = self.enumerate_sample_names(self.file_path_csv, sample_name)

            # Checks the spots that the user wants to input
            spot_name_inp = input("Enter all spot names of sample (separated by comma): ")

            # Checks if user wants to quit program
            if spot_name_inp == "quit":
                self.cond = False
                break

            if "cvd" in sample_name_read:
                if degree_range == 60:
                    cond_triangle = True
            else:
                self.tr1_sides, self.tr2_sides = None, None

            while cond_triangle:
                if side < 3:
                    side += 1
                    angles_of_sides_triangle_1 = float(
                        input(f"Enter the {side} side of the first triangle (angle): "))
                    self.tr1_sides.append(self.reformat_light_sides(angles_of_sides_triangle_1))

                if (side >= 3) and (side < 6):
                    side += 1
                    angles_of_sides_triangle_2 = float(
                        input(f"Enter the {side - 3} side of the second triangle (angle): "))
                    self.tr2_sides.append(self.reformat_light_sides(angles_of_sides_triangle_2))

                if side >= 6:
                    self.tr1_error = self.calculate_error(self.tr1_sides)
                    self.tr2_error = self.calculate_error(self.tr2_sides)
                    # Calculates the mean error
                    self.error_triangle = self.tr1_error + self.tr2_error
                    self.error = round(self.error_triangle + self.measuring_error, 1)

                    cond_triangle = False
                    side = 0
                    continue

            angle_inp = float(input("Enter twist angle of sample (in degrees): "))
            self.org_twist_angle = angle_inp

            # This returns angle reformatted
            self.twist_angle = self.reformat_angles(angle_inp, degree_range)

            # Parses the spots in order to print them and gets them into an integer format
            spots = spot_name_inp.rsplit(",")

            for i in spots:
                self.spots.append(int(i))

            # Writes data to file
            self.update_file(self.file_path_csv)

            # Reset the spots and the triangle sides
            self.tr1_sides, self.tr2_sides, self.spots = [], [], []

            print("Data confirmed!")


if __name__ == "__spotangle_saver__":
    csv_pro = CSV()
    csv_pro.writing_loop()
