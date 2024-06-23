""" The SolarPanel class represents a solar panel with attributes such as name, power output,
surface area, battery level and battery capacity.
Various methods for interacting with the solar panel.
"""


class SolarPanel:
    """Represent a solar panel.
       Attributes:
           name (str): The name of the solar panel.
           power_output (float): The power output of the solar panel in watts.
           surface_area (float): The surface area of the solar panel in square meters.
           solar_panel_level_of_the_battery (int): The battery level of the solar panel (0-100%).
       """

    def __init__(self, name, power_output, surface_area, solar_panel_level_of_the_battery):
        """Initialize a new instance of SolarPanel.
        """
        assert name.isalnum(), "name must be alphanumeric"
        assert power_output > 0
        self.name = name
        self.power_output = power_output
        self.surface_area = surface_area
        self.solar_panel_level_of_the_battery = solar_panel_level_of_the_battery
        self.solar_panel_level_of_the_battery = 100

    def display_solar_panel_informations(self):
        """Display solar panel information.
        """
        solar_panel = SolarPanel(self.name, self.power_output, self.surface_area,
                                 self.solar_panel_level_of_the_battery)
        print("name: ", self.name, "power output: ", self.power_output, "surface area: ", self.surface_area,
              "level battery: ", self.solar_panel_level_of_the_battery)

    def use_energy(self, energy_consumed: float):
        """Use energy from the solar panel's battery.
               :argument: energy_consumed: The amount of energy to consume.
        """
        if self.solar_panel_level_of_the_battery <= energy_consumed:
            print("level battery is not enough for this use")
        if self.solar_panel_level_of_the_battery >= energy_consumed:
            self.solar_panel_level_of_the_battery -= energy_consumed
            print(energy_consumed, "used", self.solar_panel_level_of_the_battery, "rest")

    def store_energy(self, energy: float):
        """Store energy in the solar panel's battery.
                :argument: energy (float): The amount of energy to store.
        """
        assert energy > 0.0
        if self.solar_panel_level_of_the_battery == 100:
            print("This solar panel don't need more energy ")
        else:
            self.solar_panel_level_of_the_battery += energy
            print("great charge!")
            if self.solar_panel_level_of_the_battery > 100:
                self.solar_panel_level_of_the_battery = 100
                print("Level battery is full")

    def perform_maintenance(self):
        """Restore the performance of a solar panel
        """
        self.solar_panel_level_of_the_battery = 100

    def check_maintenance_needed(self):
        """Check if solar panel need maintenance
        """
        if self.solar_panel_level_of_the_battery < 20:
            print("Solar panel need maintenance, Let's do it !")
            self.perform_maintenance()
            print(self.solar_panel_level_of_the_battery)
        elif self.solar_panel_level_of_the_battery >= 20:
            print("the solar panel does not yet need maintenance !")

    def efficiency_calculation(self, efficiency_factor: float, battery_capacity: float):
        """solar panel efficiency calculation
        """
        n = ((self.power_output + self.solar_panel_level_of_the_battery)
             / (self.surface_area * battery_capacity))
        n = n * efficiency_factor * 100
        print("efficiency: ", round(n, 2))
        if n < 15:
            print("BAD")
        else:
            print("GOOD")

    @staticmethod
    def useful_life_calculation(performance_guarantee: int, annual_degradation_rate: float):
        """Solar panel useful life calculation"""
        useful_life = performance_guarantee / annual_degradation_rate
        print("useful life is:", round(useful_life, 2))
