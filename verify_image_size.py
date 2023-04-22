import cv2

image = cv2.imread("128_imgz/data/imgs/flip_horizontal_random_brightness_0b19576e733d483dbcb846495384eef1.jpg")
print(image.shape)
image = cv2.imread("128_imgz/data/masks/flip_horizontal_random_brightness_0b19576e733d483dbcb846495384eef1_mask.png")
print(image.shape)
image = cv2.imread("256_imgz/data/imgs/flip_horizontal_random_brightness_0c4c7b1822464dbf8ac9f25eb2c3f6d5.jpg")
print(image.shape)
image = cv2.imread("256_imgz/data/masks/flip_horizontal_random_brightness_0c4c7b1822464dbf8ac9f25eb2c3f6d5_mask.png")
print(image.shape)