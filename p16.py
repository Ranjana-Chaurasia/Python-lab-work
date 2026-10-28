# Safe File Processor with Custom Exception Hierarchy
import traceback

# Custom exception classes
class FileProcessingError(Exception):
    pass

class InvalidFormatError(FileProcessingError):
    pass

# Function to process a file
def process_file(filename):
    file = None

    try:
        file = open(filename, "r")
        print("File opened successfully.")

        for line_no, line in enumerate(file, 1):
            line = line.strip()

            if not line:
                continue

            # Each line must contain a name and a number separated by a comma
            parts = line.split(",")

            if len(parts) != 2 or not parts[0].strip():
                raise InvalidFormatError(
                    f"Invalid format at line {line_no}: {line}"
                )

            try:
                value = float(parts[1])
            except ValueError:
                raise InvalidFormatError(
                    f"Invalid number at line {line_no}: {line}"
                )

            print(f"Name: {parts[0].strip()}, Value: {value}")

    except FileNotFoundError:
        print("Error: File not found.")

    except InvalidFormatError as error:
        print("Formatting Error:", error)
        with open("error.log", "a") as log:
            log.write(traceback.format_exc())

    except OSError as error:
        print("File Error:", error)

    except Exception:
        print("Unexpected Error:")
        with open("error.log", "a") as log:
            log.write(traceback.format_exc())

    else:
        print("File processed successfully.")

    finally:
        if file is not None:
            file.close()
        print("File processing completed. Resources cleaned up.")

filename = input("Enter file name: ")
process_file(filename)