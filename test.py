import os


def fetch_txt_files(directory_path):
    # Using list comprehension for brevity and ensuring unique file names
    return [file_name for file_name in os.listdir(directory_path) if file_name.endswith('.txt')]


def extract_elements(file_names):
    extracted_elements = []
    for file_name in file_names:
        parts = file_name.split('_')
        if len(parts) > 7:  # Ensure there are enough parts
            first_element = parts[0]
            second_element = parts[1].upper()
            fourth_element = parts[3].upper()
            seventh_element = parts[6]
            extra_element = 'CDR'
            extracted_elements.append((first_element, second_element, seventh_element, fourth_element, extra_element))
    print("Extracted elements:", extracted_elements)
    return extracted_elements

if __name__ == '__main__':
    folder_path = os.path.join('txtFiles')  # Ensuring platform-independent path
    txt_file_names = fetch_txt_files(folder_path)

    print("Text files found:", txt_file_names)
    extracted_data = extract_elements(txt_file_names)

    for data in extracted_data:
        print(data)
