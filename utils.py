import numpy as np
import pydicom as pyd

window_center = 300
window_width = 1500
lungwin = np.array([window_center - window_width // 2., window_center + window_width // 2])

def dcm_2_img(data, intercept, slope):
    img = data.astype(np.float64) * slope
    img = img.astype(np.int16) + intercept
    newimg = (img - lungwin[0]) / (lungwin[1] - lungwin[0])
    newimg[newimg < 0] = 0
    newimg[newimg > 1] = 1
    newimg = (newimg * 255).astype('uint8')
    return newimg