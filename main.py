import pandas as pd
import csv
from datetime import datetime as dt
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finanice_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)

            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry added successfully")

    @classmethod
    def get_transaction(cls, start_date, end_date):

        df = pd.read_csv(cls.CSV_FILE)

        df["date"] = pd.to_datetime(df["date"], format=CSV.DATE_FORMAT)
        start_date = dt.strptime(start_date, CSV.DATE_FORMAT)
        end_date = dt.strptime(end_date, CSV.DATE_FORMAT)

        mask = df["date"] >= start_date & df["date"] <= end_date

        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No Transaction found in the given date range")

        else:
            print(
                f"Transaction from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}"
            )


def add():

    CSV.initialize_csv()

    date = get_date(
        prompt="Enter the Date of the transaction (dd-mm-yyyy) or Enter for Today's date: ",
        allow_default=True,
    )

    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(
        date=date,
        amount=amount,
        category=category,
        description=description,
    )
