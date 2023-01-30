# design a matrix calculator, which can do the following operations:
# 1. add two matrices
# 2. subtract two matrices
# 3. multiply two matrices
# 4. transpose a matrix
# 5. calculate the determinant of a matrix
# 6. inverse a matrix
# 7. solve a system of linear equations
# 8. exit the program

# import the matrix class
from tkinter import *
import numpy as np 

def check_value(value):
    """ this function will check if a value is int or float. """
    try:
        value = float(value)
        return True
    except ValueError:
        return False

def string2matrix(str):
    """ 
    this function will extract the matrix from a string input. 
    The string must be in the following format: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    if the string is not in the correct format, the function will return None.
    """
    # change "[" to "" and change "]" to ";"
    str = str.replace("[", "")
    str = str.replace("]", ";")
    rows = str.split(";")

    # extract the matrix
    matrix = []
    for row in rows:
        row = row.split(",")
        row_value = []
        for i in range(len(row)):
            row[i] = row[i].strip()
            if row[i] == "":
                continue
            if not check_value(row[i]):
                return None
            row_value.append(float(row[i]))
        if len(row_value) != 0:
            matrix.append(row_value)

    # check if the matrix is valid
    if len(matrix) == 0:
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return None

    # convert the matrix to a numpy array
    matrix = np.array(matrix)
    return matrix


# create a class for the GUI of the matrix calculator
class MatrixCalculator:

    # initialize the GUI
    def __init__(self, root):
        # create a frame
        frame = Frame(root)
        frame.pack()

        # create a label for the matrix calculator
        self.label = Label(frame, text="Matrix Calculator")
        self.label.pack()

        # create a button for adding two matrices
        self.add_button = Button(frame, text="Add two matrices", command=self.add_matrices)
        self.add_button.pack()

        # create a button for subtracting two matrices
        self.subtract_button = Button(frame, text="Subtract two matrices", command=self.subtract_matrices)
        self.subtract_button.pack()

        # create a button for multiplying two matrices
        self.multiply_button = Button(frame, text="Multiply two matrices", command=self.multiply_matrices)
        self.multiply_button.pack()

        # create a button for transposing a matrix
        self.transpose_button = Button(frame, text="Transpose a matrix", command=self.transpose_matrix)
        self.transpose_button.pack()

        # create a button for calculating the determinant of a matrix
        self.determinant_button = Button(frame, text="Calculate the determinant of a matrix", command=self.determinant_matrix)
        self.determinant_button.pack()

        # create a button for inverting a matrix
        self.inverse_button = Button(frame, text="Invert a matrix", command=self.inverse_matrix)
        self.inverse_button.pack()

        # create a button for solving a system of linear equations
        self.solve_button = Button(frame, text="Solve a system of linear equations", command=self.solve_linear_equations)
        self.solve_button.pack()

        # create a button for exiting the program
        self.exit_button = Button(frame, text="Exit", command=frame.quit)
        self.exit_button.pack()

    def add_matrices_calc(self):
        """ when the add_matrices button is pressed, this function will be called. It will add the two matrices and display the result in a new window. """
        # get the first matrix
        matrix1 = self.add_entry1.get()
        matrix1 = string2matrix(matrix1)


        if matrix1 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The first matrix is not valid.")
            self.error_label.pack()

            return

        # get the second matrix
        matrix2 = self.add_entry2.get()
        matrix2 = string2matrix(matrix2)

        if matrix2 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The second matrix is not valid.")
            self.error_label.pack()

            return
        
        # check if the two matrices have the same shape
        if matrix1.shape != matrix2.shape:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The two matrices must have the same shape.")
            self.error_label.pack()

            return
        
        # add the two matrices
        result = matrix1 + matrix2

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for adding two matrices
    def add_matrices(self):
        # create a new window
        add_window = Toplevel(root)
        add_window.title("Add two matrices")

        # create a label for the first matrix
        self.add_label1 = Label(add_window, text="Enter the first matrix:")
        self.add_label1.pack()

        # create an entry for the first matrix
        self.add_entry1 = Entry(add_window)
        self.add_entry1.pack()

        # create a label for the second matrix
        self.add_label2 = Label(add_window, text="Enter the second matrix:")
        self.add_label2.pack()

        # create an entry for the second matrix
        self.add_entry2 = Entry(add_window)
        self.add_entry2.pack()

        # create a button for adding the two matrices
        self.add_button = Button(add_window, text="Add the two matrices", command=self.add_matrices_calc)
        self.add_button.pack()

    def subtract_matrices_calc(self):
        """ when the subtract_matrices button is pressed, this function will be called. It will subtract the two matrices and display the result in a new window. """
        # get the first matrix
        matrix1 = self.subtract_entry1.get()
        matrix1 = string2matrix(matrix1)

        if matrix1 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The first matrix is not valid.")
            self.error_label.pack()

            return

        # get the second matrix
        matrix2 = self.subtract_entry2.get()
        matrix2 = string2matrix(matrix2)

        if matrix2 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The second matrix is not valid.")
            self.error_label.pack()

            return
        
        # check if the two matrices have the same shape
        if matrix1.shape != matrix2.shape:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The two matrices must have the same shape.")
            self.error_label.pack()

            return
        
        # subtract the two matrices
        result = matrix1 - matrix2

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for subtracting two matrices
    def subtract_matrices(self):
        # create a new window 
        subtract_window = Toplevel(root)
        subtract_window.title("Subtract two matrices")

        # create a label for the first matrix
        self.subtract_label1 = Label(subtract_window, text="Enter the first matrix:")
        self.subtract_label1.pack()

        # create an entry for the first matrix
        self.subtract_entry1 = Entry(subtract_window)
        self.subtract_entry1.pack()

        # create a label for the second matrix
        self.subtract_label2 = Label(subtract_window, text="Enter the second matrix:")
        self.subtract_label2.pack()

        # create an entry for the second matrix
        self.subtract_entry2 = Entry(subtract_window)
        self.subtract_entry2.pack()

        # create a button for subtracting the two matrices
        self.subtract_button = Button(subtract_window, text="Subtract the two matrices", command=self.subtract_matrices_calc)
        self.subtract_button.pack()

    def multiply_matrices_calc(self):
        """ when the multiply_matrices button is pressed, this function will be called. It will multiply the two matrices and display the result in a new window. """
        # get the first matrix
        matrix1 = self.multiply_entry1.get()
        matrix1 = string2matrix(matrix1)

        if matrix1 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The first matrix is not valid.")
            self.error_label.pack()

            return

        # get the second matrix
        matrix2 = self.multiply_entry2.get()
        matrix2 = string2matrix(matrix2)

        if matrix2 is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The second matrix is not valid.")
            self.error_label.pack()

            return
        
        # check if the two matrices can be multiplied 
        if matrix1.shape[1] != matrix2.shape[0]:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The two matrices cannot be multiplied.")
            self.error_label.pack()

            return
        
        # multiply the two matrices
        result = matrix1 @ matrix2

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for multiplying two matrices
    def multiply_matrices(self):
        # create a new window
        multiply_window = Toplevel(root)
        multiply_window.title("Multiply two matrices")

        # create a label for the first matrix
        self.multiply_label1 = Label(multiply_window, text="Enter the first matrix:")
        self.multiply_label1.pack()

        # create an entry for the first matrix
        self.multiply_entry1 = Entry(multiply_window)
        self.multiply_entry1.pack()

        # create a label for the second matrix
        self.multiply_label2 = Label(multiply_window, text="Enter the second matrix:")
        self.multiply_label2.pack()

        # create an entry for the second matrix
        self.multiply_entry2 = Entry(multiply_window)
        self.multiply_entry2.pack()

        # create a button for multiplying the two matrices
        self.multiply_button = Button(multiply_window, text="Multiply the two matrices", command=self.multiply_matrices_calc)
        self.multiply_button.pack()

    def transpose_matrix_calc(self):
        """ when the transpose_matrix button is pressed, this function will be called. It will transpose the matrix and display the result in a new window. """
        # get the matrix
        matrix = self.transpose_entry.get()
        matrix = string2matrix(matrix)

        if matrix is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not valid.")
            self.error_label.pack()

            return
        
        # transpose the matrix
        result = matrix.T

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for transposing a matrix
    def transpose_matrix(self):
        # create a new window
        transpose_window = Toplevel(root)
        transpose_window.title("Transpose a matrix")

        # create a label for the matrix
        self.transpose_label = Label(transpose_window, text="Enter the matrix:")
        self.transpose_label.pack()

        # create an entry for the matrix
        self.transpose_entry = Entry(transpose_window)
        self.transpose_entry.pack()

        # create a button for transposing the matrix
        self.transpose_button = Button(transpose_window, text="Transpose the matrix", command=self.transpose_matrix_calc)
        self.transpose_button.pack()

    def determinant_matrix_calc(self):
        """ when the determinant_matrix button is pressed, this function will be called. It will calculate the determinant of the matrix and display the result in a new window. """
        # get the matrix
        matrix = self.determinant_entry.get()
        matrix = string2matrix(matrix)

        if matrix is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not valid.")
            self.error_label.pack()

            return
        
        # check if the matrix is a square matrix
        if matrix.shape[0] != matrix.shape[1]:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not a square matrix.")
            self.error_label.pack()

            return
        
        # calculate the determinant of the matrix
        result = np.linalg.det(matrix)

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for calculating the determinant of a matrix
    def determinant_matrix(self):
        # create a new window
        determinant_window = Toplevel(root)
        determinant_window.title("Calculate the determinant of a matrix")

        # create a label for the matrix
        self.determinant_label = Label(determinant_window, text="Enter the matrix:")
        self.determinant_label.pack()

        # create an entry for the matrix
        self.determinant_entry = Entry(determinant_window)
        self.determinant_entry.pack()

        # create a button for calculating the determinant of the matrix
        self.determinant_button = Button(determinant_window, text="Calculate the determinant of the matrix", command=self.determinant_matrix_calc)
        self.determinant_button.pack()
    
    def inverse_matrix_calc(self):
        """ when the inverse_matrix button is pressed, this function will be called. It will invert the matrix and display the result in a new window. """
        # get the matrix
        matrix = self.inverse_entry.get()
        matrix = string2matrix(matrix)

        if matrix is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not valid.")
            self.error_label.pack()

            return
        
        # check if the matrix is a square matrix
        if matrix.shape[0] != matrix.shape[1]:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not a square matrix.")
            self.error_label.pack()

            return
        
        # check if the matrix is invertible
        if np.linalg.det(matrix) == 0:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not invertible.")
            self.error_label.pack()

            return
        
        # invert the matrix
        result = np.linalg.inv(matrix)

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    # create a function for inverting a matrix
    def inverse_matrix(self):
        # create a new window
        inverse_window = Toplevel(root)
        inverse_window.title("Invert a matrix")

        # create a label for the matrix
        self.inverse_label = Label(inverse_window, text="Enter the matrix:")
        self.inverse_label.pack()

        # create an entry for the matrix
        self.inverse_entry = Entry(inverse_window)
        self.inverse_entry.pack()

        # create a button for inverting the matrix
        self.inverse_button = Button(inverse_window, text="Invert the matrix", command=self.inverse_matrix_calc)
        self.inverse_button.pack()

    def solve_linear_equations_calc(self):
        """ when the solve_linear_equations button is pressed, this function will be called. It will solve the system of linear equations and display the result in a new window. """
        # get the matrix
        matrix = self.solve_entry.get()
        matrix = string2matrix(matrix)

        if matrix is None:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not valid.")
            self.error_label.pack()

            return
        
        c = matrix[:, -1]
        A = matrix[:, :-1]
        
        # check if the matrix is a square matrix
        if A.shape[0] != A.shape[1]:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not a square matrix.")
            self.error_label.pack()

            return
        
        # check if the matrix is invertible
        if np.linalg.det(A) == 0:
            # create a new window
            error_window = Toplevel(root)
            error_window.title("Error")

            # create a label for the error
            self.error_label = Label(error_window, text="The matrix is not invertible.")
            self.error_label.pack()

            return
        
        # solve the system of linear equations
        result = np.linalg.inv(A) @ c

        # create a new window
        result_window = Toplevel(root)
        result_window.title("Result")

        # create a label for the result
        self.result_label = Label(result_window, text=result)
        self.result_label.pack()

    def solve_linear_equations(self):
        # create a new window
        solve_window = Toplevel(root)
        solve_window.title("Solve a system of linear equations")

        # create a label for the matrix
        self.solve_label = Label(solve_window, text="Enter the matrix:")
        self.solve_label.pack()

        # create an entry for the matrix
        self.solve_entry = Entry(solve_window)
        self.solve_entry.pack()

        # create a button for solving the system of linear equations
        self.solve_button = Button(solve_window, text="Solve the system of linear equations", command=self.solve_linear_equations_calc)
        self.solve_button.pack()
        
    # create a function for solving a system of linear equations
    def solve_system(self):
        # create a new window
        solve_window = Toplevel(root)
        solve_window.title("Solve a system of linear equations")

        # create a label for the matrix
        self.solve_label = Label(solve_window, text="Enter the matrix:")
        self.solve_label.pack()

        # create an entry for the matrix
        self.solve_entry = Entry(solve_window)
        self.solve_entry.pack()

        # create a button for solving the system of linear equations
        self.solve_button = Button(solve_window, text="Solve the system of linear equations", command=self.solve_system)
        self.solve_button.pack()
    
# create a main function
def main():
    # create a window
    global root
    root = Tk()
    root.title("Matrix Calculator")

    # create a menu
    menu = Menu(root)
    root.config(menu=menu)

    # create a file menu
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.destroy)

    # create a help menu
    help_menu = Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)

    # create a calculator object
    calculator = MatrixCalculator(root)

    # enter the main loop
    root.mainloop()

# call the main function
main()