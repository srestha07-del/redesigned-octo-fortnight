# Project Statement: Guess the Number Game

## 1. Problem Statement
Novice programmers often struggle to implement interactive console applications that balance dynamic state tracking with responsive user feedback. This project addresses that challenge by creating a clean, lightweight, and deterministic terminal-based game environment. 

The application resolves the lack of real-time assistance in simple console loops by generating a hidden target number, tracking player attempts, and calculating relative difference bounds to guide user decision-making dynamically without heavy computational or library dependencies.

## 2. Scope of the Project
The scope of this project is strictly focused on building a text-based, single-tier console application in Python. 

### In-Scope Elements:
* Automatic generation of a random target integer within the discrete range of 1 to 100 inclusive.
* Processing user inputs via the terminal console interface.
* Enforcement of a strict operational limit of exactly 5 attempts per game loop session.
* Real-time calculation and display of directional hints ("Too high" or "Too low") after each guess.
* Clean execution termination upon reaching either a win state or an out-of-attempts loss state.

### Out-of-Scope Elements:
* Graphical User Interfaces (GUIs), web deployments, or external mobile application frameworks.
* Persistent database integrations, cloud hosting, or multi-user cross-platform synchronization.

## 3. Target Users
This application is designed for:
* **Casual Gamers:** Individuals seeking a quick, lightweight, and engaging text-based logic puzzle directly inside their terminal.
* **Academic Evaluators:** Instructors and reviewers checking for correct mastery of basic Python programming fundamentals, logical conditioning branches, loop limits, and structured clean code implementation.

## 4. High-Level Features
* **Pseudo-Random Number Generation:** Dynamically seeds and initializes a new, hidden target number for every game run to ensure absolute replayability.
* **Relative Validation Clues:** Compares inputs against the target to deliver immediate, relative direction hints to help the user refine their subsequent guesses.
* **Lifecycle State Monitor:** Tracks continuous loop iterations up to the threshold count of 5, triggering distinct win or loss terminal screen outputs safely upon cycle completion.
