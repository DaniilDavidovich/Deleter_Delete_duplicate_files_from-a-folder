from send2trash import send2trash

def move_to_trash(file_paths: list[str]) -> int:
    success_count = 0
    for path in file_paths:
        try:
            send2trash(path)
            success_count += 1
        except Exception as e:
            print(f"Failed to move {path}: {e}")
    return success_count