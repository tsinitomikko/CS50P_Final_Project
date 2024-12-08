import os
import enum
from colorama import init, Fore, Style


class Action(enum.Enum):
    CREATE = "CREATE"
    RENAME = "RENAME"


class Type(enum.Enum):
    FILE = "FILE"
    FOLDER = "FOLDER"


class Strings:
    init()

    back = ".."

    # *** Sheet Headers *** 
    spreadsheet_name = "Rename Folders"

    instructions_create = """Working Directory:  {working_dir}
Instructions:
    1. Enter new names in the \'Folder Name\' column to create new folders.
    2. Save as: {filename}
        in {filename_dir}
    3. Go back to the application and type \'yes\' to save changes."""
    instructions_rename = """Working Directory:  {working_dir}
Instructions:
    1. Enter new names in the \'Rename\' column to update file or folder names.
    2. Save as: {filename}
        in {filename_dir}
    3. Go back to the application and type \'yes\' to save changes."""

    folder_name = "Folder Name"
    folder_date_last_modified = "Date Last Modified"
    folder_files = "Files"

    file_name = "File Name"
    file_date_last_modified = "Date Last Modified"
    file_date_created = "Date Created"
    file_size = "Size"
    file_type = "Type"

    rename = "Rename"
    document_file = "Document File"

    # *** Headers *** 
    prompt_manage = Fore.BLUE + "Select an item to manage:" + Style.RESET_ALL
    prompt_action = Fore.BLUE + "Select action: " + Style.RESET_ALL

    # *** Options ***
    option_item = Fore.LIGHTBLACK_EX + "[{i}] {option}" + Style.RESET_ALL
    option_none = Fore.LIGHTBLACK_EX + "..." + Style.RESET_ALL
    option_folders = Fore.LIGHTMAGENTA_EX + "Folders" + Style.RESET_ALL
    option_files = Fore.LIGHTMAGENTA_EX + "Files" + Style.RESET_ALL
    option_create = Fore.LIGHTMAGENTA_EX + "Create" + Style.RESET_ALL
    option_rename = Fore.LIGHTMAGENTA_EX + "Rename" + Style.RESET_ALL

    # *** Input ***
    input_item = Fore.CYAN + "Enter item: " + Style.RESET_ALL
    input_action = Fore.CYAN + "Enter action: " + Style.RESET_ALL
    input_path = Fore.CYAN + "Enter Directory Path: " + Style.RESET_ALL
    input_save = Fore.CYAN + "Save changes? (y/n): " + Style.RESET_ALL

    # *** Others ***
    init_sheet = Fore.MAGENTA + "\nInitializing spreadsheet...\n" + Style.RESET_ALL

    # *** Success messages ***
    result_renaming_successful = (
            Fore.GREEN
            + Style.BRIGHT
            + "*** Renamed {num} {type} Successfully! ***\n"
            + Style.RESET_ALL
    )
    result_creating_successful = (
            Fore.GREEN
            + Style.BRIGHT
            + "*** Created {num} Folder(s) Successfully! ***\n"
            + Style.RESET_ALL
    )

    # *** Error messages ***
    err_input_interrupted = Fore.RED + Style.BRIGHT + "*** Input Interrupted! ***\n" + Style.RESET_ALL
    err_invalid_choice = Fore.RED + Style.BRIGHT + "Invalid Choice!\n" + Style.RESET_ALL
    err_invalid_action = Fore.RED + Style.BRIGHT + "Invalid Action '{action}'!\n" + Style.RESET_ALL
    err_dir_not_found = (
            Fore.RED + Style.BRIGHT + "'{dir}' not found.\n" + Style.RESET_ALL
    )
    err_dir_already_exists = (
            Fore.RED + Style.BRIGHT + "'{dir}' already exists.\n" + Style.RESET_ALL
    )
    err_permission_denied = (
            Fore.RED + Style.BRIGHT + "Permission denied for dir '{dir}'." + Style.RESET_ALL
    )
    err_occurred = (
            Fore.RED
            + Style.BRIGHT
            + "An unexpected error occurred: {err}"
            + Style.RESET_ALL
    )
    err_rename_cancelled = (
            Fore.RED + Style.BRIGHT + "*** Renaming Canceled! ***\n" + Style.RESET_ALL
    )
    err_folder_exists = (
            Fore.RED
            + Style.BRIGHT
            + "Folder '{name}' already exists. Skipping..."
            + Style.RESET_ALL
    )
    err_file_exists = (
            Fore.RED
            + Style.BRIGHT
            + "File '{name}' already exists. Skipping..."
            + Style.RESET_ALL
    )
    err_entries_not_found = (
            Fore.RED + Style.BRIGHT + "No entries found in '{dir}'.\n" + Style.RESET_ALL
    )


class Colors:
    blue_dodger = "1E90FF"
    gray_dark = "212427"
    gray_dark_medium = "808080"
    gray_light = "C0C0C0"
    purple = "800080"
    white = "FFFFFF"


# List of file extensions and their corresponding file types
file_extensions = {
    ".zip": "ZIP Archive",
    ".tar": "TAR Archive",
    ".gz": "Gzip Compressed Archive",
    ".py": "Python Source Code File",
    ".js": "JavaScript Source Code File",
    ".html": "HTML File",
    ".css": "CSS File",
    ".cpp": "C++ Source Code File",
    ".java": "Java Source Code File",
    ".c": "C Source Code File",
    ".rar": "RAR Archive",
    ".7z": "7-Zip Archive",
    ".tar.gz": "Tar Gzip Archive",
    ".tgz": "Tar Gzip Archive",
    ".rtf": "Rich Text Format File",
    ".doc": "Microsoft Word Document",
    ".docx": "Microsoft Word Document",
    ".odt": "OpenDocument Text Document",
    ".pdf": "Portable Document Format File",
    ".txt": "Plain Text File",
    ".epub": "Electronic Publication File",
    ".azw3": "Amazon Kindle eBook",
    ".djvu": "DjVu Image File",
    ".fb2": "FictionBook2 File",
    ".mobi": "Amazon Kindle eBook",
    ".pdb": "PalmDOC eBook",
    ".prc": "Palm Reader Compressed eBook",
    ".mp3": "MP3 Audio File",
    ".wav": "WAV Audio File",
    ".flac": "FLAC Audio File",
    ".aac": "AAC Audio File",
    ".mp4": "MP4 Video File",
    ".avi": "AVI Video File",
    ".mov": "MOV Video File",
    ".mkv": "MKV Video File",
    ".wmv": "Windows Media Video File",
    ".flv": "Flash Video File",
    ".webm": "WebM Video File",
    ".gif": "GIF Image File",
    ".png": "PNG Image File",
    ".jpeg": "JPEG Image File",
    ".jpg": "JPEG Image File",
    ".bmp": "BMP Image File",
    ".tif": "TIFF Image File",
    ".tiff": "TIFF Image File",
    ".webp": "WEBP Image File",
    ".svg": "Scalable Vector Graphics File",
    ".svgz": "Scalable Vector Graphics Compressed File",
    ".psd": "Photoshop Document File",
    ".ai": "Adobe Illustrator File",
    ".cdr": "CorelDRAW File",
    ".indd": "InDesign Document File",
    ".ppt": "PowerPoint Presentation File",
    ".pptx": "PowerPoint Presentation File",
    ".pps": "PowerPoint Show File",
    ".ppsx": "PowerPoint Show File",
    ".odp": "OpenDocument Presentation File",
    ".key": "Keynote Presentation File",
    ".numbers": "Numbers Spreadsheet File",
    ".pages": "Pages Document File",
    ".xls": "Microsoft Excel Spreadsheet File",
    ".xlsx": "Microsoft Excel Spreadsheet File",
    ".ods": "OpenDocument Spreadsheet File",
    ".csv": "Comma-Separated Values File",
    ".tsv": "Tab-Separated Values File",
    ".json": "JSON File",
    ".xml": "XML File",
    ".yaml": "YAML File",
    ".yml": "YAML File",
    ".sql": "SQL Database File",
    ".mdb": "Microsoft Access Database File",
    ".accdb": "Microsoft Access Database File",
    ".sqlite": "SQLite Database File",
    ".db": "Database File",
    ".exe": "Executable File",
    ".dll": "Dynamic-Link Library File",
    ".jar": "Java Archive File",
    ".apk": "Android Package File",
    ".ipa": "iOS App File",
    ".dmg": "Mac OS X Disk Image File",
    ".iso": "Disc Image File",
    ".torrent": "BitTorrent File",
    ".srt": "SubRip Subtitle File",
    ".ass": "Advanced SubStation Alpha Subtitle File",
    ".ssa": "SSA Subtitle File",
    ".ttf": "TrueType Font File",
    ".otf": "OpenType Font File",
    ".woff": "Web Open Font Format File",
    ".woff2": "Web Open Font Format 2 File",
    ".eot": "Embedded OpenType Font File",
    ".ico": "Icon File",
    ".cur": "Cursor File",
    ".ani": "Animated Cursor File"
}


def clear_terminal():
    if os.name == "nt":
        os.system("cls")  # Windows OS
    else:
        os.system("clear")  # Mac OS
