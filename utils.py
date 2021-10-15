import numpy as np

def displayMathHelper(num_iters, curr_iter):
    final_iter_magnitude = np.floor(np.log10(num_iters)).astype(np.int32)
    magnitude = np.floor(np.log10(curr_iter)).astype(np.int32)
    n_digits = magnitude + 1
    final_iter_n_digits = final_iter_magnitude + 1

    if magnitude == final_iter_magnitude:
        space_str=0*'\ '
    else:
        space_str = (final_iter_n_digits-np.floor(np.log10(curr_iter)).astype(np.int32))*'\ '

    return space_str