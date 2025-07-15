
from Classes.data_trainer import Trainer   
from Classes.classifier import Classifier   
from Classes.ui import UI              

def main():
    trainer = Trainer()
    classifier = Classifier(trainer)
    ui = UI()
    flag = True

    while flag:
        result_values = ui.enter_situations()
        result_dict = dict(zip(trainer.feature, result_values))

        prediction, stats = classifier.classify_with_stats(result_dict)

        print(f"\n{ui.GREEN}Prediction: {prediction}{ui.RESET}\n")

        for category, prob in stats.items():
            print(f"{category}: {prob:.8f}")

        again = input("\nClassify another example? (y/n): ")
        if again.lower() != 'y':
            flag = False


if __name__ == "__main__":
    main()

