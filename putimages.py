import boto3
import os

s3 = boto3.resource('s3')
image_directory = '/Users/atchudhansreekanth/Desktop/images'
metadata = {
    'image1.jpg': 'Elon Musk',
    'image2.jpg': 'Elon Musk',
    'image3.jpg': 'Bill Gates',
    'image4.jpg': 'Bill Gates',
    'image5.jpg': 'Sundar Pichai',
    'image6.jpg': 'Sundar Pichai'
}

for filename in os.listdir(image_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')): 
        file_path = os.path.join(image_directory, filename)
        with open(file_path, 'rb') as file:
            s3_object = s3.Object('famouspersons-images-atchudhan', 'index/' + filename)
            ret = s3_object.put(
                Body=file,
                Metadata={'FullName': metadata.get(filename, 'Unknown')}
            )
