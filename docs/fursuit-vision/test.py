#!/usr/bin/env python

import cv2
import numpy as np
import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--width', default=None, type=int)
    parser.add_argument('--height', default=None, type=int)
    args = parser.parse_args()

    # Open the default camera
    cameras = [ cv2.VideoCapture(0), cv2.VideoCapture(1), ]

    # Get the default frame width and height
    frame_width = int(cameras[0].get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cameras[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame0 = cameras[0].read()
        ret, frame1 = cameras[1].read()

        if not ret:
            return

        # Resize frames to the same height
        height =  args.height or  min(frame0.shape[0], frame1.shape[0])
        width = args.width or int(frame0.shape[1] * height / frame0.shape[0])
        frame0 = cv2.resize(frame0, (width, height))
        frame1 = cv2.resize(frame1, (width, height))

        # Combine frames horizontally
        combined_frame = np.hstack((frame0, frame1))

        cv2.imshow('Side-by-Side Videos', combined_frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            return


if __name__ == "__main__":
    main()

