from constants import g

# Fundamental Ship Parameters
L = 55  # Length
B = 5  # Breadth
D = 10  # Depth
T = 5  # Draught
Cb = 0.7  # Block Coefficient
Vk = 14  # TODO - what is Vk?
DWT = 100000  # Deadweight

# Derived Ship Parameters
KB = 0.53*T  # Vertical Centre of Buoyancy
BMt = (0.085*Cb - 0.002)*(B ** 2)/(T+Cb)  # Metacentric Radius
KG = 1 + 0.52*D  # Vertical Centre of Gravity
GMt = KB + BMt - KG  # Metacentric Height

V = 0.5144*Vk  # TODO: is this the service speed?
froude_number = V / ((g*L) ** 0.5)
