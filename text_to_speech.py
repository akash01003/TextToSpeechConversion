import cv2
import time
from PIL import Image
import pytesseract
import os
import pyttsx
import sys
from Engine import Engine
# Capture duration in milliseconds
capture_duration = 100000
#initalizing camera; 0:usb camera 1:web cam
camera = cv2.VideoCapture(0)
#inializing starting time of the camera and is assigned to a variable
start_time = time.time()
while True:
    #read camera image using read() and saves value to 2 temporary variables-image &amp; retutn_value
    return_value,image = camera.read()
    #convert the image to gray sacle and display the image
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow(&#39;image&#39;,gray)
    #If the time exceeds the capture time, then write image to &quot;text.jpg&quot; and camer stoppped
    if ( int(time.time() - start_time) &lt; capture_duration ):
        cv2.imwrite(&#39;test.jpg&#39;,image)
        break
camera.release()
image = cv2.imread(&quot;test.jpg&quot;)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#gaussian threshold is used to prepeocess the image and mediamBlur to remove noise from image &amp; displa
y image
gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
           cv2.THRESH_BINARY,11,3)
gray = cv2.medianBlur(gray, 3) 
      
cv2.imshow(&quot;Image&quot;, gray)
filename = &quot;{}.png&quot;.format(os.getpid())
cv2.imwrite(filename, gray)
text = Image.open(filename)
str = pytesseract.image_to_string(text, lang=&#39;eng&#39;)
os.remove(filename)
print(str)
cv2.imshow(&quot;Image&quot;, image)
cv2.imshow(&quot;Output&quot;, gray)
cv2.waitKey(0)
cv2.destroyAllWindows()