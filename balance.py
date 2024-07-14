def check_balance():
    import csv
    file_path = 'accounts.csv'
    account_number_to_search = input("Enter the account number to search: ")
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        account_details = None
        for row in reader:
            if row[1] == account_number_to_search: 
                account_details = row
                break
    if account_details:
        print("Account details found:")
        for col, value in zip(header, account_details):
            print(f"{col}: {value}")
    else:
        print(f"No account found with account number {account_number_to_search}.")

