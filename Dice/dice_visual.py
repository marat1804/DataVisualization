from Dice.dice import Dice
import pygal


class DiceVisual:
    def __init__(self, dices):
        self.__dices = []
        for dice in dices:
            self.__dices.add(dice)
        self.results = []
        self.frequencies = []

    def rollAll(self):
        for _ in range(50000):
            result = 0
            for dice in self.__dices:
                result += dice.roll()
            self.results.append(result)

    def countFrequencies(self):
        max_result = 0
        for dice in self.__dices:
            max_result += dice.num_sides
        for value in range(2, max_result + 1):
            frequency = self.results.count(value)
            self.frequencies.append(frequency)

    def createHist(self):
        hist = pygal.Bar()
        hist.title = 'Results of rolling two D6 dice 50000 times'
        hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                         '15', '16']
        hist.x_title = 'Result'
        hist.y_title = 'Frequency of Result'
        name = ""
        for dice in self.__dices:
            name += "D" + str(dice.num_sides) + " "
        hist.add(name, self.frequencies)
        hist.render_to_file('diсe_visual_1.svg')


if "__init__" == "__main__":
    diceVisual = DiceVisual([Dice(), Dice(10)])
    diceVisual.rollAll()
    diceVisual.countFrequencies()
    diceVisual.createHist()
