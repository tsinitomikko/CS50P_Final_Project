import os
import action as act
import sys

from utils import Action, Type, Strings, clear_terminal
from sheet import Sheet
import entry


def main():
    """
    This is the entry point of the program.

    Args:

    Returns:
        None
    """
    try:
        update_directory()
    except (KeyboardInterrupt, EOFError):
        print(Strings.err_input_interrupted)
    except (IndexError, ValueError):
        print(Strings.err_invalid_choice)


def update_directory():
    """
    Assign the flow of updating the files and folders in the user-defined directory.

    Args:

    Returns:
        None
    """
    entry_type = select_type_from_user()
    action = select_action_from_user(entry_type=entry_type)
    sheet, input_dir, entries = launch_sheet_window(action=action, entry_type=entry_type)
    ask_to_save_changes(sheet=sheet,
                        action=action,
                        entry_type=entry_type,
                        input_dir=input_dir,
                        entries=entries)


def select_type_from_user() -> Type:
    """
    Shows the user data type options to manage.

    Args:

    Returns:
        Type:   The type of data.
    """
    clear_terminal()
    print(Strings.prompt_manage)
    options = [
        Strings.option_none,
        Strings.option_files,
        Strings.option_folders]
    print_options(options)
    input_item = int(input(Strings.input_item))
    entry_type = None
    match options[input_item]:
        case Strings.option_none:
            entry_type = None
            print()
            sys.exit(0)
        case Strings.option_files:
            entry_type = Type.FILE
        case Strings.option_folders:
            entry_type = Type.FOLDER
    return entry_type


def select_action_from_user(entry_type: Type) -> Action:
    """
    Shows the user actions for the data type to manage.

    Args:
        entry_type:     The data type.

    Returns:
        action:         The action to execute with the data type.
    """
    print()
    print(Strings.prompt_action)
    options = []
    match entry_type:
        case Type.FILE:
            options = [
                Strings.back,
                Strings.option_rename]
        case Type.FOLDER:
            options = [
                Strings.back,
                Strings.option_create,
                Strings.option_rename]
    print_options(options)
    input_item = int(input(Strings.input_action))
    action = None
    match options[input_item]:
        case Strings.back:
            action = None
            update_directory()
        case Strings.option_create:
            action = Action.CREATE
        case Strings.option_rename:
            action = Action.RENAME
    return action


def launch_sheet_window(action: Action,
                        entry_type: Type) -> tuple[Sheet, str, list]:
    """
    Opens a spreadsheet application from the user's computer.

    Args:
        action:     The action to to execute with the data type.
        entry_type: The data type to manage.
    Returns:
        sheet:      An object to setup the spreadsheet.
        input_dir:  Directory of the file or folder to manage.
        entries:    The file or folder items in the directory.
    """
    print()
    sheet = Sheet()
    input_dir = input(Strings.input_path).strip("'\"")
    if not os.path.isdir(input_dir):
        print(Strings.err_dir_not_found.format(dir=input_dir))
        sys.exit(1)
    else:
        entries = []
        match action:
            case Action.CREATE:
                sheet.create(input_dir=input_dir,
                             headers=entry.header_create()
                             ).show()
            case Action.RENAME:
                entries = entry.get_entries(type=entry_type,
                                            dir=input_dir)
                if len(entries) > 0:
                    sheet.rename(input_dir=input_dir,
                                 entries=entries,
                                 headers=entry.header_rename(entry_type)
                                 ).show()
                else:
                    print(Strings.err_entries_not_found.format(dir=input_dir))
                    sys.exit(1)
        return sheet, input_dir, entries


def ask_to_save_changes(sheet: Sheet,
                        action: Action,
                        entry_type: Type,
                        input_dir: str,
                        entries: list):
    """
    Asks the user to save the changes made in the spreadsheet.

    Args:
        sheet:      The spreadsheet object.
        action:     The action to be executed with the files or folders.
        entry_type: The data type.
        input_dir:  The user-defined directory.
        entries:    The list of files or folders.
    Retruns:
        None
    """
    while True:
        ans = input(Strings.input_save).lower()
        workbook = sheet.load()
        match ans:
            case "y" | "yes":
                match action:
                    case Action.CREATE:
                        act.create(workbook=workbook,
                                   input_dir=input_dir)
                        break
                    case Action.RENAME:
                        act.rename(workbook=workbook,
                                   entry_dir=input_dir,
                                   entry_type=entry_type,
                                   entries=entries)
                        break
                break
            case "n" | "no":
                print(Strings.err_rename_cancelled)
                break
            case _:
                print(Strings.err_invalid_choice)
    sheet.delete()


def print_options(options):
    """
    Prints the option in a numerical order.

    Args:
        options:    List of strings to show.
    Returns:
        None
    """
    for i, option in enumerate(options):
        if option is not None:
            print(Strings.option_item.format(i=i, option=option))
    print()


if __name__ == '__main__':
    main()
