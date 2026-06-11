
class FileModel:
    def __init__(self):
        self._file_names: list[str] = []
        self._folder_path: str = ""

    def get_file_names(self) -> list[str]:
        return self._file_names.copy()

    def get_folder_path(self) -> str:
        return self._folder_path

    def set_folder_path(self, path: str) -> None:
        self._folder_path = path

    def add_file(self, name: str) -> None:
        if name: 
            self._file_names.append(name)

    def add_files(self, names: list[str]) -> None:
        for name in names:
            if name:
                self._file_names.append(name)

    def remove_file(self, index: int) -> None:
        if 0 <= index < len(self._file_names):
            self._file_names.pop(index)

    def clear_files(self) -> None:
        self._file_names.clear()