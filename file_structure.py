from pathlib import Path

# Folders you want to ignore
EXCLUDE_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "env", "venv"}

def generate_folder_structure(dir_path: str | Path, indent: str = "") -> None:
    path = Path(dir_path)
    
    if not path.exists():
        print(f"Error: The path '{dir_path}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: The path '{dir_path}' is not a directory.")
        return
        
    if indent == "":
        print(f"📁 {path.name}/")
        
    try:
        items = [
            x for x in path.iterdir() 
            if not (x.is_dir() and x.name in EXCLUDE_DIRS)
        ]
        items.sort(key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(f"{indent}└── [Permission Denied]")
        return

    for index, item in enumerate(items):
        is_last = (index == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        if item.is_dir():
            print(f"{indent}{connector}📁 {item.name}/")
            next_indent = indent + ("    " if is_last else "│   ")
            generate_folder_structure(item, next_indent)
        else:
            print(f"{indent}{connector}📄 {item.name}")

if __name__ == "__main__":
    target_directory = input("Enter Directory Path: ")
    print(f"Generating structure for: {target_directory}\n")
    generate_folder_structure(target_directory)
