#!/usr/bin/env python3
import sys

def main():
    """
    42 London Discovery Piscine - Final Combined Script
    Demonstrates: CLI Handling, List Comprehensions, and Input Validation.
    """
    
    # 1. Accessing Command Line Arguments (Module 5 Logic)
    # sys.argv[0] is the script name; the rest are user inputs.
    args = sys.argv[1:]
    
    if not args:
        print("Usage: ./discovery_final_tool.py <number1> <number2> ...")
        print("Example: ./discovery_final_tool.py 2 8 9 48")
        return

    try:
        # 2. Data Transformation (Module 4 & 5 Logic)
        # Convert string arguments to integers and filter out small values
        original_numbers = [int(arg) for arg in args]
        
        # List Comprehension: Add 2 to any number greater than 5
        transformed = [x + 2 for x in original_numbers if x > 5]
        
        # 3. Utilizing Sets for Unique Values
        unique_results = sorted(list(set(transformed)))

        # 4. Professional Output (Module 4 Formatting)
        print("-" * 30)
        print(f"Original Input:  {original_numbers}")
        print(f"Filtered (>5) + 2: {transformed}")
        print(f"Unique Sorted:    {unique_results}")
        print("-" * 30)

    except ValueError:
        print("Error: Please provide only whole numbers as arguments.")
        print("Note: Shell special characters (!, ?) must be quoted or escaped.")

if __name__ == "__main__":
    main()
