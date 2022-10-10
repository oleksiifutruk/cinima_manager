from Cinema import *





def movi():  # information about movie list
    hesh = []
    for i in set(Cinema_hall.hall_list):
        hesh.append(i.seans1)
        hesh.append(i.seans2)
        hesh.append(i.seans3)
        hesh.append(i.seans4)
    for item in set(hesh):
        print(f"{item.name}. Duration : {item.duration} minutes.")


def cinema_info():  # information about hall
    for hall in Cinema_hall.hall_list:
        hall.show_schedule()
        print()


def one_cinema_info(hall):  # One Hall info
    Cinema_hall.hall_list[hall].show_schedule()


def main():
    try:
        inp = int(input(
            "Hello viewer!, information menu:"
            "\n  ""See the list of available movies  input -> 1"
            "\n  See the schedule of all halls     input -> 2"
            "\n  Hall information: `Red` input -> 3, `Blue` input -> 4, `Green` input -> 5"
            "\nENTER:"))
        if inp == 1:
            movi()
        if inp == 2:
            cinema_info()
        if inp == 3:
            one_cinema_info(0)
        if inp == 4:
            one_cinema_info(1)
        if inp == 5:
            one_cinema_info(2)
    except:
        print("Error : 1,2...5")


if __name__ == '__main__':
    main()
