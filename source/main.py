
from source.models.file_model import FileModel
from source.gui.main_window import MainWindow
from source.controllers.file_controller import FileController

def main():
    model = FileModel()
    view = MainWindow()  
    controller = FileController(model, view)
    view.controller = controller
    view.mainloop()

if __name__ == "__main__":
    main()