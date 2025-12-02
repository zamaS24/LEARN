import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.file_path = ''
        
        # create file selector button
        self.file_btn = tk.Button(master, text="Select File", command=self.select_file)
        self.file_btn.pack()
        
        # create float input field
        self.float_label = tk.Label(master, text="MinSup:")
        self.float_label.pack()
        self.float_entry = tk.Entry(master)
        self.float_entry.pack()
        
        # create button to display file contents
        self.display_btn = tk.Button(master, text="Apriori", command=self.display_file_contents)
        self.display_btn.pack()
        
        # create text area to display file contents
        self.text_area = tk.Text(master)
        self.text_area.pack()
        
    def select_file(self):
        # open file selector dialog
        self.file_path = filedialog.askopenfilename()
        
    def display_file_contents(self):
        # read file contents and display in text area
        try:
            pass
            print('file path: ', self.file_path)
        except Exception as e:
            print(e)
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, "Error: " + str(e))

    
root = tk.Tk()
app = App(root)
root.mainloop()
































































