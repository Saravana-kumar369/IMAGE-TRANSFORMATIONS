![image](https://github.com/user-attachments/assets/27cd3887-8713-4d06-9aad-f39e1c71aa78)# IMAGE-TRANSFORMATIONS


## Aim
To perform image transformation such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping using OpenCV and Python.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
<br>

### Step2:
<br>

### Step3:
<br>

### Step4:
<br>

### Step5:
<br>

## Program:
```python
Developed By: SARAVANA KUMAR M
Register Number: 212222230133

import numpy as np
import cv2
import matplotlib.pyplot as plt

input_img = cv2.imread("image1.webp")
# cv2.imshow("image webp",input_img)
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(input_img)
plt.show()

i)Image Translation

rows, cols, dim = input_img.shape
M = np.float32([[1, 0, 20],
                [0, 1, 50],
                [0, 0, 1]])

translated_img = cv2.warpAffine(input_img, M[:2], (cols, rows))

plt.axis('off')
plt.imshow(translated_img)
plt.show()

ii) Image Scaling

scale_factor = 1.5
M_scale = np.float32([[scale_factor, 0, 0],
                      [0, scale_factor, 0],
                      [0, 0, 1]])

scaled_img = cv2.warpAffine(input_img, M[:2], (int(cols*scale_factor), int(rows*scale_factor)))

plt.axis('off')
plt.imshow(scaled_img)
plt.show()


iii)Image shearing

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


iv)Image Reflection

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



v)Image Rotation




vi)Image Cropping





```
## Output:
### ORIGINAL IMAGE
<BR>

![image](https://github.com/user-attachments/assets/3cd5b5bd-0fed-4bcd-8dd9-caebcbcf580c)

<BR>
### i)Image Translation
<br>

![image](https://github.com/user-attachments/assets/724e5d77-3f9d-4190-aaf5-28805aebcc79)

<br>

### ii) Image Scaling
<br>

![image](https://github.com/user-attachments/assets/780a0d81-5247-44cd-8fca-05edac24acb1)

<br>


### iii)Image shearing
<br>

![image](https://github.com/user-attachments/assets/06c4a969-a162-485f-9d14-6b7bc45e5a7e)

<br>


### iv)Image Reflection
<br>

![image](https://github.com/user-attachments/assets/2d229121-7e48-440a-bf16-67d7adeb54e2)

<br>



### v)Image Rotation
<br>
<br>
<br>
<br>



### vi)Image Cropping
<br>
<br>
<br>
<br>




## Result: 

Thus the different image transformations such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping are done using OpenCV and python programming.
