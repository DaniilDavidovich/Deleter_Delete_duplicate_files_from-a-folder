import os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

# Global variables
folder_path: str = ''
file_names: list[str] = []

# ---------- Function definitions ----------
def update_file_list():
    file_listbox.delete(0, END)
    for idx, fname in enumerate(file_names, 1):
        file_listbox.insert(END, f"{idx}. {fname}")

def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory(title='Select Folder')
    if folder_path:
        last_path = os.path.basename(folder_path)
        path_label.config(text=f'{last_path} ({folder_path})')
    else:
        path_label.config(text='Empty')

def add_file_button_did_tap():
    file_path = filedialog.askopenfilename(title='Select File')
    if file_path:
        last_path = os.path.basename(file_path)
        for i in range(0,100):
            file_names.append(last_path)
        update_file_list()
        print(f"Added file: {last_path}")

def remove_selected_file():
    selection = file_listbox.curselection()
    if selection:
        index = selection[0]
        removed = file_names.pop(index)
        update_file_list()
        print(f"Removed file: {removed}")
    else:
        messagebox.showinfo("No Selection", "Please select a file to remove.")

def clear_all_files():
    if file_names:
        if messagebox.askyesno("Clear All", f"Remove all {len(file_names)} files from the list?"):
            file_names.clear()
            update_file_list()
            print("Cleared all files")
    else:
        messagebox.showinfo("Empty List", "No files to clear.")

def delete_permanently_button_did_tap():
    if not folder_path:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return
    if not file_names:
        messagebox.showwarning("No Files", "Please add files to the list.")
        return

    # Confirm with user
    confirm = messagebox.askyesno(
        "Confirm Permanent Deletion",
        f"Are you sure you want to PERMANENTLY DELETE {len(file_names)} file(s) from\n{folder_path}?\n\nThis action cannot be undone!",
        icon='warning'
    )
    if confirm:
        # Original action (just print for now)
        print(f"DELETE PERMANENTLY confirmed. Files: {file_names}")
        messagebox.showinfo("Action Simulated", "Permanent deletion simulated.\n(No actual files were deleted)")
        # Here you would add real deletion code if needed
    else:
        print("User cancelled permanent deletion.")

def move_to_bin_button_did_tap():
    if not folder_path:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return
    if not file_names:
        messagebox.showwarning("No Files", "Please add files to the list.")
        return

    confirm = messagebox.askyesno(
        "Confirm Move to Bin",
        f"Move {len(file_names)} file(s) from\n{folder_path}\nto the Recycle Bin?",
        icon='question'
    )
    if confirm:
        print(f"MOVE TO BIN confirmed. Files: {file_names}")
        messagebox.showinfo("Action Simulated", "Move to Bin simulated.\n(No actual files were moved)")
        # Here you would add real move-to-bin code if needed
    else:
        print("User cancelled move to bin.")

# ---------- GUI construction ----------
root = Tk()
root.title("Deleter")
root.geometry("600x450")
root.resizable(True, True)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Top frame
top_frame = Frame(main_frame, relief=GROOVE, bd=2, padx=5, pady=5)
top_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
top_frame.grid_columnconfigure(1, weight=1)

Label(top_frame, text="Selected Folder:").grid(row=0, column=0, sticky="w", padx=5)
path_label = Label(top_frame, text="Empty", anchor="w", relief=SUNKEN, width=40, bg="white")
path_label.grid(row=0, column=1, sticky="ew", padx=5)

select_folder_btn = Button(top_frame, text="📁 Select Folder", command=choose_folder)
select_folder_btn.grid(row=0, column=2, padx=5)

# Center frame - file list
center_frame = LabelFrame(main_frame, text="Files to Process", padx=5, pady=5)
center_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
center_frame.grid_columnconfigure(0, weight=1)
center_frame.grid_rowconfigure(0, weight=1)

list_frame = Frame(center_frame)
list_frame.grid(row=0, column=0, sticky="nsew", columnspan=2)
list_frame.grid_columnconfigure(0, weight=1)
list_frame.grid_rowconfigure(0, weight=1)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

file_listbox = Listbox(list_frame, yscrollcommand=scrollbar.set, font=("Consolas", 10),
                        selectmode=SINGLE, relief=SUNKEN, bg="#f8f8f8")
file_listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=file_listbox.yview)

# Buttons for managing files
btn_frame = Frame(center_frame)
btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

add_file_btn = Button(btn_frame, text="➕ Add File", command=add_file_button_did_tap,
                      bg="#90EE90", padx=10)
add_file_btn.pack(side=LEFT, padx=5)

remove_file_btn = Button(btn_frame, text="❌ Remove Selected", command=remove_selected_file,
                         bg="#FFB6C1", padx=10)
remove_file_btn.pack(side=LEFT, padx=5)

clear_all_btn = Button(btn_frame, text="🗑 Clear All", command=clear_all_files,
                       bg="#FFD700", padx=10)
clear_all_btn.pack(side=LEFT, padx=5)

# Bottom frame
bottom_frame = Frame(main_frame, relief=GROOVE, bd=2, padx=5, pady=5)
bottom_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)

delete_btn = Button(bottom_frame, text="💀 Delete Permanently", command=delete_permanently_button_did_tap,
                    bg="#FF4444", fg="black", font=("Arial", 10, "bold"), padx=10)
delete_btn.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

move_btn = Button(bottom_frame, text="📂 Move to Bin", command=move_to_bin_button_did_tap,
                  bg="#4CAF50", fg="black", font=("Arial", 10, "bold"), padx=10)
move_btn.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

if __name__ == '__main__':
    root.mainloop()