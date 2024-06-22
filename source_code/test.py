"""Test for SolarPanel class and  all its functions"""

import pytest
from solar_panel import SolarPanel


@pytest.fixture
def solar_panel():
    """Create a fixture for all the test"""
    return SolarPanel("Sputnik", 200, 15, 500)


def test_solar_panel_information(solar_panel):
    """add_solar_panel Test"""
    assert solar_panel.name == "Sputnik"
    assert solar_panel.power_output == 200
    assert solar_panel.surface_area == 15
    assert solar_panel.solar_panel_level_of_the_battery == 100


def test_use_energy_enough_battery(solar_panel, capsys):
    """use_energy Test
    when level battery is enough"""
    solar_panel.solar_panel_level_of_the_battery = 100
    solar_panel.use_energy(30)
    assert solar_panel.solar_panel_level_of_the_battery == 100 - 30
    captured = capsys.readouterr()
    assert "30 used 70 rest" in captured.out


def test_use_energy_not_enough_battery(solar_panel, capsys):
    """use_energy Test
    when level battery isn't enough"""
    solar_panel.solar_panel_level_of_the_battery = 20
    solar_panel.use_energy(30)
    assert solar_panel.solar_panel_level_of_the_battery == 20
    captured = capsys.readouterr()
    assert "level battery is not enough for this use" in captured.out


def test_store_energy_when_full(solar_panel, capsys):
    """store_energy Test
    when solar panel don't need storage"""
    solar_panel.solar_panel_level_of_the_battery = 100
    solar_panel.store_energy(50)
    assert solar_panel.solar_panel_level_of_the_battery == 100
    captured = capsys.readouterr()
    assert "This solar panel don't need more energy" in captured.out


def test_store_energy_below_full(solar_panel, capsys):
    """store_energy Test
    when storage below 100"""
    solar_panel.solar_panel_level_of_the_battery = 50
    solar_panel.store_energy(30)
    assert solar_panel.solar_panel_level_of_the_battery == 50 + 30
    captured = capsys.readouterr()
    assert "great charge!" in captured.out


def test_store_energy_above_full(solar_panel, capsys):
    """store_energy Test
    when storage greater than 100"""
    solar_panel.solar_panel_level_of_the_battery = 80
    solar_panel.store_energy(40)
    assert solar_panel.solar_panel_level_of_the_battery == 100
    captured = capsys.readouterr()
    assert "Level battery is full" in captured.out


def test_perform_maintenance(solar_panel):
    """perform_maintenance test
    Restore solar panel performance"""
    solar_panel.solar_panel_level_of_the_battery = 80
    solar_panel.perform_maintenance()
    assert solar_panel.solar_panel_level_of_the_battery == 100


def test_check_maintenance_needed_low_battery(solar_panel, capsys):
    """check_maintenance_needed Test
    when solar panel need maintenance"""
    solar_panel.solar_panel_level_of_the_battery = 15
    solar_panel.check_maintenance_needed()
    assert solar_panel.solar_panel_level_of_the_battery == 100
    captured = capsys.readouterr()
    assert "Solar panel need maintenance, Let's do it !" in captured.out
    assert "100" in captured.out


def test_check_maintenance_needed_high_battery(solar_panel, capsys):
    """check_maintenance_needed Test
    when solar panel don't need maintenance"""
    solar_panel.solar_panel_level_of_the_battery = 50
    solar_panel.check_maintenance_needed()
    assert solar_panel.solar_panel_level_of_the_battery == 50
    captured = capsys.readouterr()
    assert "the solar panel does not yet need maintenance !" in captured.out


def test_efficiency_calculation_bad_efficiency(solar_panel, capsys):
    """efficiency_calculation Test
    when a solar panel has an efficiency below 15"""
    solar_panel.solar_panel_level_of_the_battery = 30
    solar_panel.efficiency_calculation(0.85, 500)
    captured = capsys.readouterr()
    assert "BAD" in captured.out


def test_efficiency_calculation_good_efficiency(solar_panel, capsys):
    """efficiency_calculation Test
    when a solar panel has an efficiency greater than 15"""
    solar_panel.solar_panel_level_of_the_battery = 100
    solar_panel.efficiency_calculation(2.5, 300)
    captured = capsys.readouterr()
    assert "GOOD" in captured.out


def test_tips_low_efficiency(solar_panel, capsys):
    """tips function Test
     when low efficiency."""
    efficiency = 10
    solar_panel.tips(efficiency)
    captured = capsys.readouterr()
    assert "To improve the efficiency of your solar panel" in captured.out
    assert "Optimize Orientation and Tilt" in captured.out
    assert "Avoid shadows" in captured.out
    assert "Use a Solar Tracking System" in captured.out
    assert "Add Anti-Reflection Devices" in captured.out
    assert "If none of these tips work, contact the manufacturer directly." in captured.out


def test_tips_high_efficiency(solar_panel, capsys):
    """tips function Test
     when for high efficiency."""
    efficiency = 20
    solar_panel.tips(efficiency)
    captured = capsys.readouterr()
    assert "Well, to maintain your solar panel's performance for as long as" in captured.out
    assert "possible, monitor it regularly for malfunctions, breakdowns or loss" in captured.out
    assert "of performance. Repair or replace defective components promptly." in captured.out


def test_useful_life_calculation(solar_panel, capsys):
    """useful_life_calculation function Test."""
    performance_guarantee = 3
    annual_degradation_rate = 0.5
    solar_panel.useful_life_calculation(performance_guarantee, annual_degradation_rate)
    captured = capsys.readouterr()
    expected_output = "useful life is: 6.0"
    assert expected_output in captured.out
