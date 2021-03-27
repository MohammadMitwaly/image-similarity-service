from PIL import Image
import imagehash

def compare_imagehash_demo():
    original = "org-colosseum.jpg"  
    images = ["colosseum-1.jpg","colosseum-2.jpg","colosseum-3.jpg","colosseum-4.jpg","colosseum-5.jpg"]
    image_hashes = []
    cutoff_value = 5
    org_hash = imagehash.average_hash(Image.open("src/data/{filename}".format(filename=original))) 

    for image in images:
        image_hashes.append(imagehash.average_hash(Image.open("src/data/{filename}".format(filename=image))))

    minimal_hash = org_hash - image_hashes[0]
    print(minimal_hash)
    most_similar_image = images[0]
    for hash_value, image_name in zip(image_hashes, images):
        comparison_value = org_hash - hash_value
        if comparison_value < minimal_hash:
            minimal_hash = comparison_value
            most_similar_image = image_name
    # If the output is 0 that means the images are identical, 
    # here we map the values from 0 to 100, where 100 == identical images
    similarity_score = abs(minimal_hash-100)
    return "Most similar image is {imagename}, with similarity of {similarity_score}".format(imagename=most_similar_image, similarity_score=similarity_score)
