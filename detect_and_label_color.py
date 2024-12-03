import numpy as np
import cv2

COLOR_RANGES = {

    "Red": {"lower": np.array([136, 87, 111], np.uint8), "upper": np.array([180, 255, 255], np.uint8)},
    "Green": {"lower": np.array([25, 52, 72], np.uint8), "upper": np.array([102, 255, 255], np.uint8)},
    "Blue": {"lower": np.array([94, 80, 2], np.uint8), "upper": np.array([120, 255, 255], np.uint8)},
    "Yellow": {"lower": np.array([22, 60, 200], np.uint8), "upper": np.array([60, 255, 255], np.uint8)},
}

KERNEL = np.ones((5, 5), "uint8")

def apply_color_mask(hsv_frame, color_name, color_range):
  
    mask = cv2.inRange(hsv_frame, color_range["lower"], color_range["upper"])
    mask = cv2.dilate(mask, KERNEL)
    return mask


def detect_and_label_color(image_frame, mask, color_name, bounding_box_color):
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300: 
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image_frame, (x, y), (x + w, y + h), bounding_box_color, 2)
            cv2.putText(image_frame, f"{color_name} Color", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, bounding_box_color, 2)

def main():
    
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Kamera açılırken bir hata oluştu!")
        return

    try:
        while True:
            ret, frame = webcam.read()
            if not ret:
                print("Kamera görüntüsü alınamadı.")
                break

            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            for color_name, color_range in COLOR_RANGES.items():
                mask = apply_color_mask(hsv_frame, color_name, color_range)
                bounding_box_color = {
                    "Red": (0, 0, 255),
                    "Green": (0, 255, 0),
                    "Blue": (255, 0, 0),
                    "Yellow": (0, 255, 255),
                }[color_name]
                detect_and_label_color(frame, mask, color_name, bounding_box_color)

            cv2.imshow("Color Detection", frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                print("Çıkış yapılıyor...")
                break
    finally:
        webcam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
