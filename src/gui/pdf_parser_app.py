"""
===================================================
    PDFParser - GUI Entry Point
===================================================

This script serves as the gui entry point for the PDFParser application.
It defines the graphical user interface (GUI).

Features:
- Imports a PDF file and extracts text and images.
- Exports extracted data as TXT and PNG files.
- Handles errors and logs them if encountered.
- Launches the graphical interface for user interaction.

Usage:
- Run this script to launch the application:
    python main.py
-- You may only want to run it in command line, in this case call main() in the "__name__" var --

Dependencies:
- Ensure all required modules are installed using:
    pip install -r requirements.txt

Author: Clement
Date project started: 06/02/2025
===================================================
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler

class PDFParserApp:
    def __init__(self):
        """
        Initializes the main application window with single and multi-file parsing options.
        """
        self.window = tk.Tk()
        self.window.title("PDF Parser Application")
        self.window.geometry("800x600")

        # Left Frame (For file selection)
        self.left_frame = tk.Frame(self.window, width=300, bg="#f0f0f0")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Right Frame (For export options)
        self.right_frame = tk.Frame(self.window, bg="#ffffff")
        self.right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Left Frame Widgets (File Selection)
        self.single_file_button = tk.Button(
            self.left_frame, text="Select a PDF file (Replace)", 
            command=self.open_single_pdf, bg="#4CAF50", fg="white", 
            font=("Arial", 12)
        )
        self.single_file_button.pack(pady=10, padx=20, fill=tk.X)

        self.multi_file_button = tk.Button(
            self.left_frame, text="Select multiple PDFs", 
            command=self.open_multiple_pdfs, bg="#FF9800", fg="white", 
            font=("Arial", 12)
        )
        self.multi_file_button.pack(pady=10, padx=20, fill=tk.X)

        self.clear_button = tk.Button(
            self.left_frame, text="Clear loaded files", 
            command=self.clear_previous_data, bg="#D32F2F", fg="white", 
            font=("Arial", 12)
        )
        self.clear_button.pack(pady=10, padx=20, fill=tk.X)

        # Right Frame Widgets (Export)
        self.export_images_button = tk.Button(
            self.right_frame, text="Export images to PNG", 
            command=self.export_images, bg="#2196F3", fg="white", 
            font=("Arial", 12)
        )
        self.export_text_button = tk.Button(
            self.right_frame, text="Export to TXT", 
            command=self.export_text, bg="#FF5722", fg="white", 
            font=("Arial", 12)
        )

        # Core Components
        self.import_manager = ImportManager()
        self.export_manager = ExportManager()
        self.error_handler = ErrorHandler()
        self.pdf_parsers = []

        self.export_images_button.pack_forget()
        self.export_text_button.pack_forget()
        self.clear_button.pack_forget()

    def run(self):
        """ Starts the main application loop. """
        self.window.mainloop()

    def clear_previous_data(self):
        """ Clears previously parsed data before loading a new file. """
        self.pdf_parsers = []
        self.export_manager.text_outputs = []
        self.export_manager.image_outputs = []

        self.export_images_button.pack_forget()
        self.export_text_button.pack_forget()
        self.clear_button.pack_forget()

        messagebox.showinfo("Info", "Cleared all loaded files.")

    def open_single_pdf(self):
        """ Opens a single PDF file and replaces any previously loaded file. """
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.clear_previous_data()
            self.process_pdf(file_path)

    def open_multiple_pdfs(self):
        """ Opens multiple PDF files and adds them to the list without replacing previous files. """
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if file_paths:
            for file_path in file_paths:
                self.process_pdf(file_path)

    def process_pdf(self, file_path):
        """ Processes a selected PDF file, adds it to the list, and makes it ready for export. """
        try:
            pdf_file = self.import_manager.import_file(file_path)
            pdf_parser = PDFParser(pdf_file)
            self.pdf_parsers.append(pdf_parser)

            self.export_images_button.pack(pady=10, padx=20)
            self.export_text_button.pack(pady=10, padx=20)
            self.clear_button.pack(pady=10, padx=20)

        except Exception as e:
            self.error_handler.log_error(str(e))
            messagebox.showerror("Error", f"Failed to load PDF: {e}")

    def export_text(self):
        """ Exports all parsed text outputs into a single file. """
        try:
            output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_path and self.pdf_parsers:
                with open(output_path, "w", encoding="utf-8") as file:
                    for pdf_parser in self.pdf_parsers:
                        file.write(pdf_parser.parse_text().content + "\n\n")

        except Exception as e:
            self.error_handler.log_error(str(e))
            messagebox.showerror("Error", f"Failed to export text: {e}")

    def export_images(self):
        """ Exports all parsed images into a directory. """
        try:
            output_dir = filedialog.askdirectory()
            if output_dir and self.pdf_parsers:
                for pdf_parser in self.pdf_parsers:
                    self.export_manager.image_outputs.append(pdf_parser.parse_images())

                self.export_manager.export_images(output_dir)
        except Exception as e:
            self.error_handler.log_error(str(e))
            messagebox.showerror("Error", f"Failed to export images: {e}")