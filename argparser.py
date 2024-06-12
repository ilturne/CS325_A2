import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='CLI program')
    parser.add_argument('file_path', type=str, help='Path to the file')
    parser.add_argument('integer_value', type=int, help='Integer value')
    parser.add_argument('float_value', type=float, help='Float value')
    args = parser.parse_args()

    file_path = args.file_path
    integer_value = args.integer_value
    float_value = args.float_value

    result = integer_value + float_value

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
