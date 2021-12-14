from constants import p, g


##############################################################################
# This file contains functions corresponding to formulas defined by the
# computational model used. The decision to define formulas in a separate
# file was intended to allow code reusability if any formula is used in more
# than one place.
##############################################################################

# TODO: Put all functions with the fundamental ship parameters as only arguments

def get_DWT(L, B, T, D, Cb, Vk):
    displacement = get_displacement(L, B, T, Cb)
    V, froude_number = get_V(Vk), get_froude_number(Vk, L)
    power = get_power(Cb, displacement, V, froude_number)
    lightship_weight = get_lightship_weight(
        get_steel_weight(L, B, D, Cb),
        get_outfit_weight(L, B, D, Cb),
        get_machinery_weight(power)
    )
    return displacement - lightship_weight


def get_V(Vk):
    return 0.5144*Vk


def get_displacement(L, B, T, Cb):
    return p*L*B*T*Cb


def get_froude_number(Vk, L):
    V = get_V(Vk)
    return V / ((g*L) ** 0.5)


def get_power(Cb, displacement, V, froude_number):
    a = 4977.06*(Cb ** 2) - 8105.61*Cb + 4456.51
    b = -10847.2*(Cb ** 2) + 12817*Cb - 6960.32
    return (displacement ** (2/3))*(V ** 3) / (a + b*froude_number)


def get_steel_weight(L, B, D, Cb):
    return 0.034*(L**1.7)*(B**0.7)*(D**0.4)*(Cb**0.5)


def get_outfit_weight(L, B, D, Cb):
    return (L ** 0.8)*(B ** 0.6)*(D ** 0.3)*(Cb ** 0.1)


def get_machinery_weight(power): return 0.17*(power ** 0.9)


def get_lightship_weight(steel_weight, outfit_weight, machinery_weight):
    return steel_weight + outfit_weight + machinery_weight


def get_sea_days(round_trip_miles, Vk):
    return round_trip_miles/(24*Vk)


def get_daily_consumption(power):
    return 0.19*power*24/1000 + 0.2


def get_fuel_carried(daily_consumption, sea_days):
    return daily_consumption*(sea_days+5)


def get_miscellaneous_DWT(DWT):
    return 2*(DWT ** 0.5)


def get_cargo_DWT(DWT, fuel_carried, miscellaneous_DWT):
    return DWT-fuel_carried-miscellaneous_DWT


def get_port_days(cargo_DWT, handling_rate):
    return 2*((cargo_DWT/handling_rate)+0.5)


def get_round_trips_per_year(sea_days, port_days):
    return 350/(sea_days+port_days)


def get_port_cost(DWT):
    return 6.3*(DWT ** 0.8)


def get_fuel_cost(daily_consumption, sea_days, fuel_price):
    return 1.05*daily_consumption*sea_days*fuel_price


def get_voyage_costs(fuel_cost, port_cost, round_trips_per_year):
    return (fuel_cost+port_cost)*round_trips_per_year


def get_running_cost(DWT):
    return 40000*(DWT ** 0.3)


def get_ship_cost(steel_weight, outfit_weight, power):
    return 1.3*(2000*steel_weight + 3500 *
                outfit_weight + 2400*(power ** 0.8))


def get_capital_costs(ship_cost): return 0.2*ship_cost


def get_annual_cost(capital_costs, running_cost, voyage_costs):
    return capital_costs + running_cost + voyage_costs


def get_annual_cargo(cargo_DWT, round_trips_per_year):
    return cargo_DWT*round_trips_per_year


def get_transportation_cost(annual_cost, annual_cargo):
    return annual_cost/annual_cargo


def get_KB(T):  # Vertical Centre of Buoyancy
    return 0.53*T


def get_BMt(Cb, B, T):  # Metacentric Radius
    return (0.085*Cb - 0.002)*(B ** 2)/(T+Cb)


def get_KG(D):  # Vertical Centre of Gravity
    return 1 + 0.52*D


def get_GMt(KB, BMt, KG):  # Metacentric Height
    return KB + BMt - KG
