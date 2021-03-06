import pickle
from os.path import join

# Where did you save the camera calibration results? pickle files
calibration_outputs_dir = 'output/camera calibration'

# Filename used to save the camera calibration result (mtx,dist)
calibration_mtx_dist_filename = 'camera_cal_dist_pickle.p'

# Filename used to save the perspective transform matrices (M, Minv)
calibration_m_minv_filename = 'perspective_trans_matrices.p'


def load_camera_mtx_dist_from_pickle():
    """
    Read in the saved camera matrix and distortion coefficients
    These are the arrays we calculated using cv2.calibrateCamera()
    """

    dist_pickle = pickle.load(open(join(calibration_outputs_dir, calibration_mtx_dist_filename), "rb"))
    mtx = dist_pickle["mtx"]
    dist = dist_pickle["dist"]

    return mtx, dist


def load_perspective_transform_from_pickle():
    """
    Read in the saved perspective transformation matrices
    These are the arrays we calculated using cv2.getPerspectiveTransform()
    """

    dist_pickle = pickle.load(open(join(calibration_outputs_dir, calibration_m_minv_filename), "rb"))
    m = dist_pickle["M"]
    minv = dist_pickle["Minv"]

    return m, minv
