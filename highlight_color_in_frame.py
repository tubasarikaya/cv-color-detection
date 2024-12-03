import cv2
import numpy as np

def detect_color(frame, lower_bound, upper_bound):
  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    highlighted_color = cv2.bitwise_and(frame, frame, mask=color_mask)
    
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Highlighted Color", highlighted_color)

def get_hsv_bounds(color_choice):
   
    color_ranges = {
        1: (np.array([161, 155, 84]), np.array([179, 255, 255])),  # Red
        2: (np.array([94, 80, 2]), np.array([126, 255, 255])),     # Blue
        3: (np.array([25, 52, 72]), np.array([102, 255, 255]))     # Green
    }
    return color_ranges.get(color_choice)

def main():
   
    cap = cv2.VideoCapture(0)
    
    print("Color Detection Program")
    print("1: Red\n2: Blue\n3: Green")
    
    try:
        color_choice = int(input("Which color would you like to detect? (1/2/3): "))
        hsv_bounds = get_hsv_bounds(color_choice)
        
        if hsv_bounds is None:
            print("Invalid choice. The program is terminating.")
            return
        
        lower_bound, upper_bound = hsv_bounds
        print("Detecting the selected color. Press 'q' to quit.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture camera image. The program is terminating.")
                break
            
            detect_color(frame, lower_bound, upper_bound)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                print("Terminating the program...")
                break
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
