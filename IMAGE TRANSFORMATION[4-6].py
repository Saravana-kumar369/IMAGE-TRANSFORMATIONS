
##iv)Image Reflection
import numpy as np
import cv2
import matplotlib.pyplot as plt
input_image=cv2.imread("got.jpg") 
input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
plt.axis("off") 
plt.imshow(input_image)
plt.show()
M_x = np.float32([[-1, 0, cols],
                  [0, 1, 0],
                  [0, 0, 1]])

reflected_img_xaxis = cv2.warpAffine(input_img, M_x[:2], (cols, rows))

plt.axis("off")
plt.imshow(reflected_img_xaxis)
plt.show()

M_y = np.float32([[1, 0, 0],
                  [0, -1, rows],
                  [0, 0, 1]])

reflected_img_yaxis = cv2.warpAffine(input_img, M_y[:2], (cols, rows))

plt.axis("off")
plt.imshow(reflected_img_yaxis)
plt.show()


##v)Image Rotation:
import numpy as np
import cv2
import matplotlib.pyplot as plt
input_image=cv2.imread("got.jpg") 
input_image=cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
angle=np.radians(45)
M = np.float32([[np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0]])
center = (cols // 2, rows // 2)
M = cv2.getRotationMatrix2D(center, -60, 1.0)
rotated_img = cv2.warpAffine(input_img, M, (cols, rows))

plt.axis('off')
plt.imshow(rotated_img)
plt.show()

##vi)Image Cropping:

import numpy as np
import cv2
import matplotlib.pyplot as plt
input_image=cv2.imread("got.jpg") 
input_image=cv2.cvtColor(input_image,cv2.COLOR_BGR2RGB)
cropped_img = input_img[50:200, 200:400]
plt.axis('off')
plt.imshow(cropped_img)
plt.show()
