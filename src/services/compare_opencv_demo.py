import cv2 
import operator

def compare_opencv_demo():
    original = "org-colosseum.jpg"  
    images = ["colosseum-1.jpg","colosseum-2.jpg","colosseum-3.jpg","colosseum-4.jpg","colosseum-5.jpg"]
    historgrams = []
    similarity_map = {}

    org_image_file = cv2.imread("./data/{filename}".format(filename=original)) 
    gray_image = cv2.cvtColor(org_image_file, cv2.COLOR_BGR2GRAY) 
    org_histogram = cv2.calcHist([gray_image], [0],  
                            None, [256], [0, 256]) 

    for image in images:
        imageFile = cv2.imread("./data/{filename}".format(filename=image))
        gray_image = cv2.cvtColor(imageFile, cv2.COLOR_BGR2GRAY) 
        histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        historgrams.append(histogram)

    c1 = 0
    for histogram, image in zip(historgrams, images):
        i = 0
        c1 = 0
        while i<len(org_histogram) and i<len(histogram): 
            c1+=(org_histogram[i]-histogram[i])**2
            i+= 1
        c1 = c1**(1 / 2)
        similarity_map[image] = c1

    most_similar_image = min(similarity_map.items(), key=operator.itemgetter(1))[0]
    return("The most similar image to the original is: {most_similar_image}".format(most_similar_image=most_similar_image))