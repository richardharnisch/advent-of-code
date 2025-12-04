# advent-of-code

Richard's solutions for advent of code.

see <https://adventofcode.com/>

## run.sh

This script automates the setup and execution of Advent of Code challenges.

It supports three main operations: running scripts for a specific day, pushing changes to GitHub, and running all scripts. All commands run in the directory of the current year automatically. Running scripts assumes a usable python environment at `.venv` with an interpreter at `.venv/bin/python3`. I use `uv` for this, see the `pyproject.toml` for details. 

### Usage:
`./run.sh <day_number>`: Creates the directory and files for the specified day if they do not exist, or executes any Python scripts found in the directory if it does exist.

`./run.sh push`: Commits all changes with a message containing the current day number and pushes to GitHub.

`./run.sh all`: Executes all Python scripts in all day directories, using corresponding input files.

`./run.sh --year [year] [command]`: Executes [command] in the specified [year] directory instead of the current one. Creates the year directory if not present.

### Arguments:
`<day_number>`: The day number for which to create the directory and files, or to execute the scripts.

`push`: Commits and pushes all changes to GitHub with a commit message containing the current day number.

`all`: Executes all Python scripts in all day directories, using corresponding input files.

### Examples:
`./run.sh 1` - Sets up or runs the scripts for day 1.

`./run.sh push` - Commits and pushes all changes to GitHub.

`./run.sh all` - Runs all scripts for all days.
