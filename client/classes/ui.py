import requests

class UI:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"


    def enter_situations(self):
        situations = {}
        dict_uniqe_valu = requests.get('http://127.0.0.1:8000/uniqe_val').json()
        for feature in dict_uniqe_valu:
            str_for_input = f"{self.BLUE}Choose the {feature} {self.GREEN}( "

            for i, option in enumerate(dict_uniqe_valu[feature], start=1):
                str_for_input += f"{i}. {option}, "
            str_for_input = str_for_input[:-2] + f" ){self.RESET}: "

            user_choice = input(str_for_input)

            while (not user_choice.isdigit()) or (int(user_choice) < 1 or int(user_choice) > len(dict_uniqe_valu[feature])):
                print(f"{self.RED}Invalid choice, please try again.{self.RESET}")
                user_choice = input(str_for_input)

            situations[feature] = dict_uniqe_valu[feature][int(user_choice) - 1]

        return situations



