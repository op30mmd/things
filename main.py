import os

def main():
  """
  Main function of the CLI file manager.
  """
  # Display current directory
  print(f"Current directory: {os.getcwd()}")

  # Get user input
  user_input = ""
  while user_input.lower() != "exit":
    user_input = input("> ").strip()

    # Handle different commands
    if user_input == "ls":
      # List files and directories
      list_files_and_directories()
    elif user_input.startswith("cd"):
      # Change directory
      change_directory(user_input)
    elif user_input.startswith("mkdir"):
      # Create directory
      create_directory(user_input)
    elif user_input.startswith("rm"):
      # Remove file or directory
      remove_file_or_directory(user_input)
    elif user_input == "help":
      # Display help message
      print_help()
    else:
      print(f"Unknown command: '{user_input}'")

def list_files_and_directories():
  """
  List files and directories in the current directory.
  """
  for entry in os.listdir():
    if os.path.isfile(entry):
      print(f"\t{entry}")
    elif os.path.isdir(entry):
      print(f"\t[DIR] {entry}")

def change_directory(command):
  """
  Change the current directory.
  """
  try:
    os.chdir(command[3:])
  except FileNotFoundError:
    print(f"Error: Directory '{command[3:]}' does not exist.")

def create_directory(command):
  """
  Create a new directory.
  """
  try:
    os.mkdir(command[4:])
  except FileExistsError:
    print(f"Error: Directory '{command[4:]}' already exists.")

def remove_file_or_directory(command):
  """
  Remove a file or directory.
  """
  try:
    os.remove(command[3:])
  except FileNotFoundError:
    print(f"Error: File or directory '{command[3:]}' does not exist.")
  except IsADirectoryError:
    os.rmdir(command[3:])

def print_help():
  """
  Display a help message.
  """
  print("\nAvailable commands:")
  print("\tls: List files and directories in the current directory.")
  print("\tcd <directory>: Change the current directory.")
  print("\tmkdir <directory>: Create a new directory.")
  print("\trm <file/directory>: Remove a file or directory.")
  print("\thelp: Display this help message.")
  print("\texit: Quit the program.\n")

if __name__ == "__main__":
  main()
