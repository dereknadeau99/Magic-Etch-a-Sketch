#from https://datacarpentry.org/image-processing/08-edge-detection/

import skimage
import skimage.feature
import skimage.viewer
import sys

#filename == .png name
#sigma == the value of the Gaussian smoothing
filename = sys.argv[1]
sigma = float(sys.argv[2])
low_threshold = float(sys.argv[3])
high_threshold = float(sys.argv[4])

#load and display original image as grayscale
image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.viewer(image=image)
viewer.show()

#apply Canny edge detection
edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)

#display edges
viewer = skimage.viewer.ImageViewer(edges)
viewer.show()