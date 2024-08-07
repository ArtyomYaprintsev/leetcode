#!/bin/bash

SOLUTIONS_DIR="solutions"
TEMPLATES_DIR="templates"

generate_file_by_template() {
    local dir="$1"
    local file="$2"

    content=$(<"$TEMPLATES_DIR/$file")
    echo "$content" > "$dir/$file"
}

# Check if a name argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 'name'"
    exit 1
fi

# Extract and validate the name argument
name="$1"
regex='^[0-9]+\.\s[a-zA-Z0-9 -_.,]+$'

if [[ ! "$name" =~ $regex ]]; then
    echo "Error: Provided name does not match the required pattern."
    exit 1
fi

# Format the name
formatted_name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr -d '.' | tr ' ' '-')

# Solution base dir
solution_dir="$SOLUTIONS_DIR/$formatted_name"

# Create a new git branch
git checkout -b "$formatted_name"

# Create a new folder with the formatted name
mkdir "$solution_dir"

for file in '__init__.py' 'solution.py' 'test_solution.py';
do
    generate_file_by_template $solution_dir $file
done

# # Add the new file to git and commit
git add "$solution_dir"
git commit -m "Init solution"

echo "Branch, folder, and related files created successfully."
