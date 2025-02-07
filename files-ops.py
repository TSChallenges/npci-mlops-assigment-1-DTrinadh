#code for few file operations using python
import os
import sys


def create_directory(dir_name):
    os.mkdir(dir_name)
    print("Directory was created")

    return

def change_directory(dir_name):
    os.chdir(dir_name)
    print("Changed Directory path");
    return


def delete_directory(dir_name):
    os.rmdir(dir_name)
    print("Succesfully removed directory");
    return


def list_dir():
    print("list of present directories");
    print(os.listdir());
    return


def display_pwd():
    print("present working directory");
    print(os.getcwd());
    return


def create_file(file_name):

    with open(file_name, 'w') as f:
        pass
    print(f"File '{file_name}' is created")

    return


def write_file(file_name):

    contents = input("Enter the contents into the file")
    with open(file_name, 'a') as f:
        f.write(contents + '\n')
    print(f"Contents written to file successfully")

    return


def read_file(file_name):

    with open(file_name, 'r') as f:
        print(f.read())

    return


def delete_file(file_name):
    #for testing purpose to this function have created delete.txt file and deleted via functions only
    os.remove(file_name)
    return


def main():
    while True:
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Delete a file")
        print("0. Exit")
        choice = input("Enter your choice here: ")

        if choice == '1':
            file_name = input("1. Enter the file name")
            create_file(file_name)
        elif choice == '2':
            file_name = input("2. Enter the file name")
            write_file(file_name)
        elif choice == '3':
            file_name = input("3. Enter the file name")
            read_file(file_name)
        elif choice == '4':
            file_name = input("4. Enter the file name")
            delete_file(file_name)
        elif choice == '0':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
