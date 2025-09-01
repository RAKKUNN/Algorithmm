#!/bin/bash
# Usage: test.sh <lang> <platform> <problem_dir_name>
# Example: test.sh python leetcode 1-two-sum

lang="$1"
platform="$2"
problem="$3"

if [ -z "$problem" ]; then
    echo "Usage: test.sh <lang> <platform> <problem_dir>"
    exit 1
fi

solution_dir="solutions/$lang/$platform/$problem"
cases_file="$solution_dir/cases.txt"

if [ ! -f "$cases_file" ]; then
    echo "Cases file not found: $cases_file"
    exit 1
fi

# Determine how to run the solution based on language
if [ "$lang" = "python" ]; then
    run_cmd="python $solution_dir/main.py"
elif [ "$lang" = "cpp" ]; then
    exe_file="/tmp/${platform}-${problem}.out"
    g++ -O2 -std=c++17 "$solution_dir/main.cpp" -o "$exe_file"
    if [ $? -ne 0 ]; then
        echo "Compilation failed for $solution_dir/main.cpp"
        exit 1
    fi
    run_cmd="$exe_file"
elif [ "$lang" = "go" ]; then
    exe_file="/tmp/${platform}-${problem}"
    go build -o "$exe_file" "$solution_dir/main.go"
    if [ $? -ne 0 ]; then
        echo "Go build failed for $solution_dir/main.go"
        exit 1
    fi
    run_cmd="$exe_file"
else
    echo "Unknown language: $lang"
    exit 1
fi

case_num=0
pass_count=0
fail_count=0

# Read the cases file, splitting on blank lines into input/expected pairs
cases_data=$(awk 'BEGIN{RS=""; FS="---"} {gsub(/\r/, ""); gsub(/^\n|\n$/, "", $1); gsub(/^\n|\n$/, "", $2); printf "%s\036%s\037", $1, $2}' "$cases_file")
# Remove trailing separator (if any)
cases_data="${cases_data%$'\037'}"
IFS=$'\037' read -d '' -ra blocks <<< "$cases_data"

for block in "${blocks[@]}"; do
    # Skip any empty block (safety check)
    [ -z "$block" ] && continue
    case_num=$((case_num+1))

    # Split the block into input and expected output on our separator
    IFS=$'\036' read -r input expected <<< "$block"

    # Run the solution with the input and capture the output
    output=$(printf "%b" "$input" | eval $run_cmd)

    # Normalize trailing newlines for fair comparison
    expected_trim=$(echo -ne "$expected")
    output_trim=$(echo -ne "$output")

    if [ "$output_trim" = "$expected_trim" ]; then
        echo "Case $case_num: PASS"
        pass_count=$((pass_count+1))
    else
        echo "Case $case_num: FAIL"
        echo "Input:"
        printf "%s\n" "$input"
        echo "Expected:"
        printf "%s\n" "$expected"
        echo "Output:"
        printf "%s\n" "$output"
        fail_count=$((fail_count+1))
    fi
done

total=$case_num
echo "Passed: $pass_count/$total, Failed: $fail_count/$total"
