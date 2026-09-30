# Guess the Number Game

An interactive, terminal-based algorithmic game built in Python where players attempt to guess a randomly selected integer within a constrained number of attempts using real-time feedback clues.

## Project Overview
This project applies fundamental programming logic, control flow, and pseudo-random number generation to implement a console-based game lifecycle. The program chooses a target integer between 1 and 100, grants the player 5 attempts, and dynamically provides evaluation cues ("Too low" or "Too high") to assist decision-making.

## Features
* **Random Target Generation:** Semi-random calculation ensures a unique solution every runtime instance.
* **Algorithmic Hint Logic:** Evaluates inputs programmatically to return direct relative positioning indicators.
* **State & Cycle Bounds:** Implements strict tracking bounds to terminate execution upon exhausting the attempt limit.

## Technologies & Tools Used
* **Language:** Python 3.14.7
* **Core Libraries:** `random` (Standard library module for random integer generation)
* **Environment:** Command Line Interface (CLI) / Terminal

## Steps to Install & Run the Project

### 1. Environment Setup
This project runs entirely on standard Python runtimes. Ensure you have Python 3 installed on your machine.
* To check if Python is installed, open your command prompt/terminal and run:
  ```bash
  python --version
  ```

### 2. Dependency Installation
* **No external third-party packages are required.** The project strictly utilizes Python’s built-in `random` module. No `pip install` commands are needed.

### 3. Configuration
* No environment variables, configuration keys, or external database structures are required to initialize this application.

### 4. Running the Application
1. Open your terminal or command prompt.
2. Navigate directly to the root directory where the script file is saved:
   ```bash
   cd /path/to/your/project-directory
   ```
3. Run the script using the python command:
   ```bash
   python main.py
   ```

## Instructions for Testing
You can manually verify all execution flows with these four baseline test criteria in your terminal:
* **Lower Bound Verification:** Input `1`. The program must output: `"Too low!!!! Try again!!!"`.
* **Upper Bound Verification:** Input `100`. The program must output: `"Too high!!! Try again!!!"`.
* **Positive Success Flow:** Follow the relative cues to hit the hidden integer. The terminal should print `"Congratulations! You guessed the number!"` and exit cleanly.
* **Negative Failure Flow:** Provide 5 deliberately incorrect inputs. The application must break the execution cycle, log `"Oops! You ran out of attempts. Better luck next time!"`, and terminate safely.


