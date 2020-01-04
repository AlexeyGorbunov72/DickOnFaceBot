import dlib
import cv2
from PIL import Image
from imutils import face_utils
import numpy as np

def resize_dick(input_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size)
    original_image = original_image.convert("RGB")

    fucken_pixels = original_image.load()
    normal_pixels = []
    for i in range(original_image.size[0]):
        buffer_ = []
        for x in range(0, original_image.size[1]):
            try:
                buffer_.append(fucken_pixels[i, x])
            except:
                pass

        normal_pixels.append(buffer_)
   #for i in normal_pixels:
   #     for h in i:
   #         if h[0] == 0:
   #             print("0", end="")
   #         else:
   #             print("1", end="")
   #     print("")
    return normal_pixels




class Dick:
    p = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(p)

    frontground = cv2.imread(r"penis2.0.png")


    def penis_on_face(self, path_to_face):
        pic = cv2.imread(path_to_face)
        gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        recv = self.detector(gray, 0)

        for rec in recv:
            shape = self.predictor(gray, rec)
            shape = face_utils.shape_to_np(shape)
            (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS['mouth']
            mouth_ = cv2.convexHull(shape[mStart: mEnd])
            print(mouth_[0][0])
            self.draw_penis_around_point(mouth_[0][0], 100, pic)
        return "dick_on_face.jpg"
    def draw_penis_around_point(self, point, deltaX, pic):
        penis = resize_dick("penis0.0.0.png", deltaX, 80)


        if deltaX < point[0]:
            for y in range(point[1] - len(penis) // 2, point[1] + len(penis) // 2):

                for x in range(point[0] - deltaX, point[0]):


                    try:
                        if penis[y - point[1] + len(penis)//2][x - point[0] + deltaX][0] != 0:
                            pic[y][x] = penis[y - point[1] + len(penis)//2][x - point[0] + deltaX]
                    except:
                        pass
        cv2.imwrite("dick_on_face.jpg", pic)

