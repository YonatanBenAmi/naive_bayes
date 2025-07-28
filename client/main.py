
from classes.ui import UI      
import requests        

def main():

    ui = UI()
    flag = True

    while flag:
        result_values = ui.enter_situations() # User choices
        # data = requests.get('http://localhost:8001') 
        # print("Data from server:", data.json())  # Display data from the server

        response = requests.post('http://localhost:8001/classify', json=result_values).json()
        print("success", response)
        # print(f"\n{ui.GREEN}Prediction: {response['prediction']}{ui.RESET}\n")

        for category, prob in response['results'].items():
            print(f"{category}: {prob:.8f}")

        again = input("\nClassify another example? (y/n): ")
        if again.lower() != 'y':
            flag = False



if __name__ == "__main__":
    main()

