import os
import datetime
import cv2

def folderExist(dirPath):
    currentMonthYear = datetime.datetime.now()
    MONTH_YEAR = str(currentMonthYear.strftime("%B-%Y"))
    dirFolders = os.listdir(dirPath)
    
    if (MONTH_YEAR in dirFolders):
        return MONTH_YEAR
    
    newPath = os.path.join(dirPath, MONTH_YEAR)
    os.mkdir(newPath)
    return MONTH_YEAR


camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Initialize the camera.

nonImgError, imgData = camera.read()  # Grabs, decodes and returns the next video frame

if nonImgError:  
    
    try:
        path = ".\\RecentLogins"
        
        MONTH_YEAR = folderExist(path)
        path = f".\\RecentLogins\\{MONTH_YEAR}"
        
        date_time = datetime.datetime.now() 
        CURRENT_TIME = date_time.strftime("%b %d %Y %I:%M%p")
        
        cv2.imwrite(os.path.join(path, f"{CURRENT_TIME.replace(':', ';')}.png"), imgData) 
        
    except Exception as error:
        print("There was an error: {}".format(error))
