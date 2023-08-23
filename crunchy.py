import datetime

def conjoin_text(line):
    return ''.join(line.split())

def remove_punctuation(line):
    return line.replace("-", "").replace("'", "")

def filter_lines(lines, min_length, max_length):
    return [line for line in lines if min_length <= len(line) <= max_length]

def replace_special_characters(line):
    replacements = {
        "é": "e",
        "É": "E",
        "í": "i",
        "ú": "u",
        "ö": "o",
        "á": "a",
        "ó": "o",
        "û": "u",
        "ë": "e"
        # Add more characters and replacements as needed
    }
    
    for char, replacement in replacements.items():
        line = line.replace(char, replacement)
    return line

def add_chronologies(lines):
    chronologies = []
    for i in range(100):
        chronologies.append(f"{i:02}")
    for year in range(1940, 2024):
        chronologies.append(str(year))
    
    chronology_lines = []
    for line in lines:
        for chronology in chronologies:
            chronology_lines.append(f"{line}{chronology}")
            chronology_lines.append(f"{line}-{chronology}")
            reversed_chronology = chronology[::-1]
            chronology_lines.append(f"{line}{reversed_chronology}")
            chronology_lines.append(f"{line}-{reversed_chronology}")
    
    chronology_lines.extend(lines)  # Add original conjoined lines
    lowercase_lines = [line.lower() for line in lines]
    chronology_lines.extend(lowercase_lines)  # Add lowercase conjoined lines
    capitalized_lines = [line.capitalize() for line in lines]
    chronology_lines.extend(capitalized_lines)  # Add capitalized conjoined lines
    
    return chronology_lines

def leetify(line):
    leet_versions = []
    for i in range(len(line)):
        if line[i] == 'a':
            leet_versions.append(line[:i] + '@' + line[i+1:])
        if line[i] == 'i':
            leet_versions.append(line[:i] + '1' + line[i+1:])
        if line[i] == 'o':
            leet_versions.append(line[:i] + '0' + line[i+1:])
    
    leet_versions.append(line)
    
    leet_versions.extend([line.replace('a', '@', 1) for _ in range(line.count('a'))])
    leet_versions.extend([line.replace('a', '@')])
    
    leet_versions.extend([line.replace('i', '1', 1) for _ in range(line.count('i'))])
    leet_versions.extend([line.replace('i', '1')])
    
    leet_versions.extend([line.replace('o', '0', 1) for _ in range(line.count('o'))])
    leet_versions.extend([line.replace('o', '0')])
    
    return leet_versions

def process_file(input_file):
    unique_lines = set()  # Set to store unique lines
    
    with open(input_file, 'r') as input_f:
        lines = input_f.readlines()

    processed_lines = [replace_special_characters(conjoin_text(remove_punctuation(line.strip()))) for line in lines]
    filtered_lines = filter_lines(processed_lines, 4, 16)

    lowercase_lines = [line.lower() for line in filtered_lines]

    capitalized_lines = [line.capitalize() for line in filtered_lines]

    combined_lines = capitalized_lines + lowercase_lines

    leet_lines = []
    for line in combined_lines:
        leet_versions = leetify(line)
        leet_lines.extend(leet_versions)

    chronology_lines = add_chronologies(leet_lines)
    
    reversed_lines = [line[::-1].lower() for line in filtered_lines]
    reversed_chronology_lines = add_chronologies(reversed_lines)
    
    reversed_chronology_lines.extend(chronology_lines)  # Append original, lowercase, and capitalized conjoined lines
    
    # Add lines to the unique set
    unique_lines.update(reversed_chronology_lines)
    
    sorted_unique_lines = sorted(unique_lines)  # Sort the lines alphabetically
    
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file_with_datetime = f"output_{current_date_time}.txt"

    with open(output_file_with_datetime, 'w') as output_f:
        output_f.write('\n'.join(sorted_unique_lines))

if __name__ == "__main__":
    input_file_name = "input.txt"  # Replace with your input file's name
    process_file(input_file_name)
