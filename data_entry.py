from datetime import datetime as dt

DATE_FORMAT: str = "%d-%m-%Y"
CATAGORIES = {
    "I": "Income",
    "E": "Expense",
}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return dt.today().strftime(DATE_FORMAT)

    try:
        valid_date = dt.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(format=DATE_FORMAT)

    except ValueError:
        print("Invalid Date Fromat Please in dd--mm-yyyy")
        return get_date(prompt, allow_default)


def get_amount():

    try:
        amount = float(input("Enter the Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative Number")
        return amount

    except ValueError as e:
        print(e)
        return get_amount()


def get_category():

    category = input(
        "ENter the Category ('I' for INCOME, or 'E' for EXPENSE): "
    ).upper()

    if category in CATAGORIES:
        return CATAGORIES[category]

    print("Invalid Catagory Please 'I' for Income or 'E' for Expense")
    return get_category()


def get_description():

    return input("Enter a Description (optional): ")
