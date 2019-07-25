# Superpixels
---
**Superpixel** is a group of connected pixels with similar colors or gray levels. Instead of just working with one pixel, we'll use superpixels for image segmentation.

---
## Dataset
The dataset that I have used is a kaggle dataset for identification and segmentation of nuclei in cells. The dataset consists of 670 images and each of the image is an RGB image with dimension 512×512. Below is the figue of the type of data that we have for segmentation.
**![](https://lh6.googleusercontent.com/Ngzs_qC2dUCs-fRkOOVSumBDYS8R3KI69cVdTWaQA6SxM2Qmlsh6tr39SlN5R_6kn_iV_l3xiAS6B6Lwvl96LL_Yzwj18t3c1H0JSyzHDlt4Q7aRoD2I1qkzjgeXUDnq_HcpO5wR)**
(Source:[Kaggle](https://www.kaggle.com/paultimothymooney/identification-and-segmentation-of-nuclei-in-cells))
In my approach , i have devided the image in 4 different types namely colored, white background, Black images with big cells and black images with small cells. The reason of doing this was thresholding and the other things that we are doing in segmentation.

---
## Segmentation by superpixels
There are basically three steps that i did with the segmentation:

1. Used SLIC- Simple Linear Iterative Clustering
2. Used Canny Edge Detection to remove connected nuclei
3. Used Thresholding for segmentation 

### 1. SLIC- Simple Linear Iterative Clustering
SLIC performs a local clustering of pixels in 5-D spacedefines by L,a,b values of CILEB and x,y cordinates of the pixels. The distance measure used for clustering is different in case of SLIC, which enables compactness and regularity in the superpixels shape.
**![](https://lh6.googleusercontent.com/0gNNMYPM9NvsiWPRY1CugIbfDnGi2BWBq665keG4F3xi5d2hYdh1dABlbjZDrnSKZ_Wo7y8Mm_bTX8apMylrR2JjSyRp6zGCrRqQyHIFPc9EDZ-SC2DypSxAu5auJiVi46FzSXk-)**
**Fig**:The figure consists of image with superpixels followed by original image

### 2. Canny edge detection
The Canny edge detection algorithm is composed of 5 steps:

1. **Noise reduction**- reduces noise.
2. **Gradient calculation**- detects edge intensity and direction by calculating the gradient of the image using edge detection operators.
3. **Non-maximum suppression**- As the final image should have thin edges. non-maximum suppression is performed to thin out the edges.
4. **Double threshold**- The double threshold step aims at identifying 3 kinds of pixels: strong, weak, and non-relevant.
5. **Edge Tracking by Hysteresis**- Based on the threshold results, the hysteresis consists of transforming weak pixels into strong ones, if and only if at least one of the pixels around the one being processed is a strong one.

### 3. Thresholding for segmentation
After detecting the edges, the last task is the segment the nuclei out of the images. I have done the segmentation using OTSU thresholding as it tries to maximize the inclass variability.
**![](https://lh3.googleusercontent.com/e2_pfyeFWcaXTFxDt8scvrKRHABlaPj_QWPWeBcr-KgR6uKIBOnP2ioBcXEPEgbDnrmDzheqQKCdkLUhwneqRLeSvqGdfOdjDHriqYpY-NBd2nO141Rs4wNfDwzzPoFWJCt16h1f)**
**Fig**: The figure consists image with superpixels followed by image of the detected edges followed by processed images

The figure below shows the result that we have got from the other methods of segmentation that I have used in the other repositories:
**![](https://lh3.googleusercontent.com/G48JV5E_Lc5bjv_2g0rddq-R8Bx7y9wokWBayRRCAYRhNGf1m6aX4PDAs0agabrjbAbeH531D2acM0fJmQVQCtVPEW-n5K97Y2-mulPe4EESrVIgaEhuJF6VDRkPpQRaPrYaHzw2)**


