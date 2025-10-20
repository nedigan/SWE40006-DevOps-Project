import os
import sys

def test_file_exists():
    filepath = "app.py"  # change this to whatever file you want to check
    assert os.path.exists(filepath), f"File not found: {filepath}"

if __name__ == "__main__":
    try:
        test_file_exists()
        print("✅ File exists!")
        sys.exit(0)
    except AssertionError as e:
        print(f"❌ {e}")
        sys.exit(1)