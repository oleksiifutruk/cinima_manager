from Movie import *


class Cinema_hall:  # Create Cinema class.
    hall_list = []  # Hall BD

    def __init__(self, hall_color, seans1T, seans1, seans2T, seans2, seans3T, seans3, seans4T,
                 seans4):  # Create Cinema Room, Color and session.
        self.hall = hall_color
        self.seans1, self.seans1T = seans1, seans1T
        self.seans2, self.seans2T = seans2, seans2T
        self.seans3, self.seans3T = seans3, seans3T
        self.seans4, self.seans4T = seans4, seans4T
        Cinema_hall.hall_list.append(self)

    def show_schedule(self): #Schedule for 1 object
        print(f"<<<Welcomes to the {self.hall} hall>>>")
        print(f"{self.seans1T} --> {self.seans1.name}")
        print(f"{self.seans2T} --> {self.seans2.name}")
        print(f"{self.seans3T} --> {self.seans3.name}")
        print(f"{self.seans4T} --> {self.seans4.name}")


first, second, third = Cinema_hall("red", "10:00", a, "13:00", b, "16:00", c, "19:00", d), \
                       Cinema_hall("blue", "11:00", e, "14:00", d, "17:00", c, "20:00", b), \
                       Cinema_hall("green", "22:00", d, "01:00", c, "04:00", b, "07:00", e)  # creat object
