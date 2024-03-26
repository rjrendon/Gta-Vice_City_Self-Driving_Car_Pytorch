import cv2
from pynput import keyboard
import time
import os

# Initialize image counters
forward_img_num = 0
left_img_num = 0
brake_img_num = 0
right_img_num = 0

# Create directories if they don't exist
os.makedirs('raw/train/forward', exist_ok=True)
os.makedirs('raw/train/left', exist_ok=True)
os.makedirs('raw/train/brake', exist_ok=True)
os.makedirs('raw/train/right', exist_ok=True)

training_folder = "raw/train"

# Create the training data folders if they don't exist
os.makedirs(os.path.join(training_folder, "forward"), exist_ok=True)
os.makedirs(os.path.join(training_folder, "left"), exist_ok=True)
os.makedirs(os.path.join(training_folder, "brake"), exist_ok=True)
os.makedirs(os.path.join(training_folder, "right"), exist_ok=True)

def grab_camera():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 for the default camera, change if you have multiple cameras
    
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None
    
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Release the camera
    cap.release()
    
    # Check if frame is captured successfully
    if not ret:
        print("Error: Camera not found.")
        return None
    
    # Resize the frame to 224x224
    frame_resized = cv2.resize(frame, (80, 90))
    
    return frame_resized

def on_press(key):
    global forward_img_num, left_img_num, brake_img_num, right_img_num
    try:
        if key.char == 'w':
            forward_img_num += 1
            frame = grab_camera()
            # if frame is not None:
            img_dir = os.path.join(training_folder, 'forward', f'forward_{forward_img_num}.jpg')
            cv2.imwrite(img_dir, frame)
            print("Saved To:", img_dir)
           
            
        elif key.char == 'a':
            left_img_num += 1
            frame = grab_camera()
            # if frame is not None:
            img_dir = os.path.join(training_folder, 'left', f'left_{left_img_num}.jpg')
            cv2.imwrite(img_dir, frame)
            print("Saved To:", img_dir)
            
        elif key.char == 's':
            brake_img_num += 1
            frame = grab_camera()
            # if frame is not None:     
            img_dir = os.path.join(training_folder, 'brake', f'brake_{brake_img_num}.jpg')
            cv2.imwrite(img_dir, frame)
            print("Saved To:", img_dir)
            
        elif key.char == 'd':
            right_img_num += 1
            frame = grab_camera()
            # if frame is not None:
            img_dir = os.path.join(training_folder, 'right', f'right_{right_img_num}.jpg')
            cv2.imwrite(img_dir, frame)
            print("Saved To:", img_dir)

    except AttributeError:
        if key == keyboard.Key.delete:
            return False

if __name__ == "__main__":
    
    # pause while changing to GTA window
    time.sleep(4)
    
    # Monitor keypress
    print("Go Drive Now!!!!!!!")
    with keyboard.Listener(on_press) as listener:
        listener.join()
        
    print(forward_img_num)
    print(left_img_num)
    print(brake_img_num)
    print(right_img_num)
    print("Total images saved:", forward_img_num + left_img_num + brake_img_num + right_img_num)