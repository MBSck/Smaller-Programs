"""This makes the 2D-Heatmap plot and fits them into a lineplot"""
__author__: "Marten Scheuck"


def read_dat_file(file):
    """Reads a file and flattens it into a single row"""

    flattened_file_content = []

    with open(file, "r") as f:
        for row in f:
            column_file = row.split()
            for i in column_file:
                edited = i.replace(',', '.')
                flattened_file_content.append(edited)

    return flattened_file_content


def line_fit(x_value: float, params: tuple):
    """Fits a line and returns point on line for input"""

    start_point, end_point = params

    m = (end_point[1] - start_point[1]) / (end_point[0] - start_point[0])
    n = (start_point[1] * end_point[0] - end_point[1] * start_point[0]) / (end_point[0] - start_point[0])

    return round(m * x_value + n, 3)


def parabola_fit(x_value, params: tuple):
    """Parabola fit"""
    a, b, c = params
    return a + b*x_value + c*(x_value**2)


def divide_chunks(input_list, n):
    """Divides lists into smaller ones"""
    for i in range(0, len(input_list), n):
        yield input_list[i:i + n]


def make_dat_file(input_list, output_filename: str, row_length: int):
    """Reads the data into a 2d plot format and saves it as a dat"""

    edited_list = list(divide_chunks(input_list, row_length))

    with open(output_filename, "w+") as f:
        for i in edited_list:
            for j in i:
                f.write(str(j) + '\t')

            f.write('\n')


def fit_data(file: str, fit_to_use, params: tuple, output_file_row_length: int = 3):
    """Fits the data and then converts it back into the 2D format"""

    flattened_list = read_dat_file(file)
    fitted_list = []
    file_name = file.split(".")

    for i in flattened_list:
        fitted_list.append(fit_to_use(float(i), params))

    make_dat_file(fitted_list, output_filename=(file_name[0] + "_" + fit_to_use.__name__ + "ted.txt"),
                  row_length=output_file_row_length)


if __name__ == "__main__":
    fit_data("HeatmapFLA.txt", line_fit, ((105.865699, 12.3853645), (113.633904, 13.5465124)), 3)
    fit_data("HeatmapFTA.txt", line_fit, ((72.1357523, 12.3853645), (78.1839751, 13.5465124)), 3)

    fit_data("HeatmapFLA.txt", parabola_fit, (6.76955, -0.03686, 8.49205E-4))
    fit_data("HeatmapFTA.txt", parabola_fit, (2.48965, 0.0866, 7.01202E-4))
