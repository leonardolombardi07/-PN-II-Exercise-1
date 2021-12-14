
from formulas import *
from parameters import round_trip_miles, handling_rate, fuel_price


def transportation_cost_function(x):
    '''A function that calculates the transportation cost from a set
    of parameters.

    Parameters
    -------
    x : list
        A list of parameters whose order matches what was defined in 
        the initial guess vector (x0)

    Returns
    -------
    out : float
        The value of the transportation cost calculated from given parameters
    '''
    L, B, D, T, Cb, Vk = x

    # Power
    displacement = get_displacement(L, B, T, Cb)
    V, froude_number = get_V(Vk), get_froude_number(Vk, L)
    power = get_power(Cb, displacement, V, froude_number)

    # Weights
    steel_weight = get_steel_weight(L, B, D, Cb)
    outfit_weight = get_outfit_weight(L, B, D, Cb)

    # General (TODO: give a better name for this category of calculations)
    DWT = get_DWT(L, B, T, D, Cb, Vk)
    sea_days = get_sea_days(round_trip_miles, Vk)
    daily_consumption = get_daily_consumption(power)
    fuel_carried = get_fuel_carried(daily_consumption, sea_days)
    miscellaneous_DWT = get_miscellaneous_DWT(DWT)
    cargo_DWT = get_cargo_DWT(DWT, fuel_carried, miscellaneous_DWT)

    port_days = get_port_days(cargo_DWT, handling_rate)
    round_trips_per_year = get_round_trips_per_year(sea_days, port_days)

    # Costs
    port_cost = get_port_cost(DWT)
    fuel_cost = get_fuel_cost(daily_consumption, sea_days, fuel_price)
    voyage_costs = get_voyage_costs(fuel_cost, port_cost, round_trips_per_year)
    running_cost = get_running_cost(DWT)
    ship_cost = get_ship_cost(steel_weight, outfit_weight, power)
    capital_costs = get_capital_costs(ship_cost)
    annual_cost = get_annual_cost(capital_costs, running_cost, voyage_costs)
    annual_cargo = get_annual_cargo(cargo_DWT, round_trips_per_year)

    return get_transportation_cost(annual_cost, annual_cargo)
