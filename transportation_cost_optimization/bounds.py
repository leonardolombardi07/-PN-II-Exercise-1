def build_bounds():
    '''A function that defines bounds for each parameter of the optimization
   problem.


    Returns
    -------
    out : sequence, tup
        Sequence of tuples, each representing the minimum and maximum bounds
        for a specific parameter.

    Notes
    -----
    The order of the bounds of the returned sequence must match the order of
    the initial guess vector (x0) defined. The value "None" represents the
    absence of a minimum or maximum bound.
    '''

    L_bound = (0, 274.32)
    B_bound = (0, None)
    D_bound = (0, None)
    T_bound = (0, None)
    Cb_bound = (0.63, 0.75)
    Vk_bound = (14, 18)
    return (
        L_bound,
        B_bound,
        D_bound,
        T_bound,
        Cb_bound,
        Vk_bound,
    )
