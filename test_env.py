#!/usr/bin/env python3
"""
Print current Python path information.
"""

import sys

def main():
    """Print Python path and version."""
    print("Python executable:", sys.executable)
    print("\nPython path (sys.path):")
    for i, path in enumerate(sys.path):
        print(f"{i:3d}: {path}")

if __name__ == "__main__":
    main()
