Project 4: Employee Payroll System - README
Overview
The Employee Payroll System is a comprehensive command-line application developed in Python as part of the Machine Learning September 2026 training curriculum minor projects. It automates personnel record management and salary calculations, allowing administrators to manage employee data, compute wages based on hours or salary structures, generate itemized payslips, and persist records across sessions.

Main Features Implemented
Add Employees: Register new employees (Full-Time, Part-Time, or Contract) with unique IDs, names, and designation details.

Calculate Salary: Automatically compute net salaries factoring in base pay, overtime, bonuses, taxes, and deductions.

Generate Payslip: Produce detailed, formatted electronic payslips for individual employees.

Search Employees: Quickly retrieve and display employee records and payroll histories by ID or name.

Data Persistence: Automatically save and load employee and payroll data using persistent storage files to maintain data integrity.

Classes Used
Following object-oriented programming (OOP) principles, the project implements the following core classes:

Employee (Abstract/Base Class): Encapsulates core attributes (emp_id, name, department) and defines abstract interfaces for salary computation.

FullTimeEmployee (Derived Class): Inherits from Employee and implements fixed-salary calculations with standard benefits and deductions.

PartTimeEmployee (Derived Class): Inherits from Employee and implements hourly-wage calculations based on hours worked.

PayrollSystem (Management Class): Orchestrates the employee database, handles user interactions, manages file I/O operations, and coordinates menu navigation.

How the Project Works
Initialization: Upon launching, the application reads stored data files to load existing employee records into memory.

Menu-Driven Interface: The program provides an interactive console menu allowing administrators to choose tasks such as adding personnel, calculating payroll, generating payslips, or searching records.

Validation & Exception Handling: User inputs are strictly validated to prevent crashes caused by invalid numeric entries, negative values, or duplicate employee IDs.

Persistence: Every addition or update modifies internal collections and saves the updated state to persistent files.

How to Run the Project
Prerequisites
Python 3.8 or higher installed on your system.

Standard Python libraries (no external dependencies required).

Execution Steps
Clone the repository or download all project files into a local directory.

Open your terminal or command prompt and navigate to the project root directory:

Bash
cd employee-payroll-system
Run the main application script:

Bash
python main.py
Follow the on-screen prompts in the interactive console to operate the system.
