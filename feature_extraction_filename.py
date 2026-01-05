# import numpy as np
# from main import *
#
# def feature_extraction_fn(fn):
#     """
#     extract feature from filename
#     """
#     # vectorize
#     im = vectorize_img(fn)
#     # project
#     im1 = np.dot(im, ProjectionMatrix)
#     # standardization
#     return feature_extraction(im1)
#
# fn1 = path + 'M-036-18.bmp'
# fn2 = path + 'W-045-01.bmp'
# fn3 = path + 'M-048-01.bmp'
# fn4 = path + 'W-027-02.bmp'
#
# x1 = feature_extraction_fn(fn1)
# p1 = logreg.predict_proba(x1)
# print(p1)
#
# x2 = feature_extraction_fn(fn2)
# p2 = logreg.predict_proba(x2)
# print(p2)
#
# x3 = feature_extraction_fn(fn3)
# p3 = logreg.predict_proba(x3)
# print(p3)
#
# x4 = feature_extraction_fn(fn4)
# p4 = logreg.predict_proba(x4)
# print(p4)
