# Import the os module to interact with the operating system and the DeepFace module for face recognition.
import os
from deepface import DeepFace

# Initialize variables to track the smallest distance and whether a match is found.
small_distance = None
match_found = False

# Loop through all files in the 'Samples' folder.
for file in os.listdir("Samples"):
    # Check if the file is a JPG image.
    if file.endswith(".jpg"):
        try:
            # Attempt to verify if the test image matches the current sample image.
            result = DeepFace.verify("<%IMAGE_WHICH_HAS_TO_BE_MATCHED%>", f"TrainedImage/{file}")
        except Exception as e:
            # Print an error message if there is an issue processing the image.
            print(f"Error processing {file}: {str(e)}")
            continue
        
        # Check if the faces are verified as the same person.
        if result["verified"]:
            # Print the name of the person if a match is found and set the match_found flag to True.
            print("This Person Looks exactly Like ", file.split(".")[0])
            match_found = True
            break
        
        # Update the smallest distance if it's not set or if the current distance is smaller.
        if small_distance is None:
            small_distance = (file.split(".")[0], result['distance'])
        else:
            small_distance = (file.split(".")[0], result['distance']) if result["distance"] < small_distance[1] else (file.split(".")[0], result['distance'])
    else:
        # Print a message indicating that no exact match is found if the file is not a JPG image.
        print(f"No exact Match Found! Closest Match is {small_distance[0]}")

# If no match is found in any of the files, print a message indicating that.
if not match_found:
    print("No match found in any of the files in the 'Samples' folder.")
