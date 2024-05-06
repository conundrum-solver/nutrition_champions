import os
from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(student_id):
    # Construct the filename based on the student ID
    filename = os.path.join('media/qr_codes/', f"{student_id}.png")
    #filename = os.path.join('media/qr_codes/qr_code_01_0BVZiCw.png')
    print("Attempting to decode QR code from file: ", filename)
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"QR code image '{filename}' not found.")
        return None
    
    try:
        # Open the QR code image
        with open(filename, 'rb') as image_file:
            print("QR code image file opened sucessfully.")
            # Decode the QR code image
            decoded_objects = decode(Image.open(image_file))
            #decoded_objects = decode('qr_code_01_0BVZiCw.png')
            print("Decoded objects: ", decoded_objects)
            # Extract the decoded data (assuming only one QR code in the image)
            if decoded_objects:
                decoded_data = decoded_objects[0].data.decode('utf-8')
                print("Decoded QR data: ", decoded_data)
                if decoded_data == student_id:
                    return decoded_data
                else:
                    print("Decoded student ID does not match the requested student ID.")
                    return None
            else:
                print("Decoded not done correctly!")
                return None
        
        
        
    except FileNotFoundError:
        print(f"QR code image '{filename}' not found.")
        return None
