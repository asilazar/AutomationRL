import numpy as np

number_of_states_x = 6
number_of_states_y = 9
number_of_states_amp = 4
number_of_states_ang = 8
factor_amp = 20
factor_ang = 45
g = 9.8
mass = 0.01  # 10 grams
uk = 0.2  # friction coefficient
a = uk * g


def get_next_movement(pos_x, pos_y, vel_x, vel_y, dim_x, dim_y, delta_t):
    pos_x = pos_x + vel_x * delta_t
    pos_y = pos_y + vel_y * delta_t
    vel_x = vel_x - np.sign(vel_x) * a * delta_t
    vel_y = vel_y - np.sign(vel_y) * a * delta_t

    if pos_y < 0:
        pos_y = -pos_y
    elif pos_y > dim_y:
        pos_y = dim_y - (pos_y - dim_y)
    return pos_x, pos_y, vel_x, vel_y


def get_next_movement_positions(pos_x, pos_y, vel_angle, vel_amplitude, dim_x, dim_y, delta_t):
    vel_x = vel_amplitude * np.cos(vel_angle)
    vel_y = vel_amplitude * np.sign(vel_angle)
    pos_x, pos_y, vel_x, vel_y = get_next_movement(pos_x, pos_y, vel_x, vel_y, dim_x, dim_y, delta_t)
    vel_amplitude = np.sqrt(np.power(vel_x, 2) + np.power(vel_y, 2))
    vel_angle = np.arctan2(vel_y, vel_x) * 180 / np.pi
    if vel_angle < 0:
        vel_angle = vel_angle + 360
    state_x = int(pos_x / (dim_x / number_of_states_x))
    state_y = int(pos_y / (dim_y / number_of_states_y))

    state_amp = int(vel_amplitude / factor_amp)
    if state_amp > number_of_states_amp - 1:
        state_amp = number_of_states_amp - 1
    state_ang = int(vel_angle / factor_ang)
    if state_ang > number_of_states_ang - 1:
        state_ang = number_of_states_ang - 1
    return state_x, state_y, state_amp, state_ang

