import requests
from colorama import init, Fore, Style


init()


class Cocktails(object):
    def __init__(self):
        self.source_ingredients = []
        api_key = 9973533
        self.popular_cocktails_url = f'https://www.thecocktaildb.com/api/json/v2/{api_key}/popular.php'
        self.latest_cocktails_url = f'https://www.thecocktaildb.com/api/json/v2/{api_key}/latest.php'
        self.popular_cocktails = []
        self.latest_cocktails = []
        self.possible_cocktails = []        
        self.process_input()
        self.cocktails_simplified1 = self.retrieve_possible_cocktails(url=self.popular_cocktails_url, cocktails_type=self.popular_cocktails, all_cocktails={})
        self.cocktails_simplified2 = self.retrieve_possible_cocktails(url=self.latest_cocktails_url, cocktails_type=self.latest_cocktails, all_cocktails={})
        self.cocktails_simplified1.update(self.cocktails_simplified2)
        self.create_output()
        self.display_result()

    def display_result(self):
        print(Fore.BLUE, "\nPossible cocktails:")
        output = '\n'+'\n'.join(self.possible_cocktails)
        print(Fore.GREEN, f"{output}")

    def process_input(self):
        print(Fore.BLUE, "Please enter your source ingredients in comma separated variable format, with one space separating each comma.")
        print(Style.RESET_ALL)
        self.source_ingredients = input().split(', ')

    def create_output(self):
        for k, v in self.cocktails_simplified1.items():
            if all(ingredient in self.source_ingredients for ingredient in v):
                self.possible_cocktails.append(k)

    def retrieve_possible_cocktails(self, url, cocktails_type, all_cocktails):
        try:
            response = requests.get(url=url)
            if response.status_code == 200:
                cocktails_type = response.json()
                cocktails = []
                for i in range(0, len(cocktails_type['drinks'])):
                    for k, v in cocktails_type['drinks'][i].items():
                        if k == 'strDrink':
                            cocktails.append(v)
                all_cocktails = {c: [] for c in cocktails}
                for i, c in zip(range(0, len(cocktails_type['drinks'])), all_cocktails):
                    for key, value in cocktails_type['drinks'][i].items():
                        if 'strIngredient' in key and value != None:
                            all_cocktails[c].append(value)
                return all_cocktails
 
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            if self.timeout < 3:
                self.timeout += 1
                self.get_data()
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print(Fore.RED, "Too many redirects; possible bad URL?")
        except requests.exceptions.RequestException as e:
            # Disaster.
            print(Fore.RED, "Requests failure.")
            raise SystemExit(e)


if __name__ == '__main__':
    c = Cocktails()