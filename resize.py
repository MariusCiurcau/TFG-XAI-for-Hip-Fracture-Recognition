import cv2
import os
import shutil

def resize(input_images_folder, output_images_folder, padding=True):
    os.makedirs(output_images_folder, exist_ok=True)

    width_max = 0
    height_max = 0
    for root, dirs, files in os.walk(input_images_folder, topdown=False):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                img = cv2.imread(os.path.join(root, file))
                h, w = img.shape[:2]
                width_max = max(width_max, w)
                height_max = max(height_max, h)

    for root, dirs, files in os.walk(input_images_folder, topdown=False):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                img = cv2.imread(os.path.join(root, file))
                h, w = img.shape[:2]
                if padding:
                    diff_vert = height_max - h
                    pad_top = diff_vert // 2
                    pad_bottom = diff_vert - pad_top
                    diff_hori = width_max - w
                    pad_left = diff_hori // 2
                    pad_right = diff_hori - pad_left
                    img_padded = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=0)
                    assert img_padded.shape[:2] == (height_max, width_max)
                    cv2.imwrite(os.path.join(output_images_folder, file), img_padded)
                else:
                    img_resized = cv2.resize(img, (max(height_max, width_max), max(height_max, width_max)), interpolation=cv2.INTER_LINEAR)
                    cv2.imwrite(os.path.join(output_images_folder, file), img_resized)
                print(f"Saved image {file}")

if __name__ == "__main__":
    input_folder = "./Datasets/Dataset/Femurs/augmented_images"
    output_folder = "./Datasets/Dataset/Femurs/resized_augmented_images"
    resize(input_folder, output_folder, False)