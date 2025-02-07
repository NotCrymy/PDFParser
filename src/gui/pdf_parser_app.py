import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler

class PDFParserApp:
    def __init__(self):
        """
        Initializes the main application window with a split layout.
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
        self.select_button = tk.Button(
            self.left_frame, text="Select your PDF file", 
            command=self.open_pdf, bg="#4CAF50", fg="white", 
            font=("Arial", 12)
        )
        self.select_button.pack(pady=20, padx=20, fill=tk.X)

        # Right Frame Widgets (Initially hidden export buttons)
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

        # Initially hide export buttons
        self.export_images_button.pack_forget()
        self.export_text_button.pack_forget()

        # Core Components
        self.import_manager = ImportManager()
        self.export_manager = ExportManager()
        self.error_handler = ErrorHandler()
        self.pdf_parser = None

    def run(self):
        """
        Starts the main application loop.
        """
        self.window.mainloop()

    def open_pdf(self):
        """
        Opens a PDF file using a file dialog and processes it.
        """
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                pdf_file = self.import_manager.import_file(file_path)
                self.pdf_parser = PDFParser(pdf_file)

                # Show export buttons after successful parsing
                self.export_images_button.pack(pady=10, padx=20)
                self.export_text_button.pack(pady=10, padx=20)

                messagebox.showinfo("Success", "PDF Loaded Successfully!")
            except Exception as e:
                self.error_handler.log_error(str(e))
                messagebox.showerror("Error", f"Failed to load PDF: {e}")

    def export_text(self):
        """
        Exports the text output to a file.
        """
        try:
            output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_path and self.pdf_parser:
                self.export_manager.text_outputs.append(self.pdf_parser.parse_text())
                self.export_manager.export_to_txt(output_path)
                messagebox.showinfo("Success", "Text exported successfully!")
        except Exception as e:
            self.error_handler.log_error(str(e))
            messagebox.showerror("Error", f"Failed to export text: {e}")

    def export_images(self):
        """
        Exports the images to a directory.
        """
        try:
            output_dir = filedialog.askdirectory()
            if output_dir and self.pdf_parser:
                self.export_manager.image_outputs.append(self.pdf_parser.parse_images())
                self.export_manager.export_images(output_dir)
                messagebox.showinfo("Success", "Images exported successfully!")
        except Exception as e:
            self.error_handler.log_error(str(e))
            messagebox.showerror("Error", f"Failed to export images: {e}")