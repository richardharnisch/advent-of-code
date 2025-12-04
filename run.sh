#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <day_number> | push | all"
    exit 1
fi

if [[ "$1" == "--year" ]]; then
    YEAR_DIR="$2"
    shift 2
    if [ ! -d "$YEAR_DIR" ]; then
        mkdir "$YEAR_DIR"
        echo "Created directory $YEAR_DIR"
    fi
else
    YEAR_DIR=$(date +%Y)
fi
cd "$YEAR_DIR"
DAY_DIR="day$1"

if [ "$1" == "push" ]; then
    current_day=$(date +%d)
    git add .
    git commit -m "day $current_day"
    git push
    echo "Pushed changes to GitHub with commit message 'Commit for day $current_day'"
elif [ "$1" == "all" ]; then
    for dir in day*/; do
        if [ -d "$dir" ]; then
            cd "$dir"
            for py_file in *.py; do
                if [ -f "$py_file" ]; then
                    input_file="${py_file%.py}.in"
                    output_file="${py_file%.py}.out"
                    if [ -f "$input_file" ]; then
                        ../../.venv/bin/python3 "$py_file" < "$input_file" > "$output_file"
                        echo "Executed $py_file in $dir with input from $input_file and output to $output_file"
                    else
                        echo "Input file $input_file not found for $py_file in $dir"
                    fi
                fi
            done
            cd ..
        fi
    done
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    # Create the directory and files if they do not exist
    if [ ! -d "$DAY_DIR" ]; then
        mkdir "$DAY_DIR"
        echo "Created directory $DAY_DIR"
        
        # Create the files
        cp ../template.py "$DAY_DIR/1.py"
        cp ../template.py "$DAY_DIR/2.py"
        touch "$DAY_DIR/1.in" "$DAY_DIR/1.out"
        touch "$DAY_DIR/2.in" "$DAY_DIR/2.out"
        echo "Created files 1.py, 1.in, 1.out, 2.py, 2.in, 2.out in $DAY_DIR"
    else
        cd "$DAY_DIR"

        # Check for any Python files and run them
        for py_file in *.py; do
            if [ -f "$py_file" ]; then
                input_file="${py_file%.py}.in"
                output_file="${py_file%.py}.out"
                if [ -f "$input_file" ]; then
                    ../../.venv/bin/python "$py_file" < "$input_file" > "$output_file"
                    echo "Executed $py_file with input from $input_file and output to $output_file"
                else
                    echo "Input file $input_file not found for $py_file"
                fi
            fi
        done
    fi
else
    echo "Invalid argument: $1"
    echo "Usage: $0 <day_number> | push | all"
    exit 1
fi