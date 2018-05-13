import numpy as np

class torque(array):
    t_r = -36.07956616966136 # torque coefficient for roll
    t_p = -12.14599781908070 # torque coefficient for pitch
    t_y =   8.91962804287785 # torque coefficient for yaw

t_r = -36.07956616966136 # torque coefficient for roll
t_p = -12.14599781908070 # torque coefficient for pitch
t_y =   8.91962804287785 # torque coefficient for yaw
D_r =  -4.47166302201591 # drag coefficient for roll
D_p = -2.798194258050845 # drag coefficient for pitch
D_y = -1.886491900437232 # drag coefficient for yaw

def sign(x):
    return (0. < x) - (x < 0.)
sign
aerial_inputs = {
    omega_start = np.array([])
    omega_end = np.array([])
    theta_start np.array([])
    dt = 0.
}

tau = (omega_end - omega_start) / dt

tau_local = np.dot(np.transpose(theta_start), tau)

omega_local = np.dot(np.transpose(theta_start), omega_start)

rhs = [
    tau[0] - D_r * omega_local[0],
    tau[1] - D_p * omega_local[1],
    tau[2] - D_y * omega_local[2]
]

u = [
    rhs[0] / T_r,
    rhs[1] / (T_p + sign(rhs[1]) * omega_local[1] * D_p),
    rhs[2] / (T_y - sign(rhs[2]) * omega_local[2] * D_y)
]