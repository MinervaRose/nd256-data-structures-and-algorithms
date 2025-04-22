import os
from typing import List

def find_files(suffix: str, path: str) -> List[str]:
    """
    Recursively finds all files under `path` that end with the given `suffix`.

    Parameters:
    -----------
    suffix : str
        File name suffix to match (e.g., '.c')
    path : str
        Starting directory path

    Returns:
    --------
    List[str]
        Full paths to matching files
    """
    matching_files = []

    if not os.path.exists(path):
        return matching_files

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    # If it's a directory, recurse into it
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        matching_files += find_files(suffix, full_path)

    return matching_files

if __name__ == "__main__":
    # Test Case 1: Provided directory structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output (order may vary):
    # ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Empty directory
    print("Test Case 2: Empty directory")
    os.makedirs("emptydir", exist_ok=True)
    print(find_files(".c", "emptydir"))  # Expected: []

    # Test Case 3: Non-existent path
    print("Test Case 3: Invalid path")
    print(find_files(".c", "nonexistent"))  # Expected: []
