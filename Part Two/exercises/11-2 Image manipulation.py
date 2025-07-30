import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the original Lenna image
lenna_image = mpimg.imread('\Users\risha\gitclones\ROAR-Academy\Part Two\notebooks\lenna.bmp')

# Load your national flag image
flag_image = mpimg.imread('images.png')

print("Lenna image shape:", lenna_image.shape)
print("Flag image shape:", flag_image.shape)



flag_height, flag_width, _ = flag_image.shape
lenna_height, lenna_width, _ = lenna_image.shape

# Calculate the starting indices for the top right corner
start_y = 0
start_x = lenna_width - flag_width

for y in range(flag_height):
    for x in range(flag_width):
        for c in range(3):  # RGB channels
            lenna_image[start_y + y, start_x + x, c] = flag_image[y, x, c]
            
plt.imshow(lenna_image)
plt.show()