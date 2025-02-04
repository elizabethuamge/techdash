import os

class TechDash:
    def __init__(self, file_path, chunk_size=1024 * 1024):
        """Initialize with the file path and the desired chunk size (default is 1MB)."""
        self.file_path = file_path
        self.chunk_size = chunk_size
    
    def split_file(self):
        """Splits the file into smaller chunks."""
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        file_size = os.path.getsize(self.file_path)
        file_basename = os.path.basename(self.file_path)
        part_number = 1

        with open(self.file_path, 'rb') as file:
            while True:
                chunk = file.read(self.chunk_size)
                if not chunk:
                    break

                part_filename = f"{file_basename}.part{part_number}"
                with open(part_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                
                print(f"Created chunk {part_filename}")
                part_number += 1

        print("File splitting complete.")

    def join_file(self, output_filename):
        """Joins the chunks back into a single file."""
        file_basename = os.path.basename(self.file_path)
        part_number = 1

        with open(output_filename, 'wb') as output_file:
            while True:
                part_filename = f"{file_basename}.part{part_number}"
                if not os.path.isfile(part_filename):
                    break

                with open(part_filename, 'rb') as chunk_file:
                    output_file.write(chunk_file.read())

                print(f"Merged {part_filename}")
                part_number += 1

        print(f"File reconstruction complete. Created {output_filename}")

if __name__ == "__main__":
    file_to_split = input("Enter the file path to split: ")
    chunk_size = int(input("Enter chunk size in bytes (default is 1048576 bytes): ") or 1048576)
    
    techdash = TechDash(file_to_split, chunk_size)
    techdash.split_file()

    join_choice = input("Do you want to join the files back together? (y/n): ").strip().lower()
    if join_choice == 'y':
        output_file = input("Enter the output file name: ")
        techdash.join_file(output_file)