import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font

import openai

from conversion import load_api_key, generate_gherkin_syntax, read_cypress_test

# Load API Key
load_api_key()
client = openai.OpenAI(api_key=load_api_key())


# Process directory and save converted files
def process_directory(source_dir, output_dir, log_widget, preview_widget):
    """Recursively process .cy.ts files from source_dir and save Gherkin syntax to output_dir."""
    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", "Invalid source directory!")
        return

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    log_widget.insert(tk.END, "Processing started...\n")
    log_widget.update_idletasks()

    for root_dir, _, files in os.walk(source_dir):
        for file_name in files:
            if file_name.endswith(".cy.ts"):
                file_path = os.path.join(root_dir, file_name)
                test_content = read_cypress_test(file_path)
                gherkin_syntax = generate_gherkin_syntax(test_content)

                if gherkin_syntax:
                    output_file = os.path.join(output_dir, file_name.replace(".cy.ts", "_gherkin.txt"))
                    with open(output_file, "w", encoding="utf-8") as file:
                        file.write(gherkin_syntax)

                    log_widget.insert(tk.END, f"Converted: {file_name} -> {output_file}\n")
                    log_widget.update_idletasks()

                    # Update preview with last converted file
                    preview_widget.delete(1.0, tk.END)
                    preview_widget.insert(tk.END, gherkin_syntax)

    log_widget.insert(tk.END, "Processing completed!\n")
    log_widget.update_idletasks()
    messagebox.showinfo("Success", f"Conversion complete! Files saved in:\n{output_dir}")


# Start processing in a separate thread
def start_conversion():
    source_dir = source_dir_entry.get()
    output_dir = output_dir_entry.get()

    if not source_dir or not output_dir:
        messagebox.showerror("Error", "Please select both source and destination directories.")
        return

    # Run process in a separate thread to avoid UI freeze
    threading.Thread(target=process_directory, args=(source_dir, output_dir, log_output, preview_text), daemon=True).start()


# UI Setup
root = tk.Tk()
root.title("Cypress to Gherkin Converter")
root.geometry("1024x1200")
root.configure(bg="white")

# Define monospaced font
monospace_font = font.Font(family="Courier", size=10)

# Source Directory Selection
tk.Label(root, text="Select Source Directory:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
source_dir_entry = tk.Entry(root, width=50)
source_dir_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", fg="black", command=lambda: source_dir_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2, padx=5, pady=5)

# Destination Directory Selection
tk.Label(root, text="Select Destination Directory:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", fg="black", command=lambda: output_dir_entry.insert(0, filedialog.askdirectory())).grid(row=1, column=2, padx=5, pady=5)

# Buttons
tk.Button(root, text="Start Conversion", fg="black", command=start_conversion).grid(row=2, column=1, pady=10)
tk.Button(root, text="Exit", fg="black", command=root.quit).grid(row=2, column=2, pady=10)

# Log Output with Monospaced Font
tk.Label(root, text="Process Log:", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky="w")
log_output = scrolledtext.ScrolledText(root, width=120, height=10, wrap=tk.WORD, font=monospace_font)
log_output.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Preview Window with Monospaced Font
tk.Label(root, text="Gherkin Output Preview:", bg="white").grid(row=5, column=0, padx=5, pady=5, sticky="w")
preview_text = scrolledtext.ScrolledText(root, width=120, height=45, wrap=tk.WORD, font=monospace_font)
preview_text.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
