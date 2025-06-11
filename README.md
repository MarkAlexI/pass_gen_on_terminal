# pass_gen_on_terminal
#### Video Demo: [https://youtu.be/LLs5ptmeMVw?si=bJ_moe-H_gRIbEEE](https://youtu.be/LLs5ptmeMVw?si=bJ_moe-H_gRIbEEE)
#### GitHub Repository: [https://github.com/MarkAlexI/pass_gen_on_terminal](https://github.com/MarkAlexI/pass_gen_on_terminal)

#### Description:

**pass_gen_on_terminal** is a Python-based terminal application that allows users to quickly generate strong, customizable passwords. Designed with both simplicity and security in mind, it supports a range of features including adjustable length, optional digits and special characters, password strength validation, and the ability to save or load passwords from a local file. It provides a clean command-line interface (CLI) that users can run with different arguments to suit their preferences.

### What It Does:

The program offers several functionalities:
- Generates a random password using letters, and optionally digits and special symbols.
- Checks whether the generated password is strong (contains uppercase, lowercase, digits, special characters, and is at least 8 characters long).
- Allows saving the generated password to a file (`passwords.txt`) for later use.
- Lets users read and display previously saved passwords.
- Can be run entirely through the command line with `argparse` options, making it scriptable and efficient.

### Project Files:

- **`project.py`** – This is the core of the application. It contains:
  - `generate_password()`: Generates a password based on user-selected options.
  - `is_strong_password()`: Validates password strength according to standard security rules.
  - `save_password_to_file()`: Appends a new password to a local text file.
  - `load_passwords_from_file()`: Reads and returns previously saved passwords.
  - `main()`: Handles argument parsing and drives the command-line interface.

- **`test_project.py`** – This file includes unit tests for the core functions using `pytest`. These help ensure that the password generation and validation logic works correctly. Tests included:
  - Validating different password combinations.
  - Checking that the file-saving mechanism works.
  - Confirming correct reading from the file.

- **`requirements.txt`** – A list of pip-installable dependencies (though for this project, no external libraries are required beyond the standard library). Empty, no requirements.

### Design Choices:

I chose to keep the interface simple and fully terminal-based, both to align with Unix philosophy and to minimize dependency overhead. While GUI solutions may offer more interactivity, the CLI approach allows for quick usage in development environments and scripting scenarios.

Another important decision was making the password generator configurable via flags. Users can quickly decide what they want in a password (e.g., digits, symbols, length), which makes the tool more flexible than typical generators that produce fixed-format outputs.

Password strength validation was built in to help users understand whether the generated result is secure enough for real-world usage.

### Usage Examples:

To generate a password with all features:
```bash
python project.py -l 16 -d -s -f
