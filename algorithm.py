'''
Created on Jul 1, 2019
This code is for segmentation using SUPERPIXELS
@author: Shubham Sharma
'''


#IMPORTING IMPORTANT FUNCTIONS
import cv2
import numpy as np
from Superpixels.functions import superpixels_segmentation
from tqdm import tqdm

type1=np.load('E:/Cell_data/U-Net/Post-processing/processed/coloured/name.npy')
type2=np.load('E:/Cell_data/U-Net/Post-processing/processed/TYPE2/IMAGES/images.npy')
type3=np.load('E:/Cell_data/U-Net/Post-processing/processed/TYPE3/images/images.npy')
type4=np.load('E:/Cell_data/U-Net/Post-processing/processed/TYPE4/IMAGES/images.npy')
very_small_cells=[660,594,488,359,138]

def give_flag(t,flag1=False, flag2=False, flag3=False, flag4=False, flag_very_small_cells=False):
    if t in very_small_cells:
        flag_very_small_cells=True
    elif t in type1:
        flag1=True
    elif t in type2:
        flag2=True
    elif t in type3:
        flag3=True
    elif t in type4:
        flag4=True  
    return flag1, flag2, flag3, flag4, flag_very_small_cells




path2save='E:/Cell_data/Superpixels/'
# for t in tqdm(range(670)):
#     flag1, flag2, flag3, flag4, flag_very_small_cells=give_flag(t)

#     img=superpixels_segmentation(t, flag1, flag2, flag3, flag4, flag_very_small_cells)
#     cv2.imwrite(path2save+str(t)+'.png',img)
 





# t=70
l=[602 ,283 ,223 ,187 ,153,70,202,153,281]
for t in tqdm(l):
    flag1, flag2, flag3, flag4, flag_very_small_cells=give_flag(t)
    img=superpixels_segmentation(t, flag1, flag2, flag3, flag4, flag_very_small_cells)
# cv2.imshow('',img)
# cv2.waitKey(0)
    cv2.imwrite(path2save+str(t)+'.png',img)

 

 
        