
import cv2

# Read the input image
image = cv2.imread("objects.jpg")

if image is None:
    print("Error: Please add an image named objects.jpg")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect object edges
edges = cv2.Canny(blur, 50, 150)

# Find object contours
contours, hierarchy = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Count detected objects
count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 500:
        count += 1
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.putText(
    image, f"Objects Count: {count}", (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
)

print("Number of objects detected:", count)

cv2.imshow("Object Counting", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
