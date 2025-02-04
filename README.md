# TechDash

TechDash is a simple Python program designed to split large files into smaller, manageable parts for easier sharing and storage on Windows systems. It also allows you to rejoin these parts back into the original file.

## Features

- Split large files into smaller chunks.
- Rejoin file chunks back into the original file.
- Customizable chunk size.

## Requirements

- Python 3.x

## Installation

Download the `techdash.py` file to your local machine.

## Usage

1. Open a terminal window (Command Prompt on Windows).
2. Navigate to the directory containing `techdash.py`.
3. Run the script using the command:
   ```bash
   python techdash.py
   ```
4. Follow the prompts to enter the file path and specify the chunk size.
5. To rejoin the files, follow the prompts after the file has been split.

## Example

To split a file named `largefile.txt` into 1MB chunks:

```bash
python techdash.py
```

- Enter the file path: `largefile.txt`
- Enter chunk size in bytes (default is 1048576 bytes): `1048576`
- Follow the on-screen instructions to complete the process.

## Notes

- Ensure the file to split exists in the specified path.
- The default chunk size is set to 1MB (1048576 bytes), but this can be adjusted according to your needs.
- The program will create chunk files in the same directory as the original file, with filenames in the format `originalfile.partN`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.