
# Deleter

Deleter is a simple desktop utility that helps you move duplicate files to the system Trash/Bin safely.

<img width="712" height="590" alt="image" src="https://github.com/user-attachments/assets/3cbf6303-e039-4f62-bb17-567fdec2d667" />

## Download

The latest active build for your operating system can always be found in:

**Actions → Build Installer → Last Commit**

Open the repository page, go to the **Actions** tab, select **Build Installer**, and download the artifact from the latest successful workflow run for our operation system.

---

## Installation

### macOS

1. Download the latest macOS build.
2. Move **Deleter.app** to the **Applications** folder.
3. Open Terminal and run:

```bash
xattr -d com.apple.quarantine /Applications/Deleter.app
```

4. Launch the application.

### Windows

1. Download the latest Windows build.
2. Run the application.
3. If Windows SmartScreen appears:
   - Click **More info**
   - Click **Run anyway**

---

## How It Works

Deleter helps you remove duplicate files by moving them to the system Trash/Bin instead of permanently deleting them.

### Step 1 — Select Folder

Click **Select Folder** and choose the folder where Deleter will search for matching filenames.

The selected folder becomes the search location. Deleter does not automatically detect duplicate files and only searches for files that match the filenames you manually add to the list.

### Step 2 — Add Files to the List

Click **Add File** and add one or more files that will be used as search references.

For every file added, Deleter searches the selected folder for files with the same filename.

Duplicate matching is performed by filename only. File content, size, hashes, and metadata are not compared.

All matching files found in the selected folder will be added to the processing list.

### Step 3 — Manage the List

Use the list management buttons:

- **Remove Selected** — removes the currently selected file from the list.
- **Clear All** — removes all files from the list.

These actions only affect the list inside the application and do not delete any files.

### Step 4 — Move Files to Bin

After verifying the list, click:

**Move to Bin**

All files currently in the list will be moved to the operating system Trash/Bin.

---

## Typical Workflow

1. Click **Select Folder**.
2. Choose the folder containing duplicates.
3. Click **Add File** and add all duplicate files you want to remove.
4. Review the list.
5. Use **Remove Selected** or **Clear All** if needed.
6. Click **Move to Bin**.

---

## Important Notes

- Deleter does not automatically scan your computer for duplicate files.
- Files must be manually added using **Add File**.
- The selected folder is searched only for filenames that match the files you added.
- Duplicate detection is based on filename only.
- File contents, checksums, file sizes, and metadata are not compared.

---

## Safety

Deleter moves files to the system Trash/Bin instead of permanently deleting them, allowing recovery through the operating system if necessary.

---

## Repository

Project Name: **Deleter**
