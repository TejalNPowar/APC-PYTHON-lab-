def read_file():
    filename = input("Enter filename to read: ")
    try:
        with open(filename, "r") as f:
            print("\n--- File Content ---")
            print(f.read())
            print("--------------------")
    except FileNotFoundError:
        print("File not found!")
