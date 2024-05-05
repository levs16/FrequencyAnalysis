import matplotlib.pyplot as plt
from collections import Counter
import sys

def perform_frequency_analysis(file_path):
    try:
        # Read the content of the file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Count the frequency of each character
        frequencies = Counter(content)
        
        # Filter out non-alphabetic characters and convert keys to lowercase
        filtered_frequencies = {char.lower(): count for char, count in frequencies.items() if char.isalpha()}
        
        # Sort the dictionary by keys (alphabetically)
        sorted_frequencies = dict(sorted(filtered_frequencies.items()))
        
        return sorted_frequencies
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def plot_frequencies(frequencies):
    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(frequencies.keys(), frequencies.values(), color="blue")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.title("Character Frequency Analysis")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    frequencies = perform_frequency_analysis(file_path)
    plot_frequencies(frequencies)
