import cv2
img = cv2.imread('../assest/waterbodies/waterbody3.png')
while True: 

    cv2.imshow("img",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()