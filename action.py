import os

from openpyxl import Workbook

from utils import Type, Strings


def rename(workbook: Workbook,
           entry_dir: str,
           entry_type: Type,
           entries: list):
    """
    This action executes rename after the user saves the changes.

    Args:
        workbook (Workbook):    The spreadsheet object.
        entry_dir (str):        The user defined directory for files or folders.
        entry_type (Type):      The data type to manage.
        entries (list):         The list of data to manage.
    Returns:
        None
    """
    print()
    rename_count = 0

    match entry_type:
        case Type.FILE:
            rename_col = 5  # rename is at 5th col
        case Type.FOLDER:
            rename_col = 3  # rename is at 3rd col
        case _:
            rename_col = 0
    list_dict = {entry.name: entry.dir for entry in entries}

    for row in workbook:
        name = row[0]
        renamed_entry = row[rename_col]
        if name in list_dict.keys():
            try:

                if renamed_entry is not None:
                    old_dir = list_dict.get(name)
                    new_dir = os.path.join(entry_dir, str(renamed_entry))

                    if entry_type == Type.FILE and os.path.isfile(new_dir):
                        print(Strings.err_file_exists.format(name=renamed_entry))
                    elif entry_type == Type.FOLDER and os.path.isdir(new_dir):
                        print(Strings.err_folder_exists.format(name=renamed_entry))
                    else:
                        os.rename(old_dir, new_dir)
                        rename_count += 1
            except FileNotFoundError:
                print(Strings.err_dir_not_found.format(dir=entry_dir))
            except FileExistsError:
                print(Strings.err_dir_already_exists.format(dir=entry_dir))
            except PermissionError:
                print(Strings.err_permission_denied.format(dir=entry_dir))
            except OSError as e:
                print(Strings.err_occurred.format(err=e))
    entry_type = "File(s)" if entry_type == Type.FILE else "Folder(s)"
    print(Strings.result_renaming_successful.format(num=rename_count, type=entry_type))


def create(workbook: Workbook,
           input_dir: str):
    """
    This action executes create after the user saves the changes.

    Args:
        workbook (Workbook):    The spreadsheet object.
        input_dir (str):        The user defined directory of files and folders.
    Returns:
        None
    """
    print()
    create_count = 0
    for row in workbook:
        folder_name = row[0]  # name column
        if folder_name is not None:
            folder_path = os.path.join(input_dir, folder_name)
            try:
                os.mkdir(folder_path)
                create_count += 1
            except FileExistsError:
                print(Strings.err_folder_exists.format(name=folder_name))
            except PermissionError:
                print(Strings.err_permission_denied.format(dir=folder_name))
            except OSError as e:
                print(Strings.err_occurred.format(err=e))
    print(Strings.result_creating_successful.format(num=create_count))
