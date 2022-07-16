import sys
import cv2 as cv
import numpy as np


def main(argv):
    default_file = 'smarties.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    lower = np.array([255, 255, 255])
    upper = np.array([220, 120, 180])

    mask = cv.inRange(src, lower, upper)
    #output = cv.bitwise_and(src, src, mask = mask)

    cv.imshow("detected circles", mask)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])