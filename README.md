# Republic-Day-Word-Maps
Republic Day honours the date January 26, 1950. On this date, the Constitution of India came into effect by replacing the Government of India act (1935).

Bhimrao Ramji Ambedkar was a wise constitutional expert, he had studied the constitutions of about 60 countries. Ambedkar is recognised as the "Father of the Constitution of India". Ambedkar had the most effective and decisive role in presenting the Constitution as a guiding document for Indian society.

Narendra Damodardas Modi is an Indian politician serving as the 14th and current Prime Minister of India since 2014.

In honour of India's 72nd Republic Day, I decided to whip up image-colored word maps from the speeches of these two influential figures. I have created a image-colored wordmap for Narendra Modi and a image-colored wordmap with boundary (obtained after foreground extraction using Grabcut Algorithm) for B.R. Ambedkar.

## Data

For the speeches of Narendra Modi, I referred to this dataset on Kaggle : [Mann ki Baat](https://www.kaggle.com/skylord/mann-ki-baat). Mann ki Baat (English translation: Matter of contemplation) is a monthly program with which Modi tries to reach out to a larger audience, and the following dataset contains transcripts of these speeches. I had to convert this data from JSON to TXT.

For the speeches of B.R. Ambedkar, I decided to focus on a very specific one. I chose Dr. Ambedkar’s final speech in the Constituent Assembly, dated November 25, 1949, where he presented his justification for the Constitution. [Ambedkar Last Speech](https://velivada.com/2020/01/25/dr-ambedkars-last-speech-in-the-constituent-assembly-on-adoption-of-the-constitution/)

## Code

The code is divided as follows:

1. modidata.py <br />
This file obtains the text of Modi's speeches and saves it into a TXT file.

2. modimap.py <br />
This file creates Modi's word map.

3. ambedkargrabcut.py <br />
This file extracts the foreground from B.R. Ambedkar's picture.

4. ambedkarmap.py <br />
This file creates Ambedkar's word map.

## Tools Used

* Python 3.7
* Pandas
* Numpy
* OpenCV
* OS
* PIL
* Matplotlib
* Scipy
* Wordcloud

import os
import numpy as np
import pandas as pd
import cv2
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as pltimport os
from scipy.ndimage import gaussian_gradient_magnitude

## Results

You can check out the intermediate images in the images folder. Ths word maps are-

![Narendra Modi](https://github.com/Akshat2430/Republic-Day-Word-Maps/blob/main/images/modi_final.png)

![Bhimrao Ambedkar](https://github.com/Akshat2430/Republic-Day-Word-Maps/blob/main/images/ambedkar-final.png)

Happy Republic Day! :india:

## Author

Akshat Kharbanda is a BITS Pilani, KK Birla Goa Campus Student majoring in Electronics and Communication Engineering. Feel free to connect on [LinkedIn](https://www.linkedin.com/in/akshat-kharbanda-b91986148/)!

