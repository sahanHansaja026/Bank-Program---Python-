def withdraw():
    try:
        import csv
        file_path = 'accounts.csv'
        account_number_to_search = input("Enter the account number: ")
        rows = []
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                rows.append(row)
        account_found = False
        for row in rows:
            if row[1] == account_number_to_search: 
                account_found = True
                new_balance = float(input("Enter the ammount: "))
                row[3] = float(row[3]) - new_balance
                break
        if account_found:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)
            print("cash withdraw successfully.")
        else:
            print(f"No account found with account number {account_number_to_search}.")
    except:
        print("someting is worng")
