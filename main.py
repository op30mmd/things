import os
import argparse
import shutil

def main():
  """
  Main function of the CLI file manager.
  """
  parser = argparse.ArgumentParser(description="A simple CLI file manager")

  # Create a mutually exclusive group for conflicting options
  exclusive_group = parser.add_mutually_exclusive_group()

  # Add options to the group
  exclusive_group.add_argument("-h", "--help", action="store_true", help="Display help message")
  exclusive_group.add_argument("-l", "--list", action="store_true", help="List files and directories")
  parser.add_argument("-d", "--directory", default=os.getcwd(), help="Set the starting directory")
  parser.add_argument("-c", "--copy", help="Copy a file or directory")
  parser.add_argument("-m", "--move", help="Move a file or directory")
  parser.add_argument("-r", "--rename", nargs=2, help="Rename a file or directory")
  parser.add_argument("-p", "--permission", help="Change file permissions")

  args = parser.parse_args()

  # Set starting directory
  os.chdir(args.directory)

  # Handle different commands based on parsed arguments
  if args.help:
    print_help()
  elif args.list:
    list_files_and_directories()
  elif args.copy:
    copy_file_or_directory(args.copy)
  elif args.move:
    move_file_or_directory(args.move)
  elif args.rename:
    rename_file_or_directory(args.rename[0], args.rename[1])
  elif args.permission:
    change_file_permissions(args.permission)
  else:
    print("No command specified. Use -h or --help for available commands.")

def list_files_and_directories():
  """
  List files and directories in the current directory.
  """
  for entry in os.listdir():
    if os.path.isfile(entry):
      print(f"\t{entry}")
    elif os.path.isdir(entry):
      print(f"\t[DIR] {entry}")

def copy_file_or_directory(source):
  """
  Copy a file or directory.
  """
  target = input("Enter target path: ")
  try:
    if os.path.isdir(source):
      shutil.copytree(source, target)
    else:
      shutil.copy2(source, target)
    print(f"Successfully copied '{source}' to '{target}'")
  except Exception as e:
    print(f"Error copying '{source}': {e}")

def move_file_or_directory(source):
  """
  Move a file or directory.
  """
  target = input("Enter target path: ")
  try:
    shutil.move(source, target)
    print(f"Successfully moved '{source}' to '{target}'")
  except Exception as e:
    print(f"Error moving '{source}': {e}")

def rename_file_or_directory(source, target):
  """
  Rename a file or directory.
  """
  try:
    os.rename(source, target)
    print(f"Successfully renamed '{source}' to '{target}'")
  except Exception as e:
    print(f"Error renaming '{source}': {e}")

def change_file_permissions(command):
  """
  Change file permissions.
  """
  # Implement permission change functionality
  print("Feature under development!")

def print_help():
  """
  Display a help message.
  """
  print(parser.format_help())

if __name__ == "__main__":
  main()
