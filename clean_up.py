from datetime import datetime
import os
import shutil


def clean_up():
    project_files: list[str] = ['.idea', 'main.py', os.path.basename(__file__), 'expressgen.bat', 'venv']
    files: list[str] = os.listdir(os.getcwd())
    dir_deleted = 0
    files_deleted = 0
    style = f"[{datetime.now().strftime('%H:%M:%S')}] -"

    for file in files:
        if file not in project_files:
            try:
                unwanted_dir_or_file = os.path.join(os.getcwd(), file)
                if os.path.isdir(unwanted_dir_or_file):
                    shutil.rmtree(unwanted_dir_or_file)
                    dir_deleted += 1
                    print(f'{style} Deleted "{unwanted_dir_or_file}"')
                else:
                    os.remove(unwanted_dir_or_file)
                    files_deleted += 1
                    print(f'{style} Deleted "{unwanted_dir_or_file}"')
            except PermissionError:
                print("Close all applications with the current folder open.")

    if dir_deleted <= 0 and files_deleted <= 0:
        print(f"{style} No files or directories were deleted")
    else:
        print(f"{style} {dir_deleted} {'directories' if dir_deleted > 1 else 'directory'} and {files_deleted} {'files' if files_deleted > 1 else 'file'} were deleted")


if __name__ == "__main__":
    clean_up()
