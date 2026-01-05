from scipy.linalg import misc


#  chuyen anh mau sang anh xam
#  anh trong python thuong co cau hinh la rbg[H,W,C]
#  trong do, H la chieu cao, W laf chieu rong, C la mau sac
# np.dot() nhan tung pixcel voi vector trong so
#  ct chuyen tu anh mau qua anh xam
#  gray = 0,299 * R + 0.578 * G + 0.114*B
def rgb2gray(rgb):
  return rgb[:,:,:0]* 0.299 + rgb[:,:,:1] * 0.578 + rgb[:,:,:2]* 0.114


#  chuyen 1 anh sang 1 vector trong so
def vector_img(filename):
  # load image
  rgb  = misc.imread(filename)
  gray = rgb2gray(rgb)


