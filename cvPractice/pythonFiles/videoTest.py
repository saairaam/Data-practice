import cv2

# Load the Super-Resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel("../../assest/EDSR_x4.pb")  # Load pre-trained model (download required)
sr.setModel("edsr", 4)  # Set the model and scale factor

# Read and enhance the image
image = cv2.imread("../../assest/videotests/image.png")
result = sr.upsample(image)

# Save and display the result
cv2.imwrite("enhanced_image.jpg", result)
cv2.imshow("Super-Resolved Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()