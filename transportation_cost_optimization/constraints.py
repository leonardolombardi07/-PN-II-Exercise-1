def build_constraints():
    '''A function that builds constraints relating two or more parameters
    defined for the optimization problem.


    Returns
    -------
    out : sequence, dict
        Sequence of dictionaries, each representing a specif constraint
        and containing the keys "type" and "fun".

        "type" : {"eq", "ineq"}
            Determines if it is an equality or inequality constraint 

        "fun" : callable
            The function defining the constraint. It receives a vector x with
            all parameters (in the order as defined by the initial guess, x0).
            Equality constraint means that the constraint function result is to
            be zero (fun(x) == 0) whereas inequality means that it is to be 
            non-negative (f(x) >= 0).

    See Also
    --------
    https://stackoverflow.com/questions/42303470/scipy-optimize-inequality-constraint-which-side-of-the-inequality-is-considere/42304099

    Notes
    -----
    Constraints typically don't need a builder function like this and are 
    more succinctly defined with "func" being a lambda function. The decision to
    create the build_constraints function was to try to make it easier to understand
    how constraints are defined in Scipy and to clarify where each constraint of the
    problem was defined.
    '''

    def L_and_B(x):
        '''L/B >= 6'''
        L, B = x[0], x[1]
        return L/B - 6

    def L_and_D(x):
        '''L/D  <= 15'''
        L, D = x[0], x[2]
        return 15 - L/D

    def L_and_T(x):
        '''L/T <= 19'''
        L, T = x[0], x[3]
        return 19 - L/T

    def T_and_DWT(x):
        '''T <= 0.45DWT^0,31'''
        T, DWT = x[3], x[6]
        return 0.45*DWT*(DWT**0.32) - T

    def T_and_D(x):
        '''T <= 0.7D + 0.7'''
        D, T = x[2], x[3]
        return 0.7*D + 0.7 - T

    def stability_condition(x):
        '''GMt >= 0.07B'''
        B, GMt = x[1], x[7]
        return GMt - 0.07*B

    return (
        {'type': 'ineq', 'fun': L_and_B},
        {'type': 'ineq', 'fun': L_and_D},
        {'type': 'ineq', 'fun': L_and_T},
        {'type': 'ineq', 'fun': T_and_DWT},
        {'type': 'ineq', 'fun': T_and_D},
        {'type': 'ineq', 'fun': stability_condition},
    )
