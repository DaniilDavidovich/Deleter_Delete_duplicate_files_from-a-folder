
import os
from tkinter import *
from tkinter import filedialog, messagebox
from source.gui.widgets import FileListbox

class MainWindow(Tk):
    
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.title("Deleter")
        self.geometry("600x450")
        self.resizable(True, True)

        self._setup_widgets()
        self._layout_widgets()
        self._bind_events()

    def _setup_widgets(self):
        self.main_frame = Frame(self)
        
        self.top_frame = Frame(self.main_frame, relief=GROOVE, bd=2, padx=5, pady=5)
        self.path_label = Label(self.top_frame, text="Empty", anchor="w", relief=SUNKEN,
                                width=40, bg="white")
        self.select_folder_btn = Button(self.top_frame, text="📁 Select Folder")
        
        self.center_frame = LabelFrame(self.main_frame, text="Files to Process", padx=5, pady=5)
        self.file_listbox = FileListbox(self.center_frame)  # <-- замена старого listbox
        
        self.btn_frame = Frame(self.center_frame)
        self.add_file_btn = Button(self.btn_frame, text="➕ Add File", bg="#90EE90", padx=10)
        self.remove_file_btn = Button(self.btn_frame, text="❌ Remove Selected", bg="#FFB6C1", padx=10)
        self.clear_all_btn = Button(self.btn_frame, text="🗑 Clear All", bg="#FFD700", padx=10)
        
        self.bottom_frame = Frame(self.main_frame, bd=2, padx=5, pady=5)
        self.move_btn = Button(self.bottom_frame, text="📂 Move to Bin",
                               bg="#4CAF50", fg="black", font=("Arial", 10, "bold"))
    
    def _layout_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.top_frame.grid_columnconfigure(1, weight=1)
        Label(self.top_frame, text="Selected Folder:").grid(row=0, column=0, sticky="w", padx=5)
        self.path_label.grid(row=0, column=1, sticky="ew", padx=5)
        self.select_folder_btn.grid(row=0, column=2, padx=5)
        
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_rowconfigure(0, weight=1)
        
        self.file_listbox.grid(row=0, column=0, sticky="nsew", columnspan=2)
        self.file_listbox.grid_columnconfigure(0, weight=1)
        self.file_listbox.grid_rowconfigure(0, weight=1)
        
        self.btn_frame.grid(row=1, column=0, columnspan=2, pady=10)
        self.add_file_btn.pack(side=LEFT, padx=5)
        self.remove_file_btn.pack(side=LEFT, padx=5)
        self.clear_all_btn.pack(side=LEFT, padx=5)
        
        self.bottom_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.move_btn.pack(expand=True, fill='x', padx=20)
    
    def _bind_events(self):
        self.select_folder_btn.config(command=self._on_select_folder)
        self.add_file_btn.config(command=self._on_add_files)
        self.remove_file_btn.config(command=self._on_remove_selected)
        self.clear_all_btn.config(command=self._on_clear_all)
        self.move_btn.config(command=self._on_move_to_bin)
    
    def _on_select_folder(self):
        if self.controller:
            self.controller.select_folder()
    
    def _on_add_files(self):
        if self.controller:
            self.controller.add_files()
    
    def _on_remove_selected(self):
        if self.controller:
            self.controller.remove_selected()
    
    def _on_clear_all(self):
        if self.controller:
            self.controller.clear_all()
    
    def _on_move_to_bin(self):
        if self.controller:
            self.controller.move_to_bin()
    
    def update_file_list(self, file_names):
        self.file_listbox.update_items(file_names)
    
    def update_folder_path(self, folder_path):
        if folder_path:
            last_path = os.path.basename(folder_path)
            self.path_label.config(text=f'{last_path} ({folder_path})')
        else:
            self.path_label.config(text='Empty')
    
    def show_message(self, title, message, msg_type="info"):
        if msg_type == "info":
            messagebox.showinfo(title, message)
        elif msg_type == "warning":
            messagebox.showwarning(title, message)
        elif msg_type == "error":
            messagebox.showerror(title, message)
        elif msg_type == "yesno":
            return messagebox.askyesno(title, message)
    
    def get_selected_index(self):
        return self.file_listbox.get_selected_index()
    
    def ask_for_folder(self):
        return filedialog.askdirectory(title='Select Folder')
    
    def ask_for_files(self):
        return filedialog.askopenfilenames(title='Select Files')
    
    def ask_confirmation(self, title, message):
        return messagebox.askyesno(title, message, icon='question')