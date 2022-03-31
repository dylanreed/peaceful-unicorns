from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Diagonal","Diagonal with Stars","Horizontal","Horizontal with Stars","Spiral 1","Spiral 1 with Stars","Spiral 2","Spiral 2 with Stars","Spiral 3","Spiral 3 with Stars","Vertical","Vertical with Stars"] 
background_weights = [0.09, 0.08, 0.09, 0.08, 0.09, 0.08, 0.09, 0.08, 0.08, 0.08, 0.08, 0.08]

body = ["Blue","Green","Grey","Indigo","Orange","Red","Violet","Yellow"] 
body_weights = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

cloud = ["Yes","No"] 
cloud_weights = [0.1, 0.9]

stars = ["None","Even More","More","Some"] 
stars_weights = [0.90, 0.06, 0.03, 0.1]

spots = ["Blank","Bright Pink","Dark Purple","Green Shimmer","Green Shine","Green Tourquise Shimmer","Green","Pearlescence","Pink","Pinkish Orange","Pretty Purple","Purplish Blue","Royal Purple","Salmon","Shimmer","Sky Blue","Yellow Green","Aqua Green"] 
spots_weights = [0.6, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0375, 0.0111, 0.0375, 0.0376, 0.0111, 0.0111, 0.0111, 0.0111, 0.0111, 0.0111, 0.0111, 0.0111]

horn = ["Big Rainbow","Small Rainbow","Ukraine Stripes","Ukraine"] 
horn_weights = [0.2, 0.2, 0.3, 0.3]

tail = ["Long Rainbow","Long Ukraine","Short Rainbow","Short Ukraine","Speedy Rainbow","Speedy Ukraine"] 
tail_weights = [0.15, 0.18, 0.15, 0.18, 0.15, 0.19]

mane = ["Blue Spikes","Curly Rainbow","Curly Ukraine","Lime Spikes","Orange Spikes","Pink Spikes","Purple Spikes","Rainbow Updo","Red Spikes","Short Rainbow","Short Ukraine","Sleek Rainbow","Sleek Ukraine","Ukraine Updo","Yellow Spikes"] 
mane_weights = [0.06, 0.07, 0.07, 0.06, 0.06, 0.06, 0.06, 0.07, 0.06, 0.07, 0.07, 0.07, 0.08, 0.08, 0.06]

eyes = ["Half Closed","Wide Awake","Wink"]  
eyes_weights = [0.1, 0.8, 0.1]

mouth = ["Happy","Hmm","Oh","Smile"]  
mouth_weights = [0.4, 0.1, 0.1, 0.4]

flash = ["Banana","None","Cream","Lavender","Mint","Peach","White"]  
flash_weights = [0.05, 0.7, 0.05, 0.05, 0.05, 0.05, 0.05]

blush = ["Dark","Medium","Light","None"]  
blush_weights = [0.1, 0.1, 0.1, 0.7]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "Diagonal":"diagonal",
    "Diagonal with Stars":"diagonal_stars",
    "Horizontal":"horizontal",
    "Horizontal with Stars":"horizontal_stars",
    "Spiral 1":"spiral_1",
    "Spiral 1 with Stars":"spiral_1_stars",
    "Spiral 2":"spiral_2",
    "Spiral 2 with Stars":"spiral_2_stars",
    "Spiral 3":"spiral_3",
    "Spiral 3 with Stars":"spiral_3_stars",
    "Vertical":"vertical",
    "Vertical with Stars":"vertical_stars"
}

body_files = {
    "Blue":"blue",
    "Green":"green",
    "Grey":"grey",
    "Indigo":"indigo",
    "Orange":"orange",
    "Red":"red",
    "Violet":"violet",
    "Yellow":"yellow"
}

cloud_files = {
    "Yes":"cloud",
    "No":"blank"
}

stars_files = {
    "None":"blank",
    "Even More":"even_more_stars",
    "More":"more_stars",
    "Some":"stars"
}

spots_files = {
    "Blank":"blank",
    "Bright Pink":"bright_pink",
    "Dark Purple":"dark_purple",
    "Green Shimmer":"green_shimmer",
    "Green Shine":"green_shine",
    "Green Tourquise Shimmer":"green_tourquise_shimmer",
    "Green":"green",
    "Pearlescence":"pearlescence",
    "Pink":"pink",
    "Pinkish Orange":"pinkish_orange",
    "Pretty Purple":"pretty_purple",
    "Purplish Blue":"purplish_blue",
    "Royal Purple":"royal_purple",
    "Salmon":"salmon",
    "Shimmer":"shimmer",
    "Sky Blue":"sky_blue",
    "Yellow Green":"yellow_green",
    "Aqua Green":"aqua_green"
}

horn_files = {
    "Big Rainbow":"big_rainbow",
    "Small Rainbow":"small_rainbow",
    "Ukraine Stripes":"ukraine_stripes",
"Ukraine":"ukraine"
}

tail_files = {
    "Long Rainbow":"long_rainbow",
    "Long Ukraine":"long_ukraine",
    "Short Rainbow":"short_rainbow",
    "Short Ukraine":"short_ukraine",
    "Speedy Rainbow":"speedy_rainbow",
    "Speedy Ukraine":"speedy_ukraine"
}

mane_files = {
    "Blue Spikes":"blue_spikes",
    "Curly Rainbow":"curly_rainbow",
    "Curly Ukraine":"curly_ukraine",
    "Lime Spikes":"lime_spikes",
    "Orange Spikes":"orange_spikes",
    "Pink Spikes":"pink_spikes",
    "Purple Spikes":"purple_spikes",
    "Rainbow Updo":"rainbow_updo",
    "Red Spikes":"red_spikes",
    "Short Rainbow":"short_rainbow",
    "Short Ukraine":"short_ukraine",
    "Sleek Rainbow":"sleek_rainbow",
    "Sleek Ukraine":"sleek_ukraine",
    "Ukraine Updo":"ukraine_updo",
    "Yellow Spikes":"yellow_spikes"
}

eyes_files = {
    "Half Closed":"half_closed",
    "Wide Awake":"wide_awake",
    "Wink":"wink"
}

mouth_files = {
    "Happy":"happy",
    "Hmm":"hmm",
    "Oh":"oh",
    "Smile":"smile"
}

flash_files = {
    "Banana":"banana",
    "None":"blank",
    "Cream":"cream",
    "Lavender":"lavender",
    "Mint":"mint",
    "Peach":"peach",
    "White":"white"
}

blush_files = {
    "Dark":"dark",
    "Medium":"medium",
    "Light":"light",
    "None":"blank"
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 48 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    new_image ["Cloud"] = random.choices(cloud, cloud_weights)[0]
    new_image ["Stars"] = random.choices(stars, stars_weights)[0]
    new_image ["Spots"] = random.choices(spots, spots_weights)[0]
    new_image ["Horn"] = random.choices(horn, horn_weights)[0]
    new_image ["Flash"] = random.choices(flash, flash_weights)[0]
    new_image ["Tail"] = random.choices(tail, tail_weights)[0]
    new_image ["Mane"] = random.choices(mane, mane_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Blush"] = random.choices(blush, blush_weights)[0]


    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

#Return true if all images are unique

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

#add token id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#print all images

print(all_images)

#get trait count

background_count = {}
for item in background:
    background_count[item] = 0

blush_count = {}
for item in blush:
    blush_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

cloud_count = {}
for item in cloud:
    cloud_count[item] = 0

stars_count = {}
for item in stars:
    stars_count[item] = 0

spots_count = {}
for item in spots:
    spots_count[item] = 0

horn_count = {}
for item in horn:
    horn_count[item] = 0

flash_count = {}
for item in flash:
    flash_count[item] = 0

tail_count = {}
for item in tail:
    tail_count[item] = 0

mane_count = {}
for item in mane:
    mane_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0

mouth_count = {}
for item in mouth:
    mouth_count[item] = 0

for image in all_images:
    blush_count[image["Blush"]] += 1
    background_count[image["Background"]] += 1
    body_count[image["Body"]] += 1
    cloud_count[image["Cloud"]] += 1
    stars_count[image["Stars"]] += 1
    spots_count[image["Spots"]] += 1
    horn_count[image["Horn"]] += 1
    flash_count[image["Flash"]] += 1
    tail_count[image["Tail"]] += 1
    mane_count[image["Mane"]] += 1
    eyes_count[image["Eyes"]] += 1
    mouth_count[image["Mouth"]] += 1


print(blush_count)
print(background_count)
print(body_count)
print(cloud_count)
print(stars_count)
print(spots_count)
print(horn_count)
print(flash_count)
print(tail_count)
print(mane_count)
print(eyes_count)
print(mouth_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:


    im1 = Image.open(f'./layers/background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/cloud/{cloud_files[item["Cloud"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/stars/{stars_files[item["Stars"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/spots/{spots_files[item["Spots"]]}.png').convert('RGBA')
    im6 = Image.open(f'./layers/horn/{horn_files[item["Horn"]]}.png').convert('RGBA')
    im7 = Image.open(f'./layers/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im8 = Image.open(f'./layers/tail/{tail_files[item["Tail"]]}.png').convert('RGBA')
    im9 = Image.open(f'./layers/mane/{mane_files[item["Mane"]]}.png').convert('RGBA')
    im10 = Image.open(f'./layers/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im11 = Image.open(f'./layers/flash/{flash_files[item["Flash"]]}.png').convert('RGBA')
    im12 = Image.open(f'./layers/blush/{blush_files[item["Blush"]]}.png').convert('RGBA')
    
    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com2, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)
    com8 = Image.alpha_composite(com7, im9)
    com9 = Image.alpha_composite(com8, im10)
    com10 = Image.alpha_composite(com9, im11)
    com11 = Image.alpha_composite(com10, im12)

    #Convert to RGB
    rgb_im = com11.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
    print (file_name)

#Generate Metadata

#f = open('./metadata/all-traits.json',) 
#data = json.load(f)

#IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
#PROJECT_NAME = "Balloon Animals"

#def getAttribute(key, value):
#    return {
#        "trait_type": key,
#        "value": value
#    }
#for i in data:
#    token_id = i['tokenId']
#    token = {
#        "image": IMAGES_BASE_URI + str(token_id) + '.png',
#        "tokenId": token_id,
#        "name": PROJECT_NAME + ' ' + str(token_id),
#        "attributes": []
#    }
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
#    token["attributes"].append(getAttribute("background", i["background"]))
#    token["attributes"].append(getAttribute("Ears", i["Ears"]))
#    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
#    token["attributes"].append(getAttribute("Head", i["Head"]))
#    token["attributes"].append(getAttribute("spots", i["spots"]))
#    token["attributes"].append(getAttribute("mouth", i["mouth"]))
#    token["attributes"].append(getAttribute("flash", i["flash"]))

#    with open('./metadata/' + str(token_id), 'w') as outfile:
#        json.dump(token, outfile, indent=4)
#f.close()