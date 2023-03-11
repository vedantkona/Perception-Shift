# Perception-Shift
Goal
Your task is to predict the aura of all humans in each image of the given dataset.
Also you need to label every object in the dataset. The physical units of volume
remain constrained to the real world measurements. (Note: objects in the image
may be closer / farther than they appear)
Context
Virtual reality has made it possible to experience the beyond. Today, one can visit
the entire world just by sitting in a chair and putting on some goggles. In the
coming future, newer generations will have the capacity to comprehend virtual
scenes on another level.

Since human evolution is taking a major shift in perception, it is required to
measure the aura (impact) every human has on the surroundings. In an ancient
script found in north-eastern Himalayas, the term aura was defined to be ratio of
one’s volume to his/her surface area. To make it simpler, we have defined the aura
to be the following:

aura =

Volume (in cm
3
)

Number of pixels occupied by the object
In 256 A.D. the average human aura was found to be 24 units.
You are the only AI expert left on the planet, please help us to find the aura of
humans in all images (rounded to 2 decimal places).

Subtask 1 (15 pts)
Identifying all objects (non-humans included) in the images, and providing the
corresponding labels
Save your predicted labels in a CSV and rename the CSV as “Object_Labels”
Subtask 2 (30 pts)
Identifying number of pixels occupied by each human in an image
Save your answers in a different CSV and rename it as “Human_Pixels”
Subtask 3 (50 pts)
Predicting the volume of each human in every image. Labeling each human with volume,
aura.
Save your answers in a different CSV and rename it as “Human_Volumes”
Save your answers in a different CSV and rename it as “Human_Auras”
Subtask 4 (5 pts)
Calculating the average aura of the entire dataset
Save your answer in a CSV and rename it as “Average_Aura”

Dataset
You will have the COCO (2017) dataset to train and test your model. You can download it
from the link below (or by any other method) and train your model locally.
https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset

Note:
● Round off every fraction to 2 decimal places
● Images that do not contain any humans should have zero average aura
