
import json
from classes.ui import UI      
import requests        

def main():

    ui = UI()
    flag = True

    while flag:
        result_values = ui.enter_situations() # User choices

        result = requests.post(f'http://127.0.0.1:8000/classify', json=result_values).json()

        print(f"\n{ui.GREEN}Prediction: {result['prediction']}{ui.RESET}\n")

        for category, prob in result['results'].items():
            print(f"{category}: {prob:.8f}")

        again = input("\nClassify another example? (y/n): ")
        if again.lower() != 'y':
            flag = False


if __name__ == "__main__":
    main()

