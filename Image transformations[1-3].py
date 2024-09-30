
##i)Image Translation
import numpy as np
import cv2
import matplotlib.pyplot as plt
input_img=cv2.imread("color image of flower.jpg")
input_img=cv2.cvtColor(input_img,cv2.)
plt.axis('off')
plt.imshow(input_img)
plt.show()
rows,cols,dim=input_img.shape
M=np.float32([[1,0,20],
             [0,1,50],
             [0,0,1]])
translated_img = cv2.warpAffine(input_img, M[:2], (cols, rows))

plt.axis('off')
plt.imshow(translated_img)
plt.show()


##ii)Image Scaling

scale_factor = 1.5
M_scale = np.float32([[scale_factor, 0, 0],
                      [0, scale_factor, 0],
                      [0, 0, 1]])

scaled_img = cv2.warpAffine(input_img, M[:2], (int(cols*scale_factor), int(rows*scale_factor)))

plt.axis('off')
plt.imshow(scaled_img)
plt.show()


##iii)Image Shearing
M_x = np.float32([[1, 0.2, 0],
                  [0, 1, 0],
                  [0, 0, 1]])

sheared_img_xaxis = cv2.warpAffine(input_img, M_x[:2], (cols, rows))

plt.axis('off')
plt.imshow(sheared_img_xaxis)
plt.show()

M_y = np.float32([[1, 0, 0],
                  [0.2, 1, 0],
                  [0, 0, 1]])

sheared_img_yaxis = cv2.warpAffine(input_img, M_y[:2], (cols, rows))

plt.axis('off')
plt.imshow(sheared_img_yaxis)
plt.show()





