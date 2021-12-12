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
    L, B, D, T, Cb, Vk, DWT, GMt, froude_number = x

    # Power
    V = 0.5144*Vk
    displacement = 1.025*L*B*T*Cb
    a = 4977.06*(Cb ** 2) - 8105.61*Cb + 4456.51
    b = -10847.2*(Cb ** 2) + 12817*Cb - 6960.32
    power = (displacement ** (2/3))*(V ** 3) / (a + b*froude_number)

    # Weights
    steel_weight = 0.034*(L**1.7)*(B**0.7)*(D**0.4)*(Cb**0.5)
    outfit_weight = (L ** 0.8)*(B ** 0.6)*(D ** 0.3)*(Cb ** 0.1)

    # We commented the lines containing the variables below because, although
    # they were mentioned in problem assignment, they are not used in our program.
    # machinery_weight = 0.17*(power ** 0.9)
    # ligthship_weight = steel_weight + outfit_weight + machinery_weight

    # General (TODO: give a better name for this category of calculations)
    round_trip_miles = 5000
    sea_days = round_trip_miles/(24*Vk)
    daily_consumption = 0.19*power*24/1000 + 0.2
    fuel_carried = daily_consumption*(sea_days+5)
    miscellaneous_DWT = 2*(DWT ** 0.5)
    cargo_DWT = DWT-fuel_carried-miscellaneous_DWT
    handling_rate = 8000
    port_days = 2*((cargo_DWT/handling_rate)+0.5)
    round_trips_per_year = 350/(sea_days+port_days)

    # Costs
    port_cost = 6.3*(DWT ** 0.8)
    fuel_price = 100
    fuel_cost = 1.05*daily_consumption*sea_days*fuel_price
    voyage_costs = (fuel_cost+port_cost)*round_trips_per_year
    running_cost = 40000*(DWT ** 0.3)
    ship_cost = 1.3*(2000*steel_weight + 3500 *
                     outfit_weight + 2400*(power ** 0.8))
    capital_costs = 0.2*ship_cost

    annual_cost = capital_costs + running_cost + voyage_costs
    annual_cargo = cargo_DWT*round_trips_per_year

    transportation_cost = annual_cost/annual_cargo
    return transportation_cost
