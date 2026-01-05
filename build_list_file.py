def build_list_fn(path,img_ids, view_ids):
    """
    Hàm này dùng để TẠO RA DANH SÁCH ĐƯỜNG DẪN ẢNH MỘT CÁCH TỰ ĐỘNG.

    INPUT:
        img_ids  : danh sách / mảng các ID ảnh (ví dụ: [4, 22, 100])
        view_ids : danh sách / mảng các ID góc nhìn (ví dụ: [1, 3, 10])

    OUTPUT:
        list_fn  : list các đường dẫn ảnh dạng:
                   path + "<img_id>_<view_id>.jpg"
                   ví dụ: "/data/4_1.jpg"
    """

    list_fn = []
    for im_id in img_ids:
        for v_id in view_ids:
            fn = path + str(im_id) + '_' + str(v_id) + '.jpg'
            list_fn.append(fn)
    return list_fn
