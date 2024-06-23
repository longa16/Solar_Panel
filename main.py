"""Main page of solar panel app"""

import time
from source_code.solar_panel import SolarPanel


def menu():
    """Menu of the solar panel app"""
    print("\n Welcome to solar panel Menu \n"
          "1. Add a solar panel \n"
          "2. Use energy of a solar panel \n"
          "3. Store energy of a solar panel \n"
          "4. Calculate efficiency of a solar panel \n"
          "5. Check maintenance of a solar panel \n"
          "6. Calculate useful life of a solar panel  \n"
          "7. Display solar panel informations \n"
          "8. Exit program")
    time.sleep(1)

    solar_panel = None

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the solar panel name: ")
            p_out = float(input("Enter the power output: "))
            surface_area = float(input("Enter the surface area: "))
            bat = 100
            solar_panel = SolarPanel(name, p_out, surface_area, bat)
        elif choice == 2:
            consumed = float(input("Please enter the energy you want to consume: "))
            solar_panel.use_energy(consumed)
        elif choice == 3:
            store = float(input("Please enter the energy you want to store: "))
            solar_panel.store_energy(store)
        elif choice == 4:
            factor = float(input("Please enter the efficiency factor of the solar panel: "))
            b_capacity = float(input("Please enter the battery capacity of the solar panel: "))
            solar_panel.efficiency_calculation(factor, b_capacity)
        elif choice == 5:
            solar_panel.check_maintenance_needed()
        elif choice == 6:
            performance = int(input("Enter The warranty period during which the manufacturer"
                                    " guarantees a certain level of solar panel performance (year): "))
            annual_degradation = float(input("Enter The percentage of expected degradation of solar "
                                             "panel performance each year (0.5 ; 1.0) : "))
            solar_panel.useful_life_calculation(performance, annual_degradation)
        elif choice == 7:
            solar_panel.display_solar_panel_informations()
        elif choice == 8:
            print("Good Bye ;)")
            break
        else:
            print("Error, change it.")

        time.sleep(1)


if __name__ == "__main__":
    menu()
