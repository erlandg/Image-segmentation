# Image-segmentation
Image segmentation program for FYS-2010. Separation by using the separate colors' covariance matrix

Segmentation by caclculating a statistical measure of the covariance and mean of the RBG components.
Function used:
D(z, a) = [(z - a).T C^(-1) (z - a)]^(1/2)
where D is the similarity measure, C is covariance matrix, a is the color of the area to segmentate, and z is the pixel in question.

requires numpy, matplotlib, pillow and python
run by python prob3.py
