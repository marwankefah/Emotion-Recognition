import argparse

import face_recognition
import matplotlib.pyplot as plt
from matplotlib import patches

import src.Helper as hf

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emotion Recognition')
    parser.add_argument("--imgPath",
                        help="Image To get the Emotion Recognition For",
                        type=str)
    args = parser.parse_args()
    real, imag = hf.build_filters()
    #Path Of Trained Model
    modelPath = "D:\\marwan\\Masters\\Bath\\emotionRecgonition\\model\\checkpoint.pth"
    # CSV file used to obtain the most important gabor features
    path2 = "D:\\marwan\\Masters\\Bath\\emotionRecgonition\\a.csv"

    imgPath = "D:\\marwan\\University\\2021Spring\\emotionRecognition\\check.jpg"
    # imgPath=args.imgPath
    image = face_recognition.load_image_file(imgPath)

    face_locations = face_recognition.face_locations(image)
    fig, ax = plt.subplots()
    ax.imshow(image)
    for face_location in face_locations:
        face = image[face_location[0]:face_location[2], face_location[3]: face_location[1]]
        # plt.imshow(face)
        emotion1, prob1 = hf.getemotion(face, modelPath, path2)
        # Create a Rectangle patch
        w=face_location[0]-face_location[2]
        h=face_location[1]-face_location[3]
        rect = patches.Rectangle((face_location[3],face_location[2]), h, w, linewidth=1, edgecolor='r', facecolor='none')
        ax.text(face_location[3], face_location[2], "{0} {1:.1f}% ".format(emotion1, float(prob1[0][0])),
                horizontalalignment='left',
                verticalalignment='top',fontsize=12)       # Add the patch to the Axes
        ax.add_patch(rect)
    plt.savefig("result.jpg")
    plt.show()
