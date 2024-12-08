# Directory Management System

#### [Video Demo](https://youtu.be/S4KYQ1YYqCk)

## Description

This Python project automates directory management tasks, such as bulk file renaming and creation, for the CS50p 2024
Final Project.

## Features

- Saves time and effort with automated file and folder creation and renaming.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)

## Installation

- Ensure you have Python installed (version 3.13 or later recommended).
- Install additional dependencies using
  ```
  $ pip install colorama
  ```
  ```
  $ pip install et_xmlfile
  ```
  ```
  $ pip install openpyxl
  ```

## Usage

1. Clone this repository
2. Run the application using
   ```
   $ python project.py
   ```
3. Test the application using
   ```
   $ pytest project.py
   ```

## How it Works (Brief Overview)

This project leverages Object-Oriented Programming (OOP) principles for enhanced modularity, maintainability, and code
clarity. A well-defined class hierarchy fosters efficient code organization:

- [project.py](/project.py) - This handles user interaction and manages the overall application flow.

- [action.py](/action.py) - This class centralizes the core functionality of creating and renaming files and folders in
  the specified directory. File and permission exceptions are handled here.

- [entry.py](/entry.py) - This parent class encapsulates core attributes and methods common to both Files and Folders,
  promoting code reusability and reducing redundancy. These attributes are used as column headers in the spreadsheet.

- [sheet.py](/sheet.py) - This encapsulates functionalities that dynamically generates spreadsheets tailored to user
  choices (creating or renaming files/folders). This offers functionalities for loading existing spreadsheets,
  displaying their contents, and deleting them when no longer needed.

- [utils.py](/utils.py) - This holds reusable functions and global strings, promoting code organization and reducing
  redundancy.

- [test_project.py](/test_project.py) - Unit tests within this file ensure the correctness of individual classes and
  their methods.

The application guides the user through the process with clear prompts:

**_Item Selection:_** Choose the type of data to manage (Files or Folders)

```
Select an item to manage:
[0] ...
[1] Files
[2] Folders

Enter item:
```

_The program gracefully handles invalid input, such as non-numeric values or numbers outside the expected range of 0-2._

**_Action Selection:_** Select the desired operation (Create or Rename)

```
Select action:
[0] ..
[1] Create
[2] Rename

Enter action:
```

_The program gracefully handles invalid input, such as non-numeric values or numbers outside the expected range of 0-2._

**_Directory Selection:_** Specify the target directory path

```
Enter Directory Path:
```

_The program checks the validity of the specified directory path and provides an error message if it's invalid._

**_Spreadsheet Interaction:_** A platform-specific spreadsheet (Excel, Numbers, LibreOffice) launches for user editing.

```
Initializing spreadsheet...
```

**_Modification Confirmation:_** Choose whether to apply changes to the file system

```
Save changes? (y/n):
```

_The program checks for existing files and folders before creating new ones, preventing duplicates. It then proceeds to
update other files, providing a summary of successful and skipped operations._

Based on user selections, the application automates file/folder creation or renaming and subsequently deletes the
temporary spreadsheet. This user-centric approach streamlines directory management tasks.

## Contributing

Contributions to this project are welcome. For significant changes, please open an issue first to discuss the proposed
changes.
