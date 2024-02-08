import os


def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.startswith("TEST_") and file.find("success") == -1:
                file_path = os.path.join(root, file)
                n = file.split("_")[-1]
                result_file_path = os.path.join(
                    output_folder, f"TEST_AUCHAN_success_{n}")

                process_file(file_path, result_file_path)


def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read().replace('"', "")
        numbers = data.strip().split(",")

        with open(output_file, 'w') as result_file:
            for number in numbers:
                if not number:
                    continue
                if number.find("-") != -1:
                    start, end = number.split("-")
                    for i in range(int(start), int(end)+1):
                        result_file.write(str(i) + '\n')
                    continue

                result_file.write(str(int(number)) + '\n')


if __name__ == "__main__":
    input_folder = "./files"
    output_folder = "./files/Result"

    process_files(input_folder, output_folder)
