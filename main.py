import numpy as np
from tabulate import tabulate # Run 'pip install tabulate' for beautiful tables

class MatrixTool:
    def __init__(self):
        self.matrices = {}

    def get_matrix_input(self, name):
        print(f"\n--- Input for Matrix {name} ---")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print(f"Enter elements row by row (space-separated):")
        elements = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            elements.append(row)
        return np.array(elements)

    def display(self, matrix, title="Result"):
        print(f"\n{title}:")
        print(tabulate(matrix, tablefmt="fancy_grid"))

    def run(self):
        while True:
            print("\n--- MATRIX OPERATIONS TOOL ---")
            print("1. Add  2. Subtract  3. Multiply  4. Transpose  5. Determinant  6. Exit")
            choice = input("Select operation: ")

            if choice == '6': break
            
            try:
                if choice in ['1', '2', '3']:
                    A = self.get_matrix_input("A")
                    B = self.get_matrix_input("B")
                    if choice == '1': res = np.add(A, B)
                    elif choice == '2': res = np.subtract(A, B)
                    else: res = np.dot(A, B)
                    self.display(res)
                
                elif choice == '4':
                    A = self.get_matrix_input("A")
                    self.display(A.T, "Transposed Matrix")
                
                elif choice == '5':
                    A = self.get_matrix_input("A")
                    if A.shape[0] == A.shape[1]:
                        det = np.linalg.det(A)
                        print(f"\n➤ Determinant: {det:.2f}")
                    else:
                        print("Error: Determinant requires a square matrix.")
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    tool = MatrixTool()
    tool.run()