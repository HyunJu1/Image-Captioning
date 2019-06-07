# Image Captioning
Used Keras with Tensorflow backend for the code. InceptionV3 is used for extracting the features and GRU is used for generate captions.

## Dataset
Using MS-COCO Datasets.

## Requirements
1. Tensorflow
2. Keras
3. Numpy
4. matplotlib
5. Pandas
6. Pillow
   etc..

## Steps to execute
Just Execute Image Captioning.ipynb file.

You can download the MS-COCO data set automatically through the python modules. 'coco.py, cache.py, download.py' are modules that can download coo data sets and process images.

** Please note that this was done in an environment linked to google drive in Google Colaboratory.

## Results
Following are a few results obtained after training the model for 25 epochs.


Image | Caption
--- | ---
<img src="https://github.com/HyunJu1/Image-Captioning/blob/master/images/pic5.jpg" width="400"> | **Generated Caption:** a man and a woman standing in front of a car.
<img src="https://github.com/HyunJu1/Image-Captioning/blob/master/images/pic1.jpg" width="400"> | **Generated Caption:** a girl is walking down a sidewalk with a backpack.
<img src="https://github.com/HyunJu1/Image-Captioning/blob/master/images/pic3.jpg" width="400"> | **Generated Caption:** a white dog sitting on a wooden floor next to a white plate.



## References
[1] Vinyals, Oriol, et al. "Show and tell: A neural image caption generator." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.

[2] Quanzeng You1 , Hailin Jin2 , Zhaowen Wang2 , Chen Fang2 , and Jiebo Luo1, "Image Captioning with Semantic Attention", Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016
