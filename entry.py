import os
import sys
from datetime import datetime
from utils import Type, Strings, file_extensions


class Entry:
    def __init__(self, dir):
        self.dir = dir
        self.name = os.path.basename(dir)
        self.date_created = os.path.getctime(dir)
        self.date_modified = os.path.getmtime(dir)
        self.size = os.path.getsize(dir)

    @property
    def date_modified(self):
        return datetime.fromtimestamp(self._date_modified).strftime(
            "%b %d, %Y at %I:%M %p"
        )

    @date_modified.setter
    def date_modified(self, value):
        self._date_modified = value

    @property
    def date_created(self):
        return datetime.fromtimestamp(self._date_created).strftime(
            "%b %d, %Y at %I:%M %p"
        )

    @date_created.setter
    def date_created(self, value):
        self._date_created = value

    @property
    def size(self):
        if self._size == 0:
            return "Zero bytes"
        elif self._size < 1024:
            return f"{self._size} B"
        elif self._size < 1024 * 1024:
            return f"{self._size / 1024:.0f} KB"
        elif self._size < 1024 * 1024 * 1024:
            return f"{self._size / (1024 * 1024):.1f} MB"
        else:
            return f"{self._size / (1024 * 1024 * 1024):.1f} GB"

    @size.setter
    def size(self, value):
        self._size = value


class Folder(Entry):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_count = len(os.listdir(file_path))

    @property
    def file_count(self):
        return "" if self._file_count == 0 else str(self._file_count)

    @file_count.setter
    def file_count(self, count):
        self._file_count = count

    def values(self):
        return list([
            self.name,
            self.date_modified,
            self.file_count,
            ""])

    def list(self):
        folders = []
        for entry in os.listdir(self.dir):
            _dir = os.path.join(self.dir, entry)
            if os.path.isdir(_dir) and not entry.startswith("."): # Don't include system folders
                print(os.path.basename(_dir))
                folders.append(Folder(_dir))
        return sorted(folders, key=lambda folder: folder.name)


class File(Entry):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.type = os.path.splitext(file_path)[1]

    def values(self):
        type = file_extensions.get(self.type, Strings.document_file)
        return list([
            self.name,
            self.date_created,
            self.date_modified,
            self.size,
            type,
            ""])


def header_rename(type) -> list[str]:
    match type:
        case Type.FILE:
            headers = [
                Strings.file_name,
                Strings.file_date_created,
                Strings.folder_date_last_modified,
                Strings.file_size,
                Strings.file_type,
                Strings.rename,
            ]
        case Type.FOLDER:
            headers = [
                Strings.folder_name,
                Strings.folder_date_last_modified,
                Strings.folder_files,
                Strings.rename,
            ]
        case _:
            headers = None
    return headers


def header_create():
    return [Strings.folder_name]


def get_entries(type, dir):
    entries = []
    for entry in os.listdir(dir):
        if entry.startswith("."): # Skip system directories
            continue
        _dir = os.path.join(dir, entry)
        match type:
            case Type.FILE:
                if os.path.isfile(_dir):
                    entries.append(File(_dir))
            case Type.FOLDER:
                if os.path.isdir(_dir):
                    entries.append(Folder(_dir))
    return sorted(entries, key=lambda data: data.name)
