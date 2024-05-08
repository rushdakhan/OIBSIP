import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("500x500")
        self.root.config(bg="lightblue")
        #self.root.resizable(False, False)

        # Create variables
        self.name_input = tk.StringVar()
        self.height_input = tk.StringVar()
        self.weight_input = tk.StringVar()
        self.bmi_value = tk.StringVar()
        self.bmi_status = tk.StringVar()

        # Create GUI
        self.create_gui()

        # Initialize data storage
        self.data = pd.DataFrame(columns=["Name", "Height", "Weight", "BMI", "Status"])

    def create_gui(self):
        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)

        # Create input tab
        self.input_tab = tk.Frame(self.tabs,bg="lightblue1")
        self.tabs.add(self.input_tab, text="Input")

        # Create labels and entries
        tk.Label(self.input_tab, text="   BMI Calculator  ",font=("Segoe Script",30,"bold"),fg="blue",padx=35,pady=15,bg="lightblue1").grid(row=0, column=0,columnspan=2)
        tk.Label(self.input_tab, text="Name:",font=("Georgia",14,"bold"),padx=35,pady=15, fg="crimson",bg="lightblue1").grid(row=1, column=0)
        tk.Entry(self.input_tab, textvariable=self.name_input).grid(row=1, column=1)
        tk.Label(self.input_tab, text="Height (cm):", font=("Georgia",14,"bold"),padx=39,pady=15, fg="crimson",bg="lightblue1").grid(row=2, column=0)
        tk.Entry(self.input_tab, textvariable=self.height_input).grid(row=2, column=1)
        tk.Label(self.input_tab, text="Weight (kg):", font=("Georgia",14,"bold"),padx=39,pady=15, fg="crimson",bg="lightblue1").grid(row=3, column=0)
        tk.Entry(self.input_tab, textvariable=self.weight_input).grid(row=3, column=1)

        # Create calculate button
        tk.Button(self.input_tab, text="Calculate BMI", command=self.calc_bmi,font=("Georgia",17,"bold"),height=1,background="indianred1", fg="blue4").grid(row=4, column=0, columnspan=2)

        # Create result labels
        tk.Label(self.input_tab, text="BMI:", font=("Georgia",14,"bold"),padx=5,pady=15, fg="crimson",bg="lightblue1").grid(row=5, column=0)
        tk.Label(self.input_tab, textvariable=self.bmi_value,bg="lightblue1").grid(row=5, column=1)
        tk.Label(self.input_tab, text="Status:", font=("Georgia",14,"bold"),padx=5,pady=15, fg="crimson",bg="lightblue1").grid(row=6, column=0)
        tk.Label(self.input_tab, textvariable=self.bmi_status,bg="lightblue1").grid(row=6, column=1)

        # Create history tab
        self.history_tab = tk.Frame(self.tabs)
        self.tabs.add(self.history_tab, text="History")

        # Create history listbox
        self.history_listbox = tk.Listbox(self.history_tab)
        self.history_listbox.pack(fill="both", expand=True)

        # Create statistics tab
        self.stats_tab = tk.Frame(self.tabs)
        self.tabs.add(self.stats_tab, text="Statistics")

        # Create statistics graph
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("BMI Trend")
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("BMI")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.stats_tab)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


    def calc_bmi(self):
        try:
            name = self.name_input.get()
            height = float(self.height_input.get()) / 100 
            weight = float(self.weight_input.get())
            bmi = weight / (height ** 2)
            self.bmi_value.set(f"Your BMI is {bmi:.2f}")

            if bmi < 18.5:
                self.bmi_status.set("You Are Underweight.")
                status_color="red"
            elif 18.5 <= bmi < 24.9:
                self.bmi_status.set("You Are In Good Shape!")
            elif 24.9 <= bmi < 29.9:
                self.bmi_status.set("You Are Overweight")
            elif 29.9 <= bmi:
                self.bmi_status.set("You Are Obese.")

            # Store data
            self.data = self.data.append({"Name": name, "Height": height, "Weight": weight, "BMI": bmi, "Status": self.bmi_status.get()}, ignore_index=True)

            # Update history listbox
            self.history_listbox.insert(tk.END, f"{name}: {bmi:.2f} ({self.bmi_status.get()})")
            self.history_listbox.config(fg="coral1", font=("Times New",13,"bold"))

            # Update statistics graph
            self.ax.clear()
            self.ax.set_title("BMI Trend")
            self.ax.set_xlabel("Date")
            self.ax.set_ylabel("BMI")
            self.ax.plot(range(len(self.data)), self.data["BMI"].values)
           # self.ax.plot(self.data["BMI"].values)
            self.canvas.draw()
        except ValueError:
            messagebox.showerror("Error", "Invalid input")


    def save_data(self):
        self.data.to_csv("bmi_data.csv", index=False)


    def load_data(self):
         try:
            self.data = pd.read_csv("bmi_data.csv")
            self.data.index = range(len(self.data))
            self.history_listbox.delete(0, tk.END)
            for index, row in self.data.iterrows():
              self.history_listbox.insert(tk.END, f"{row['Name']}: {row['BMI']:.2f} ({row['Status']})")
         except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()