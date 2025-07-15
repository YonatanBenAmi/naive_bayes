from Classes.get_data import GetData

class UI:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"

    def __init__(self):
        self.get_data = GetData()
        self.dict_unique_val = self.get_data.get_dict_unique_val()

    def enter_situations(self):
        situations = []

        for feature in self.dict_unique_val:
            str_for_input = f"{self.BLUE}Choose the {feature} {self.GREEN}( "

            for i, option in enumerate(self.dict_unique_val[feature], start=1):
                str_for_input += f"{i}. {option}, "
            str_for_input = str_for_input[:-2] + f" ){self.RESET}: "

            user_choice = input(str_for_input)

            while (not user_choice.isdigit()) or (int(user_choice) < 1 or int(user_choice) > len(self.dict_unique_val[feature])):
                print(f"{self.RED}Invalid choice, please try again.{self.RESET}")
                user_choice = input(str_for_input)

            situations.append(self.dict_unique_val[feature][int(user_choice) - 1])

        return situations



