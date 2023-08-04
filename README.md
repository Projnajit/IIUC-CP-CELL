# IIUC CP Cell Django Project

Welcome to the IIUC CP Cell Django Project! This repository contains the source code and related files for a web application developed using Django for the Competitive Programming (CP) Cell at IIUC (International Islamic University Chittagong).

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The IIUC CP Cell Django Project aims to provide a platform for CP enthusiasts at IIUC to practice and enhance their programming skills. This web application offers various features that facilitate learning, practicing, and participating in programming competitions.

## Features

1. **User Authentication**: Users can create accounts, log in, and manage their profiles.
2. **Problem Repository**: Browse a collection of programming problems with different difficulty levels.
3. **Practice Arena**: Solve problems in an interactive coding environment online.
4. **Contest Management**: Participate in coding contests and view real-time standings.
5. **Editorial Section**: Access editorials and solutions for problems.
6. **User Rankings**: Track and compare your progress with other CP enthusiasts.

## Installation

To set up and run the IIUC CP Cell Django Project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Projnajit/IIUC-CP-CELL.git
   ```

2. Navigate to the project directory:

   ```bash
   cd IIUC-CP-Cell
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

Once the application is set up, you can use it to:

- Create an account or log in.
- Explore the problem repository and practice solving problems.
- Participate in coding contests and view contest standings.
- Access editorial solutions for problems.
- Track your progress and rankings on the platform.



Thank you for your interest in the IIUC CP Cell Django Project. If you have any questions or need assistance, please don't hesitate to [contact us](mailto:projnajit@gmail.com). Happy coding!
