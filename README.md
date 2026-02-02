Matrix Operations Tool (Python + NumPy)

A simple command-line Matrix Operations Tool built using Python and NumPy.
This tool allows users to perform common matrix operations interactively with neatly formatted outputs.

🚀 Features

The program supports the following matrix operations:

➕ Matrix Addition

➖ Matrix Subtraction

✖ Matrix Multiplication

🔄 Matrix Transpose

📐 Determinant of a Matrix

❌ Exit the program

All results are displayed in a clean table format using the tabulate library.

🛠 Technologies Used

Python 3

NumPy – for matrix computations

Tabulate – for formatted table display in terminal

📦 Installation
1️⃣ Clone or Download the Project
git clone https://github.com/CodeMasterZahab/matrix-operations-tool.git
cd matrix-operations-tool


(Or simply download the .py file and place it in a folder.)

2️⃣ Install Required Libraries
pip install numpy tabulate

▶️ How to Run
python matrix_tool.py

You will see a menu like:
--- MATRIX OPERATIONS TOOL ---
1. Add  2. Subtract  3. Multiply  4. Transpose  5. Determinant  6. Exit

Enter the number corresponding to the operation you want to perform.

🧑‍💻 How It Works
🔢 Matrix Input

You will be asked to enter:
Number of rows
Number of columns
Matrix elements row by row (space-separated)

Example:
Enter number of rows: 2
Enter number of columns: 2
Row 1: 1 2
Row 2: 3 4

🧮 Supported Operations Explained
➕ Addition
Adds two matrices of the same dimensions.

➖ Subtraction
Subtracts Matrix B from Matrix A (same dimensions required).\

✖ Multiplication
Performs matrix multiplication using NumPy's dot product rule.

🔄 Transpose
Converts rows into columns.

📐 Determinant
Calculates determinant only for square matrices.
If a non-square matrix is entered, the program shows:
Error: Determinant requires a square matrix.

⚠️ Error Handling
The program safely handles:
Invalid matrix sizes for operations
Incorrect input formats
Determinant calculation for non-square matrices
Errors are displayed without crashing the program.

📸 Sample Output
Result:
╒═══════╤═══════╕
│  6.0  │  8.0  │
├───────┼───────┤
│ 10.0  │ 12.0  │
╘═══════╧═══════╛

Future Improvements
Add Inverse of a Matrix
Add Eigenvalues & Eigenvectors
Add Save/Load matrices from file
Build a GUI version

 Educational Purpose
This project is great for:
Understanding matrix mathematics
Practicing NumPy operations
Learning Python CLI application development

 License
This project is open-source and free to use for learning purposes.