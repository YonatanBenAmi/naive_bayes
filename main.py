
from Classes.data_trainer import Trainer   
from Classes.classified import Classifier   
from Classes.ui import UI              

def main():
    trainer = Trainer()
    classifier = Classifier(trainer)
    ui = UI()
    flag = True

    while flag:
        result_values = ui.enter_situations()
        result_dict = dict(zip(trainer.feature, result_values))

        prediction, stats, percentages = classifier.classify_with_details(result_dict)

        print(f"\n{ui.GREEN}Prediction: {prediction}{ui.RESET}\n")

        print("Detail")
        for category in stats:
            prob = stats[category]
            percent = percentages[category]
            print(f"{category}: {prob:.8f} ({percent:.2f}%)")

        again = input("\nClassify another example? (y/n): ")
        if again.lower() != 'y':
            flag = False


if __name__ == "__main__":
    main()
