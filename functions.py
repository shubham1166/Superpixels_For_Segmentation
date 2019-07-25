
'''
Created on Jun 28, 2019

@author: Shubham Sharma
'''
from skimage.segmentation import slic,mark_boundaries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
from tqdm import tqdm
from skimage.morphology import watershed
from skimage.filters import threshold_otsu
from scipy import ndimage
########################################################

#Plese write your path to image here 
path2images='E:/Cell_data/U-Net/Post-processing/origanal images/'
# path2labels='E:/Cell_data/U-Net/Post-processing/original labels/'


#This function is for the purpose of reconstruction
# def give_watershed(label_image,markers):
#     D = ndimage.distance_transform_edt(label_image)
#     ret, labels = cv2.connectedComponents(markers.astype('uint8'))
#     watershed_image=watershed(-D,labels,mask=label_image)
#     output=np.zeros(watershed_image.shape)
#     for label in np.unique(watershed_image):
#         if label==0:
#             continue
#         mask = np.zeros(label_image.shape, dtype="uint8")
#         mask[watershed_image == label] = 255
#         kernel = np.ones((3,3),np.uint8)
#         eroded_image = cv2.erode(mask,kernel,iterations=1)
#         output[eroded_image == 255] = 255
#     return output


def superpixels_segmentation(t,flag1,flag2,flag3,flag4,flag_very_small_cells):
    
    if flag_very_small_cells:
        image = Image.open(path2images+str(t)+'.png')
        contrast = ImageEnhance.Contrast(image)
        y=np.array(contrast.enhance(1))
        z=np.array(contrast.enhance(8))
        z=cv2.cvtColor(z,cv2.COLOR_RGB2GRAY).astype('uint8')
        segments = slic(y, n_segments=10000)
    
    elif flag1:
        image = Image.open(path2images+str(t)+'.png')
        contrast = ImageEnhance.Contrast(image)
        y=np.array(contrast.enhance(2))
        z=np.array(contrast.enhance(5))
        z=cv2.cvtColor(z,cv2.COLOR_RGB2GRAY).astype('uint8')
        y=(255-y)
        segments = slic(y, n_segments=3000)
        
    elif flag2:
        image = Image.open(path2images+str(t)+'.png')
        contrast = ImageEnhance.Contrast(image)
        y=np.array(contrast.enhance(2))
        segments = slic(y, n_segments=3000) 
        
    elif flag3:
        image = Image.open(path2images+str(t)+'.png')
        contrast = ImageEnhance.Contrast(image)
        y=np.array(contrast.enhance(1))
        z=np.array(contrast.enhance(8))
        z=cv2.cvtColor(z,cv2.COLOR_RGB2GRAY).astype('uint8')
        segments = slic(y, n_segments=6000)
        
    elif flag4:
        image = Image.open(path2images+str(t)+'.png')
        contrast = ImageEnhance.Contrast(image)
        y=np.array(contrast.enhance(1))
        y=255-y
        segments = slic(y, n_segments=5000)
        
        
     

    #MAKING THE SUPERPIXEL IMAGE
    # image_with_boundaries=mark_boundaries(y, segments)
    cv_image=cv2.cvtColor(y,cv2.COLOR_RGB2GRAY).astype('uint8')
    super_pixel=np.zeros(cv_image.shape,dtype='uint8')
    for label in np.unique(segments):
                mask = np.zeros(cv_image.shape, dtype="uint8")
                mask[segments == label] =1
                non_zero_cordinates=np.nonzero(mask*cv_image)
                x=cv_image[non_zero_cordinates]
                mean=np.mean(x)
                super_pixel[non_zero_cordinates]=mean
    
    
    
    if flag1:
        lines=cv2.Canny(z,100,360)
    elif flag2:
        lines=cv2.Canny(super_pixel,50,100)
    elif flag3:
        lines=cv2.Canny(z,50,100)
    
    
    #REMOVING LINES FROM SUPERPIXELS    
    if flag4==False and flag_very_small_cells==False : #as in type4 cells we donot want to remove the lines because of the very small size of the cells
        lines_eroded=super_pixel.copy()
        for i in np.unique(segments):
            mask = np.zeros(cv_image.shape, dtype="uint8")
            mask[segments == i] =1
            intersection = mask*lines
            if np.sum(intersection)>0:
                lines_eroded[segments == i]=0
    
    epsilon=0
    if flag4:
        epsilon=84
        lines_eroded=super_pixel
    elif flag_very_small_cells:
        epsilon=30
        lines_eroded=super_pixel
    
    thresh=threshold_otsu(lines_eroded)
    thresh=thresh+epsilon
    segmentation=(lines_eroded>thresh).astype('int')    
    segmentation=segmentation*255.
#     segmentation=give_watershed(label_image,segmentation)
    if t==602 or t==283 or t==223 or t==187 or t==153 or t==70 or t==202 or t==153 or t==281:
        segmentation=255-segmentation
    return segmentation





