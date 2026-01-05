import numpy as np
from build_list_file import build_list_fn
from imageio.plugins.pillow_legacy import pil_try_read
from sklearn import linear_model           # for logistic regression
from sklearn.metrics import accuracy_score # for evaluation
from scipy import misc                     # for loading image
np.random.seed(1)

path = '/home/nghung/Learn/MachineLearning/Binary_classifiers/data/'
# np.arange(start, end, step) -> tao ra mang
# np.hstack() -> gop hai mang lai voi nhau
# tao id anh
train_ids = np.arange(1, 26)
test_ids  = np.arange(26, 30)

# tạo ID góc nhìn
view_ids = np.hstack((train_ids, test_ids))


# sinh danh sách file
file_list = build_list_fn(path, train_ids, view_ids)

# in ra thử 10 file đầu
for f in file_list[:10]:
    print(f)
