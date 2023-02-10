import csv


def read_csv(path_to_file: str):  # -> List[Dict]:
    """Responsible for reading the csv file"""
    with open(path_to_file) as file:
        data = csv.DictReader(
            file, delimiter=",", fieldnames=["cliente", "pedido", "dia"]
        )
        return [product for product in data]


def analyze_log(path_to_file: str):
    data = read_csv(path_to_file)
