import pandas


class Answer:
    """It process the answers"""
    def __init__(self):
        self.states = []
        self.x = []
        self.y = []
        self.new_states = []
        self.mod_dict = {}
        self.small()

    def small(self):
        """Makes the states name into smaller case and creates a new .csv file"""
        data = pandas.read_csv("50_states.csv")
        data_state = data["state"]
        data_x = data["x"]
        data_y = data["y"]
        # print(data)
        new_state = data_state.to_list()
        new_x = data_x.to_list()
        new_y = data_y.to_list()
        self.states = new_state
        # print(self.states)
        self.x = new_x
        self.y = new_y
        temp = [i.lower() for i in self.states]
        # print(self.states)
        # for i in self.states:
        #     temp.append(i.lower())
        self.new_states = temp
        self.mod_dict["state"] = self.new_states
        self.mod_dict["x"] = self.x
        self.mod_dict["y"] = self.y
        data = pandas.DataFrame(self.mod_dict)
        data.to_csv("state.csv")

    def check(self, answer):
        """Checks the answer for correctness"""
        if answer.lower() in self.new_states:
            return True
        else:
            return False

    def place_answer(self, answer):
        """It sends the word to be placed and the coordinates of the words to be places"""
        check = self.check(answer)
        place = ""
        x_cor = 0
        y_cor = 0
        i = 0
        if check:
            for i in range(0, len(self.new_states)):
                if answer.lower() == self.new_states[i]:
                    place = self.states[i]
                    x_cor = int(self.x[i])
                    y_cor = int(self.y[i])
                    break
            del self.new_states[i]
            del self.states[i]
            del self.x[i]
            del self.y[i]
            return True, place, x_cor, y_cor
        else:
            return False, place, x_cor, y_cor

    def left_answer(self):
        """Prints the states which is not entered"""
        for i in self.new_states:
            print(i)
