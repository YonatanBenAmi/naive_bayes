from Classes.get_data import GetData
from fastapi import FastAPI

class UI:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    # <<<<< Creating an instance >>>>>.
    get_data = GetData()
    # <<<<< Variables for DataFrame >>>>>
    dict_unique_val = get_data.get_dict_unique_val() # A dictionary that holds all the unique values ​​for each column.

    
    def enter_situations(self):
        situations = []
        for feature in self.dict_unique_val:
            str_for_input = f"{self.BLUE}Choose the {feature} {self.GREEN}( "
            i = 1
            for option in self.dict_unique_val[feature]:
                str_for_input += f"{i}. {option}, "
                i += 1
            str_for_input = str_for_input[:-2] + f" ):{self.RESET} "

            user_choice = input(str_for_input)
            while (not user_choice.isdigit()) or (int(user_choice) > 0 and not int(user_choice) <= len(self.dict_unique_val[feature])):
                print(f"{self.RED}Valid choice{self.RESET}")
                user_choice = input(str_for_input)

            situations.append(self.dict_unique_val[feature][int(user_choice) - 1])
        return situations
    



