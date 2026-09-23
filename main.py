from PIL import Image
from pathlib import Path
import keras
import pydot
from keras import layers
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



subfilesList = []
path_test = Path("signVideos/fixed")
for i in path_test.iterdir():
    subfilesList.append("signVideos/fixed/" + i.name)
    #print(i.name)
del subfilesList[0]

training_images = []
training_lables = []


pixel_name_list = []
'''
#necessary for setting up database
starter_pixel_test_image = np.asarray(Image.open("signVideos/fixed/a/0003.jpg"))
starter_pixel_test_image = starter_pixel_test_image/250
#print(starter_pixel_test_image.size)

starter_pixel_test_image = starter_pixel_test_image.reshape(-1)
#print(starter_pixel_test_image.size)

pixel_test_dict = {"lable": [0]}



for i in range(starter_pixel_test_image.size):
    pixel_test_dict["pixel_"+str(i)] = [starter_pixel_test_image.item(i)]
'''
'''
test_test= np.asarray(Image.open("signVideos/fixed/a/0039.png"))/250

plt.figure()
plt.imshow(test_test)
plt.colorbar()
plt.grid(False)
plt.show()
'''




#testing varriable
how_many_pictures = 0

immages_pixels_array = np.append(((np.asarray(Image.open("signVideos/fixed/a/0039.png")))/250).reshape(-1), 0)
test_pixel_array_for_stack = np.append(((np.asarray(Image.open("signVideos/fixed/a/0038.png")))/250).reshape(-1), 0)
immages_pixels_array = np.vstack((immages_pixels_array, test_pixel_array_for_stack))

#print(immages_pixels_array.size)


training_data = pd.DataFrame(immages_pixels_array)
#print(training_data)

#builds database
for i in range(len(subfilesList)-2):
    temp_path = Path(subfilesList[i])
    #print(temp_path)


    for j in temp_path.iterdir():
        try:
            how_many_pictures += 1
            #print(how_many_pictures)
            #training_images.append(np.asarray(Image.open(subfilesList[i] + "/" + j.name)))

            #pixel_test_image = np.asarray(Image.open(subfilesList[i] + "/" + j.name))
            #pixel_test_image = pixel_test_image / 250
            #print(pixel_test_image.size)

            #pixel_test_image = pixel_test_image.reshape(-1)
            #print(pixel_test_image.size)

            #pixel_test_dict = {}
            #pixel_test_dataframe = pd.DataFrame({})

            if(how_many_pictures == 20):
                #print("test 1")
                temp_data_frame = pd.DataFrame(immages_pixels_array)
                #print("test2")
                #print(temp_data_frame)
                training_data = pd.concat([training_data, temp_data_frame])
                #print("TEST 3")
                immages_pixels_array = np.append((np.asarray(Image.open(subfilesList[i] + "/" + j.name))/250).reshape(-1), i)
                #print("test 4")
                how_many_pictures = 0
                #print("test 5")


            pixel_test_image = np.append((np.asarray(Image.open(subfilesList[i] + "/" + j.name))/250).reshape(-1), i)

            immages_pixels_array = np.vstack((immages_pixels_array, pixel_test_image))
            #print(immages_pixels_array.shape)






        except:
            pass

    print("Section "+ str(i) + " complete")




print(training_data.size)
print(training_data)


#comment when not building a database
#training_data.to_csv("test1", mode='a')


#gets data from csv file

#print("test")
#stored_training_data = pd.read_csv("test1")
#print("test2")
#print(stored_training_data.size)
#print(stored_training_data)
#print(stored_training_data.shape)


#noramlizes data to smaller scale
#training_data = training_data.apply(lambda x: x/250, axis=1)



model = tf.keras.Sequential([
    #tf.keras.layers.Flatten(input_shape=(1920, 1080)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3)
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

target = training_data.iloc[:,1306512]
#training_data.drop(1306512)
print("Target:")
print(target.head())

#print(image_values.head())

#tf.convert_to_tensor(training_data)



model.fit(training_data, target, epochs=10)


#test = Image.open("signVideos/fixed/a/0001.jpg")
#test2 = np.asarray(test)



#print(type(test2))
#print(test2.shape)



image_size = (1920, 1080)

print("done")