import requests


class CountryData:
    def __init__(self):
        self.countries = self.get_all_countries()
        self.data = self.create_country_list()

    @staticmethod
    def get_all_countries():
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    def get_country_by_name(self, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    def create_country_list(self):
        data = []

        for country in self.countries:
            name = country['name']['common']
            capital = country['capital'][0] if 'capital' in country else 'N/A'
            flag_url = country['flags']['png']
            data.append({"Country Name": name, "Capital Name": capital, "Flag URL (png)": flag_url})

        return data

    def print_table_with_borders(self, data):
        # Compute the maximum length for each column
        max_name_len = max(len(str(item["Country Name"])) for item in data) + 2
        max_capital_len = max(len(str(item["Capital Name"])) for item in data) + 2
        max_flag_len = (max(len(str(item["Flag URL (png)"])) for item in data) + 2) // 2

        border_line = "+" + "-" * max_name_len + "+" + "-" * max_capital_len + "+" + "-" * max_flag_len + "+"

        # Print table headers
        headers = "| {0:<{name_len}} | {1:<{capital_len}} | {2:<{flag_len}} |".format(
            "Country Name", "Capital Name", "Flag URL (png)",
            name_len=max_name_len - 2, capital_len=max_capital_len - 2, flag_len=max_flag_len - 2)

        print(border_line)
        print(headers)
        print(border_line)

        # Print table rows
        for item in data:
            row = "| {0:<{name_len}} | {1:<{capital_len}} | {2:<{flag_len}} |".format(
                item["Country Name"], item["Capital Name"], item["Flag URL (png)"],
                name_len=max_name_len - 2, capital_len=max_capital_len - 2, flag_len=max_flag_len - 2)
            print(row)
            print(border_line)


# Main script
def main():
    country_data = CountryData()
    print("Enter 'all' to display all countries or enter a country name in English.")
    print("To exit the program, type 'exit'.")

    while True:
        choice = input("Please make your choice: ").strip()

        if choice.lower() == 'exit':
            print("Exiting the program.")
            break
        elif choice.lower() == 'all':
            country_data.print_table_with_borders(country_data.data)
        else:
            specific_country_data = country_data.get_country_by_name(choice)
            if specific_country_data:
                formatted_data = [{
                    "Country Name": specific_country_data[0]['name']['common'],
                    "Capital Name": specific_country_data[0]['capital'][0] if 'capital' in specific_country_data[0] else 'N/A',
                    "Flag URL (png)": specific_country_data[0]['flags']['png']
                }]
                country_data.print_table_with_borders(formatted_data)
            else:
                print("Country not found. Please try again.")


if __name__ == "__main__":
    main()
