import cv2
import numpy as np

class Solver():
    @staticmethod
    def solve(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        dc = cv2.drawContours(thresh, contours, 0, (255, 255, 255), 5)

        cv2.imshow('1', dc);

        dc = cv2.drawContours(dc, contours, 1, (0, 0, 0), 5)

        cv2.imshow('2', dc);

        kernel = np.ones((19, 19), np.uint8)
        dilation = cv2.dilate(thresh, kernel, iterations=1)
        cv2.imshow('3', dilation);
        erosion = cv2.erode(dilation, kernel, iterations=1)
        cv2.imshow('4', erosion);
        diff = cv2.absdiff(dilation, erosion)

        b, g, r = cv2.split(img)
        mask_inv = cv2.bitwise_not(diff)
        r = cv2.bitwise_and(r, r, mask=mask_inv)
        b = cv2.bitwise_and(b, b, mask=mask_inv)
        res = cv2.merge((b, g, r))

        return res

