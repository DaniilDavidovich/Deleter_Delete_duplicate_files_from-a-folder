
from tkinter import Frame, Listbox, Scrollbar, END

class FileListbox(Frame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master)
        
        listbox_kwargs = {
            'font': ("Consolas", 10),
            'selectmode': "single",
            'relief': "sunken",
            'bg': "#f8f8f8"
        }
        listbox_kwargs.update(kwargs)
        
        self.listbox = Listbox(self, **listbox_kwargs)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def update_items(self, items):
        self.listbox.delete(0, END)
        for idx, item in enumerate(items, 1):
            self.listbox.insert(END, f"{idx}. {item}")
    
    def get_selected_index(self):
        selection = self.listbox.curselection()
        return selection[0] if selection else None
    
    def clear(self):
        self.listbox.delete(0, END)
    
    def get_items(self):
        return [self.listbox.get(i) for i in range(self.listbox.size())]