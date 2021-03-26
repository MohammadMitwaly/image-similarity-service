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

    hash0 = imagehash.average_hash(Image.open('quora_photo.jpg')) 
    hash1 = imagehash.average_hash(Image.open('twitter_photo.jpeg')) 
    cutoff = 5

    minimal_hash = image_hashes[0]
    most_similar_image = images[0]
    for hash_value, image_name in zip(image_hashes, images):
        if org_hash - hash_value < minimal_hash:
            minimal_hash = hash_value
            most_similar_image = image_name
    similarity_score = org_hash - minimal_hash
    return "Most similar image is {imagename}, with similarity of {similarity_score}".format(most_similar_image, similarity_score)
