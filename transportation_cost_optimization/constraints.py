from formulas import *


def build_constraints():
    '''A function that builds constraints relating two or more parameters
    or bounds that need to be calculated from the set of parameters (x0 or x)


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
    def DWT_lower_bound(x):
        ''' DWT >= 500000'''
        L, B, D, T, Cb, Vk = x[0], x[1], x[2], x[3], x[4], x[5]
        DWT = get_DWT(L, B, D, T, Cb, Vk)
        return DWT - 25000  # >= 0

    def DWT_upper_bound(x):
        ''' DWT <= 500000'''
        L, B, D, T, Cb, Vk = x[0], x[1], x[2], x[3], x[4], x[5]
        DWT = get_DWT(L, B, D, T, Cb, Vk)
        return 500000 - DWT  # >= 0

    def L_and_B(x):
        '''L/B >= 6'''
        L, B = x[0], x[1]
        return L/B - 6  # >= 0

    def L_and_D(x):
        '''L/D  <= 15'''
        L, D = x[0], x[2]
        return 15 - L/D  # >= 0

    def L_and_T(x):
        '''L/T <= 19'''
        L, T = x[0], x[3]
        return 19 - L/T  # >= 0

    def T_and_DWT(x):
        '''T <= 0.45DWT^0,31'''
        L, B, D, T, Cb, Vk = x[0], x[1], x[2], x[3], x[4], x[5]
        DWT = get_DWT(L, B, T, D, Cb, Vk)
        return 0.45*(DWT**0.32) - T  # >= 0

    def T_and_D(x):
        '''T <= 0.7D + 0.7'''
        D, T = x[2], x[3]
        return 0.7*D + 0.7 - T  # >= 0

    def stability_constraint(x):
        '''GMt >= 0.07B'''
        B, D, T, Cb = x[1], x[2], x[3], x[4]
        KB = get_KB(T)
        BMt = get_BMt(Cb, B, T)
        KG = get_KG(D)
        GMt = get_GMt(KB, BMt, KG)
        return GMt - 0.07*B  # >= 0

    def froude_number_constraint(x):
        '''froude_number <= 0.32'''
        L, Vk = x[0], x[5]
        froude_number = get_froude_number(Vk, L)
        return 0.32 - froude_number  # >= 0

    return (
        {'type': 'ineq', 'fun': DWT_lower_bound},
        {'type': 'ineq', 'fun': DWT_upper_bound},
        {'type': 'ineq', 'fun': L_and_B},
        {'type': 'ineq', 'fun': L_and_D},
        {'type': 'ineq', 'fun': L_and_T},
        {'type': 'ineq', 'fun': T_and_DWT},
        {'type': 'ineq', 'fun': T_and_D},
        {'type': 'ineq', 'fun': stability_constraint},
        {'type': 'ineq', 'fun': froude_number_constraint},
    )
