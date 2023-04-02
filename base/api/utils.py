import cv2
import numpy as np
import json
from colorthief import ColorThief

def extract_strip(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200)
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    strip = image[y:y+h, x:x+w]
    return strip

def get_colors(image, num_colors=10):
    strip_height = image.shape[0] // num_colors
    colors = []
    for i in range(num_colors):
        roi = image[i * strip_height:(i + 1) * strip_height]
        cv2.imwrite('temp_roi.jpg', roi)
        color_thief = ColorThief('temp_roi.jpg')
        dominant_color = color_thief.get_color(quality=1)
        colors.append(dominant_color)
    return colors

def main(image_path):
    # image_path = '/content/image4.jpg'
    image = cv2.imread(image_path)
    strip = extract_strip(image)
    colors = get_colors(strip)
    color_labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    color_data = {color_labels[i]: colors[i] for i in range(len(colors))}
    json_data = json.dumps(color_data, indent=2)
    
    print("Colors extracted:")
    print(json_data)
