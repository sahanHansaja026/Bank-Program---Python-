def account_initialization():
    import csv
    try:
        file_path = 'accounts.csv'
        name = input("Enter the new account owner name: ")
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        num_items = len(rows)
        account_number = "0660-123-" + str(num_items)
        mode = input("Enter the mode (saving/deposit): ")

        while True:
            initial_value = float(input("Enter the initial fund: "))
            if initial_value <= 100:
                print("Initial value must be greater than 100.")
            else:
                value = initial_value
                break

        new_row = [name, account_number, mode, value]

        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        print("Account added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the initial fund.")
    except Exception as e:
        print(f"Something went wrong: {e}")


    