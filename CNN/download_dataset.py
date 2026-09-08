import tensorflow as tf
import os

# URL for the small, filtered Cats vs Dogs dataset (~68MB, 2,000 images)
_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'

# Downloads the zip, extracts it, and returns the path to the extracted folder
path_to_zip = tf.keras.utils.get_file(
    'cats_and_dogs_filtered.zip',
    origin=_URL,
    extract=True,
    cache_dir='.'  # downloads into ./datasets by default
)

# The extracted folder sits next to the zip file
PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')

print("Dataset ready at:", PATH)
print("Train dir:", train_dir)
print("Validation dir:", validation_dir)
print("Num train cat images:", len(os.listdir(train_cats_dir)))
print("Num train dog images:", len(os.listdir(train_dogs_dir)))