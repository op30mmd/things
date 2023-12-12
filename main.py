import os
import argparse
import shutil

def main():
  """
  Main function of the interactive CLI file manager.
  """
  # Initialize variables
  current_directory = os.getcwd()
  command = None

  # Welcome message
  print("Welcome to the interactive CLI file manager!")

  while command != "exit":
    # Display current directory
    print(f"\nCurrent directory: {current_directory}")

    # Prompt user for command
    command = input("Enter command: ").strip()

    # Handle different commands
    if command == "ls":
      list_files_and_directories(current_directory)
    elif command.startswith("cd"):
      current_directory = change_directory(current_directory, command)
    elif command.startswith("mkdir"):
      create_directory(current_directory, command)
    elif command.startswith("rm"):
      remove_file_or_directory(current_directory, command)
    elif command.startswith("mv"):
      move_file_or_directory(current_directory, command)
    elif command.startswith("cp"):
      copy_file_or_directory(current_directory, command)
    elif command.startswith("rename"):
      rename_file_or_directory(current_directory, command)
    elif command.startswith("chmod"):
      change_file_permissions(current_directory, command)
    elif command == "help":
      print_help()
    elif command == "exit":
      print("Bye!")
    else:
      print(f"Unknown command: '{command}'")

def list_files_and_directories(current_directory):
  """
  List files and directories in the specified directory.
  """
  for entry in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, entry)):
      print(f"\t{entry}")
    elif os.path.isdir(os.path.join(current_directory, entry)):
      print(f"\t[DIR] {entry}")

def change_directory(current_directory, command):
  """
  Change the current directory.
  """
  try:
    new_directory = os.path.join(current_directory, command[3:])
    os.chdir(new_directory)
    return new_directory
  except FileNotFoundError:
    print(f"Error: Directory '{command[3:]}' does not exist.")
    return current_directory

def create_directory(current_directory, command):
  """
  Create a new directory.
  """
  try:
    new_directory = os.path.join(current_directory, command[4:])
    os.mkdir(new_directory)
  except FileExistsError:
    print(f"Error: Directory '{command[4:]}' already exists.")

def remove_file_or_directory(current_directory, command):
  """
  Remove a file or directory.
  """
  try:
    target_path = os.path.join(current_directory, command[3:])
    if os.path.isfile(target_path):
      os.remove(target_path)
    elif os.path.isdir(target_path):
      shutil.rmtree(target_path)
  except FileNotFoundError:
    print(f"Error: File or directory '{command[3:]}' does not exist.")

def move_file_or_directory(current_directory, command):
  """
  Move a file or directory.
  """
  try:
    source_path = os.path.join(current_directory, command[3:])
    target_path = input("Enter target path: ")
    shutil.move(source_path, target_path)
  except Exception as e:
    print(f"Error moving '{command[3:]}': {e}")

def copy_file_or_directory(current_directory, command):
  """
  Copy a file or directory.
  """
  try:
    source_path = os.path.join(current_directory, command[3:])
    target_path = input("Enter target path: ")
    if os.path.isdir(source_path):
      shutil.copytree(source_path, target_path)
    else:
      shutil.copy2(source_path, target_path)
  except Exception as e
