import os
import sys

def test_files_exists():
    filepath = "app.py"
    assert os.path.exists(filepath), f"File not found: {filepath}"
    filepath = "styles.css"
    assert os.path.exists(filepath), f"File not found: {filepath}"

if __name__ == "__main__":
    try:
        test_files_exists()
        print("Success: Files exist!")
        sys.exit(0)
    except AssertionError as e:
        print(f"Failed: {e}")
        sys.exit(1)