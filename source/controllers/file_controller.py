# source/controllers/file_controller.py
import os
from source.models.file_model import FileModel
from source.gui.main_window import MainWindow
from source.services.file_scanner import find_files
from source.services.trash_manager import move_to_trash

class FileController:
    
    def __init__(self, model: FileModel, view: MainWindow):
        self.model = model
        self.view = view
        self.view.controller = self
        self._update_view_from_model()
    
    def _update_view_from_model(self):
        self.view.update_file_list(self.model.get_file_names())
        self.view.update_folder_path(self.model.get_folder_path())

    def select_folder(self):
        path = self.view.ask_for_folder()
        if path:
            self.model.set_folder_path(path)
            self.view.update_folder_path(path)
    
    def add_files(self):
        file_paths = self.view.ask_for_files()
        if file_paths:
            names = [os.path.basename(p) for p in file_paths]
            self.model.add_files(names)
            self.view.update_file_list(self.model.get_file_names())
    
    def remove_selected(self):
        index = self.view.get_selected_index()
        if index is not None:
            self.model.remove_file(index)
            self.view.update_file_list(self.model.get_file_names())
        else:
            self.view.show_message("No Selection", "Please select a file to remove.", "warning")
    
    def clear_all(self):
        current_names = self.model.get_file_names()
        if not current_names:
            self.view.show_message("Empty List", "No files to clear.", "info")
            return
        
        if self.view.ask_confirmation("Clear All", f"Remove all {len(current_names)} files from the list?"):
            self.model.clear_files()
            self.view.update_file_list([])
    
    def move_to_bin(self):
        folder = self.model.get_folder_path()
        names = self.model.get_file_names()
        
        if not folder:
            self.view.show_message("No Folder", "Please select a folder first.", "warning")
            return
        if not names:
            self.view.show_message("No Files", "Please add files to the list.", "warning")
            return
        
        if not self.view.ask_confirmation(
            "Confirm Move to Bin",
            f"Move {len(names)} file(s) from\n{folder}\nto the Recycle Bin?"
        ):
            return
        
        found_paths = find_files(folder, names)
        
        if found_paths:
            success_count = move_to_trash(found_paths)
            self.view.show_message("Success", f"Moved {success_count} file(s) to trash.", "info")
        else:
            self.view.show_message("Files not found", "No such files found in the folder.", "warning")