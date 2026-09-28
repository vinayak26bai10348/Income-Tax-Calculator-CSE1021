print("Indian Income Tax Calculator")
print("New Tax Regime: FY 2025-26 (AY 2026-27)")
print("For a resident salaried individual")
print()

try:
    annual_salary = float(input("Enter your gross annual salary in rupees: "))

    if annual_salary < 0:
        print("Salary cannot be negative.")
    else:
        # Deduct the standard deduction available to salaried employees.
        standard_deduction = min(annual_salary, 75000)
        taxable_income = annual_salary - standard_deduction

        # Calculate tax progressively: each rate applies only to its slab.
        tax = 0

        if taxable_income > 400000:
            tax += (min(taxable_income, 800000) - 400000) * 0.05

        if taxable_income > 800000:
            tax += (min(taxable_income, 1200000) - 800000) * 0.10

        if taxable_income > 1200000:
            tax += (min(taxable_income, 1600000) - 1200000) * 0.15

        if taxable_income > 1600000:
            tax += (min(taxable_income, 2000000) - 1600000) * 0.20

        if taxable_income > 2000000:
            tax += (min(taxable_income, 2400000) - 2000000) * 0.25

        if taxable_income > 2400000:
            tax += (taxable_income - 2400000) * 0.30

        # Apply Section 87A rebate or marginal relief for eligible residents.
        if taxable_income <= 1200000:
            tax = 0
        elif tax > taxable_income - 1200000:
            tax = taxable_income - 1200000

        # Add 4% Health and Education Cess to the tax after relief.
        cess = tax * 0.04
        total_tax = tax + cess

        print()
        print(f"Gross annual salary: ₹{annual_salary:,.2f}")
        print(f"Standard deduction: ₹{standard_deduction:,.2f}")
        print(f"Taxable income: ₹{taxable_income:,.2f}")
        print(f"Estimated tax including cess: ₹{total_tax:,.2f}")
        print(f"Salary after estimated tax: ₹{annual_salary - total_tax:,.2f}")

except ValueError:
    print("Please enter a valid number for the salary.")
import tkinter as tk
from tkinter import messagebox


def calculate_tax():
    try:
        annual_salary = float(salary_entry.get())

        if annual_salary < 0:
            messagebox.showerror("Invalid Input", "Salary cannot be negative.")
            return

        # Standard deduction under new tax regime
        standard_deduction = min(annual_salary, 75000)

        taxable_income = annual_salary - standard_deduction

        # Calculate tax
        tax = 0

        if taxable_income > 400000:
            tax += (min(taxable_income, 800000) - 400000) * 0.05

        if taxable_income > 800000:
            tax += (min(taxable_income, 1200000) - 800000) * 0.10

        if taxable_income > 1200000:
            tax += (min(taxable_income, 1600000) - 1200000) * 0.15

        if taxable_income > 1600000:
            tax += (min(taxable_income, 2000000) - 1600000) * 0.20

        if taxable_income > 2000000:
            tax += (min(taxable_income, 2400000) - 2000000) * 0.25

        if taxable_income > 2400000:
            tax += (taxable_income - 2400000) * 0.30

        # Rebate / marginal relief
        if taxable_income <= 1200000:
            tax = 0
        elif tax > taxable_income - 1200000:
            tax = taxable_income - 1200000

        # Health and Education Cess
        cess = tax * 0.04
        total_tax = tax + cess

        salary_after_tax = annual_salary - total_tax

        # Display result
        result_text.set(
            f"Gross Annual Salary : ₹{annual_salary:,.2f}\n"
            f"Standard Deduction  : ₹{standard_deduction:,.2f}\n"
            f"Taxable Income      : ₹{taxable_income:,.2f}\n"
            f"Estimated Tax       : ₹{total_tax:,.2f}\n"
            f"Salary After Tax    : ₹{salary_after_tax:,.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid salary amount."
        )


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Indian Income Tax Calculator")
root.geometry("550x500")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Indian Income Tax Calculator",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    root,
    text="New Tax Regime - FY 2025-26 (AY 2026-27)",
    font=("Arial", 12)
)
subtitle_label.pack()

info_label = tk.Label(
    root,
    text="For a Resident Salaried Individual",
    font=("Arial", 11)
)
info_label.pack(pady=5)

# Salary label
salary_label = tk.Label(
    root,
    text="Enter Gross Annual Salary (₹):",
    font=("Arial", 12)
)
salary_label.pack(pady=(25, 5))

# Salary input
salary_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 13),
    justify="center"
)
salary_entry.pack()

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate Tax",
    font=("Arial", 12, "bold"),
    command=calculate_tax
)
calculate_button.pack(pady=20)

# Result heading
result_heading = tk.Label(
    root,
    text="Tax Calculation Result",
    font=("Arial", 15, "bold")
)
result_heading.pack(pady=5)

# Result
result_text = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=10)

# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 11),
    command=root.destroy
)
exit_button.pack(pady=10)

# Start GUI
root.mainloop()