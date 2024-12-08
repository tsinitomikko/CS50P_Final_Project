import unittest
from io import StringIO
from typing import AnyStr
from unittest.mock import Mock, \
    patch
from project import launch_sheet_window, \
    select_type_from_user, \
    select_action_from_user, \
    ask_to_save_changes, \
    print_options
from utils import Action, \
    Strings, \
    Type


class TestProject(unittest.TestCase):

    #
    # --> Method: print_options(options)
    #
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_options(self, mock_stdout):
        """
        --> Test: print enumerated options.
        """
        options = [
            "Option 1",
            "Option 2",
            "Option 3"]
        print_options(options)
        output = mock_stdout.getvalue().strip().splitlines()
        self.assertRegex(output[0], r"\[0\] Option 1")
        self.assertRegex(output[1], r"\[1\] Option 2")
        self.assertRegex(output[2], r"\[2\] Option 3")

    #
    # --> Method: select_type_from_user()
    #
    @patch('sys.exit')
    @patch('builtins.input', return_value=1)
    def test_select_type_from_user(self,
                                   _,
                                   mock_exit):
        """
        Test: input '1' or 'File' from items.
            Select an item to manage:
            [0] ...
        --> [1] Files
        --> [2] Folders
        """
        selected_type = select_type_from_user()
        self.assertIsInstance(selected_type, Type)
        mock_exit.assert_not_called()

    @patch('sys.exit')
    @patch('builtins.input', return_value=0)
    def test_select_type_from_user_none(self,
                                        _,
                                        mock_exit):
        """
        Test: input '0' or 'None' from items.
            Select an item to manage:
        --> [0] ...
            [1] Files
            [2] Folders
        """
        selected_type = select_type_from_user()
        self.assertEqual(selected_type, None)
        mock_exit.assert_called_once_with(0)

    @patch('sys.exit')
    @patch('builtins.input', return_value=1)
    def test_select_type_from_user_file(self,
                                        _,
                                        mock_exit):
        """
        Test: input '1' or 'File' from items.
            Select an item to manage:
            [0] ...
        --> [1] Files
            [2] Folders
        """
        selected_type = select_type_from_user()
        self.assertEqual(selected_type, Type.FILE)
        mock_exit.assert_not_called()

    @patch('sys.exit')
    @patch('builtins.input', return_value=2)
    def test_select_type_from_user_folder(self,
                                          _,
                                          mock_exit):
        """
        Test: input '2' or 'Folder' from items.
            Select an item to manage:
            [0] ...
            [1] Files
        --> [2] Folders
        """
        selected_type = select_type_from_user()
        self.assertEqual(selected_type, Type.FOLDER)
        mock_exit.assert_not_called()

    @patch('builtins.input', return_value=3)
    def test_select_type_from_user_3(self, _):
        """
        Test: input '3' or not from items.
            Select an item to manage:
            [0] ...
            [1] Files
            [2] Folders
        """
        with self.assertRaises(IndexError):
            select_type_from_user()

    @patch('builtins.input', return_value="ASD")
    def test_select_type_from_user_ASD(self,
                                       _):
        """
        Test: input 'ASD' or not from items.
            Select an item to manage:
            [0] ...
            [1] Files
            [2] Folders
        """
        with self.assertRaises(ValueError):
            select_type_from_user()

    @patch('builtins.input', return_value="")
    def test_select_type_from_user_blank(self,
                                         _):
        """
        Test: input '' or blank.
            Select an item to manage:
            [0] ...
            [1] Files
            [2] Folders
        """
        """Test input characters."""
        with self.assertRaises(ValueError):
            select_type_from_user()

    #
    # --> Method: select_action_from_user(type:Type) -> Action:
    #
    @patch('project.update_directory')
    @patch('builtins.input', return_value="1")
    def test_select_action_from_user(self,
                                     _,
                                     mock_update_directory):
        """
        Test: input '1' or 'Rename' from 'File' actions.
            Select action:
            [0] ..
        --> [1] Rename
        """
        action = select_action_from_user(Type.FILE)
        self.assertIsInstance(action, Action)
        mock_update_directory.assert_not_called()

    @patch('project.update_directory')
    @patch('builtins.input', return_value="0")
    def test_select_action_from_user_back(self,
                                          _,
                                          mock_update_directory):
        """
        Test: input '0' or back from actions.
        File
            Select action:
        --> [0] ..
            [1] Create
            [2] Rename
        Folder
            Select action:
        --> [0] ..
            [1] Create
            [2] Rename
        """
        action = select_action_from_user(Type.FILE)
        self.assertEqual(action, None)
        action = select_action_from_user(Type.FOLDER)
        self.assertEqual(action, None)
        self.assertEqual(mock_update_directory.call_count, 2)

    @patch('project.update_directory')
    @patch('builtins.input', return_value="1")
    def test_select_action_from_user_rename(self,
                                            _,
                                            mock_update_directory):
        """
        Test: input '1' or 'Rename' from 'File' actions.
            Select action:
            [0] ..
        --> [1] Rename
        """
        action = select_action_from_user(Type.FILE)
        self.assertEqual(action, Action.RENAME)
        mock_update_directory.assert_not_called()

    @patch('project.update_directory')
    @patch('builtins.input', return_value="2")
    def test_select_action_from_user_2(self,
                                       _,
                                       mock_update_directory):
        """
        Test: input '2' or none from 'File' actions.
            Select action:
            [0] ..
        --> [1] Rename
        """
        with self.assertRaises(IndexError):
            select_action_from_user(Type.FILE)
        mock_update_directory.assert_not_called()

    @patch('builtins.input', return_value="")
    def test_select_action_from_user_blank(self,
                                           _):
        """
        Test: input '' or none from 'File' actions.
            Select action:
            [0] ..
            [1] Rename
        """
        with self.assertRaises(ValueError):
            select_action_from_user(Type.FILE)

    @patch('project.update_directory')
    @patch('builtins.input', return_value="1")
    def test_select_action_from_user_create(self,
                                            _,
                                            mock_update_directory):
        """
        Test: input '1' or 'Create' from 'Folder' actions.
            Select action:
            [0] ..
        --> [1] Create
            [2] Rename
        """
        action = select_action_from_user(Type.FOLDER)
        self.assertEqual(action, Action.CREATE)
        mock_update_directory.assert_not_called()

    @patch('project.update_directory')
    @patch('builtins.input', return_value="2")
    def test_select_action_from_user_rename(self,
                                            _,
                                            mock_update_directory):
        """
        Test: input '2' or 'Rename' from 'Folder' actions.
            Select action:
            [0] ..
            [1] Create
        --> [2] Rename
        """
        action = select_action_from_user(Type.FOLDER)
        self.assertEqual(action, Action.RENAME)
        mock_update_directory.assert_not_called()

    @patch('project.update_directory')
    @patch('builtins.input', return_value="3")
    def test_select_action_from_user_3(self,
                                       _,
                                       mock_update_directory):
        """
        Test: input 3 or none from 'Folder' actions.
            Select action:
            [0] ..
            [1] Create
            [2] Rename
        """
        with self.assertRaises(IndexError):
            select_action_from_user(Type.FOLDER)
            mock_update_directory.assert_not_called()

    @patch('project.update_directory')
    @patch('builtins.input', return_value="")
    def test_select_action_from_user_blank(self,
                                           _,
                                           mock_update_directory):
        """
        Test: input '' or none from 'Folder' actions.
            Select action:
            [0] ..
            [1] Create
            [2] Rename
        """
        with self.assertRaises(ValueError):
            select_action_from_user(Type.FOLDER)
            mock_update_directory.assert_not_called()

    #
    # --> Method: launch_sheet_window(action:Action, type:Type) -> tuple[Sheet, str, list]:
    #
    @patch("sheet.Sheet.show")
    @patch("sheet.Sheet.rename")
    @patch("entry.get_entries")
    @patch("os.path.isdir")
    @patch("sys.exit")
    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window(self,
                                 _,
                                 mock_print,
                                 mock_exit,
                                 mock_isdir,
                                 mock_get_entries,
                                 mock_sheet_rename,
                                 mock_sheet_show):
        """
        Test input is a directory.
        Select action:
            [0] ..
            [1] Create
        --> [2] Rename
        Enter Directory Path: .../valid path/
        Initializing spreadsheet...
        """
        mock_isdir.return_value = True
        mock_get_entries.return_value = []
        mock_sheet_rename.return_value = Mock()
        mock_sheet_rename.return_value.show = mock_sheet_show
        result = launch_sheet_window(action=Action.RENAME,
                                     entry_type=AnyStr)
        self.assertIsInstance(result, tuple)

    @patch("sys.exit")
    @patch("builtins.print")
    @patch("os.path.isdir")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window_not_dir(self,
                                _,
                                mock_isdir,
                                mock_print,
                                mock_exit):
        """
        Test input not a directory.
            Enter Directory Path: .../invalid path/
        """
        mock_isdir.return_value = False
        launch_sheet_window(action=AnyStr,
                            entry_type=AnyStr)
        self.assertEqual(mock_print.call_args_list[-1][0][0], Strings.err_dir_not_found.format(dir=""))
        mock_exit.assert_called_once_with(1)

    @patch("sys.exit")
    @patch("os.path.isdir")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window_is_dir(self,
                               _,
                               mock_isdir,
                               mock_exit):
        """
        Test input is a directory.
            Enter Directory Path: .../valid path/
        """
        mock_isdir.return_value = True
        launch_sheet_window(action=AnyStr,
                            entry_type=AnyStr)
        mock_exit.assert_not_called()

    @patch("sheet.Sheet.show")
    @patch("sheet.Sheet.create")
    @patch("os.path.isdir")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window_create(self,
                                 _,
                                 mock_isdir,
                                 mock_sheet_create,
                                 mock_sheet_show):
        """
        Test input is a directory.
            Select action:
            [0] ..
        --> [1] Create
            [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
        """
        mock_isdir.return_value = True
        entry = Mock()
        header_list = []
        entry.header_create.return_value = header_list
        mock_sheet_create.return_value.show = mock_sheet_show
        sheet, input_dir, entries = launch_sheet_window(action=Action.CREATE,
                                                        entry_type=AnyStr)
        mock_sheet_create.assert_called_once()
        mock_sheet_show.assert_called_once()
        self.assertEqual(sheet, sheet)
        self.assertEqual(input_dir, "")
        self.assertEqual(entries, header_list)

    @patch("sheet.Sheet.show")
    @patch("sheet.Sheet.rename")
    @patch("entry.get_entries")
    @patch("os.path.isdir")
    @patch("sys.exit")
    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window_rename_no_entries(self,
                                            _,
                                            mock_print,
                                            mock_exit,
                                            mock_isdir,
                                            mock_get_entries,
                                            mock_sheet_rename,
                                            mock_sheet_show):
        """
        Test input is a directory.
        Select action:
            [0] ..
            [1] Create
        --> [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
        """
        mock_isdir.return_value = True
        mock_get_entries.return_value = []
        mock_sheet_rename.return_value = Mock()
        mock_sheet_rename.return_value.show = mock_sheet_show
        launch_sheet_window(action=Action.RENAME,
                            entry_type=AnyStr)
        mock_sheet_rename.assert_not_called()
        mock_sheet_show.assert_not_called()
        self.assertEqual(mock_print.call_args_list[-1][0][0], Strings.err_entries_not_found.format(dir=""))
        mock_exit.assert_called_once_with(1)

    @patch("sheet.Sheet.show")
    @patch("sheet.Sheet.rename")
    @patch("entry.get_entries")
    @patch("os.path.isdir")
    @patch("sys.exit")
    @patch("builtins.input", return_value="")
    def test_launch_sheet_window_rename_with_entries(self,
                                              _,
                                              mock_exit,
                                              mock_isdir,
                                              mock_get_entries,
                                              mock_sheet_rename,
                                              mock_sheet_show):
        """
        Test input is a directory.
            Select action:
            [0] ..
            [1] Create
        --> [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
        """
        mock_isdir.return_value = True
        mock_get_entries.return_value = ["entry1", "entry2"]
        mock_sheet_rename.return_value = Mock()
        mock_sheet_rename.return_value.show = mock_sheet_show
        sheet, input_dir, entries = launch_sheet_window(action=Action.RENAME,
                                                        entry_type=AnyStr)
        mock_sheet_rename.assert_called_once()
        mock_sheet_show.assert_called_once()
        mock_exit.assert_not_called()
        # TODO: self.assertEqual(sheet, _sheet)
        self.assertEqual(input_dir, "")
        self.assertEqual(entries, ["entry1", "entry2"])

    #
    # --> Method: ask_to_save_changes(sheet:Sheet, action:Action, type:Type, input_dir: str, entries: list):
    #
    @patch('sheet.Sheet.delete')
    @patch('sheet.Sheet.load')
    @patch('sheet.Sheet')
    @patch("builtins.print")
    @patch("builtins.input", side_effect=["", "invalid", "no"])
    def test_ask_to_save_changes(self,
                                        _,
                                        mock_print,
                                        mock_sheet,
                                        mock_sheet_load,
                                        mock_sheet_delete):
        """
        Test invalid input when saving changes
            Select action:
            [0] ..
            [1] Create
            [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
            Save changes? (y/n): ""
            Save changes? (y/n): "invalid"
            Save changes? (y/n): "no"
        """
        mock_sheet.return_value = Mock()
        mock_sheet.return_value.load = mock_sheet_load
        mock_sheet.return_value.delete = mock_sheet_delete
        ask_to_save_changes(sheet=mock_sheet,
                            action=AnyStr,
                            entry_type=AnyStr,
                            input_dir=AnyStr,
                            entries=AnyStr)
        mock_print.assert_any_call(Strings.err_invalid_choice)
        self.assertEqual(mock_sheet_load.call_count, 3)
        mock_sheet_delete.assert_called_once()

    @patch('action.create')
    @patch('sheet.Sheet.delete')
    @patch('sheet.Sheet.load')
    @patch('sheet.Sheet')
    @patch("builtins.input", return_value="yes")
    def test_ask_to_save_changes_yes_create(self,
                                                  _,
                                                  mock_sheet,
                                                  mock_sheet_load,
                                                  mock_sheet_delete,
                                                  mock_action_create):
        """
        Test input 'yes' and action create when saving changes
            Select action:
            [0] ..
        --> [1] Create
            [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
            Save changes? (y/n): "yes"
        """
        mock_sheet.return_value = Mock()
        mock_sheet.return_value.load = mock_sheet_load
        mock_sheet.return_value.delete = mock_sheet_delete
        mock_action_create.return_value = Mock()
        ask_to_save_changes(sheet=mock_sheet,
                            action=Action.CREATE,
                            entry_type=AnyStr,
                            input_dir=AnyStr,
                            entries=AnyStr)
        mock_sheet_load.assert_called_once()
        mock_action_create.assert_called_once()
        mock_sheet_delete.assert_called_once()

    @patch('action.create')
    @patch('sheet.Sheet.delete')
    @patch('sheet.Sheet.load')
    @patch('sheet.Sheet')
    @patch("builtins.input", return_value="YES")
    def test_ask_to_save_changes_YES_create(self,
                                                       _,
                                                       mock_sheet,
                                                       mock_sheet_load,
                                                       mock_sheet_delete,
                                                       mock_action_create):
        """
            Test input 'YES' and action create when saving changes
            Select action:
            [0] ..
        --> [1] Create
            [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
            Save changes? (y/n): "YES"
        """
        mock_sheet.return_value = Mock()
        mock_sheet.return_value.load = mock_sheet_load
        mock_sheet.return_value.delete = mock_sheet_delete
        mock_action_create.return_value = Mock()
        ask_to_save_changes(sheet=mock_sheet,
                            action=Action.CREATE,
                            entry_type=AnyStr,
                            input_dir=AnyStr,
                            entries=AnyStr)
        mock_sheet_load.assert_called_once()
        mock_action_create.assert_called_once()
        mock_sheet_delete.assert_called_once()

    @patch('action.create')
    @patch('sheet.Sheet.delete')
    @patch('sheet.Sheet.load')
    @patch('sheet.Sheet')
    @patch("builtins.input", return_value="Y")
    def test_ask_to_save_changes_Y_create(self,
                                                     _,
                                                     mock_sheet,
                                                     mock_sheet_load,
                                                     mock_sheet_delete,
                                                     mock_action_create):
        """
        Test input Y and action create when saving changes
            Select action:
            [0] ..
        --> [1] Create
            [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
            Save changes? (y/n): "Y"
        """
        mock_sheet.return_value = Mock()
        mock_sheet.return_value.load = mock_sheet_load
        mock_sheet.return_value.delete = mock_sheet_delete
        mock_action_create.return_value = Mock()
        ask_to_save_changes(sheet=mock_sheet,
                            action=Action.CREATE,
                            entry_type=AnyStr,
                            input_dir=AnyStr,
                            entries=AnyStr)
        mock_sheet_load.assert_called_once()
        mock_action_create.assert_called_once()
        mock_sheet_delete.assert_called_once()

    @patch('action.rename')
    @patch('sheet.Sheet.delete')
    @patch('sheet.Sheet.load')
    @patch('sheet.Sheet')
    @patch("builtins.input", return_value="YES")
    def test_ask_to_save_changes_YES_rename(self,
                                                  _,
                                                  mock_sheet,
                                                  mock_sheet_load,
                                                  mock_sheet_delete,
                                                  mock_action_rename):
        """
        Test input 'Y' and action rename when saving changes
            Select action:
            [0] ..
            [1] Create
        --> [2] Rename
            Enter Directory Path: .../valid path/
            Initializing spreadsheet...
            Save changes? (y/n): 'YES'
        """
        mock_sheet.return_value = Mock()
        mock_sheet.return_value.load = mock_sheet_load
        mock_sheet.return_value.delete = mock_sheet_delete
        mock_action_rename.return_value = Mock()
        ask_to_save_changes(sheet=mock_sheet,
                            action=Action.RENAME,
                            entry_type=AnyStr,
                            input_dir=AnyStr,
                            entries=AnyStr)
        mock_sheet_load.assert_called_once()
        mock_action_rename.assert_called_once()
        mock_sheet_delete.assert_called_once()
