from Classes.get_data import GetData

class UI:
    RESET = "\033[0m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"

    def __init__(self):
        # בונה אובייקט של GetData כדי לקבל את כל הערכים האפשריים לכל תכונה
        self.get_data = GetData()
        self.dict_unique_val = self.get_data.get_dict_unique_val()

    def enter_situations(self):
        situations = []  # פה נשמור את הבחירות של המשתמש

        # נעבור על כל תכונה (כל עמודה פרט לעמודת התוצאה)
        for feature in self.dict_unique_val:
            # מכינים מחרוזת שתוצג למשתמש עם האפשרויות שלו
            str_for_input = f"{self.BLUE}Choose the {feature} {self.GREEN}( "

            # מציגים את כל האפשרויות עם מספרים
            for i, option in enumerate(self.dict_unique_val[feature], start=1):
                str_for_input += f"{i}. {option}, "
            str_for_input = str_for_input[:-2] + f" ){self.RESET}: "

            # מבקשים מהמשתמש לבחור מספר
            user_choice = input(str_for_input)

            # בודקים שהקלט תקין: מספר בתוך הטווח
            while (not user_choice.isdigit()) or (int(user_choice) < 1 or int(user_choice) > len(self.dict_unique_val[feature])):
                print(f"{self.RED}Invalid choice, please try again.{self.RESET}")
                user_choice = input(str_for_input)

            # מוסיפים את הערך שנבחר למערך התשובות
            situations.append(self.dict_unique_val[feature][int(user_choice) - 1])

        return situations



