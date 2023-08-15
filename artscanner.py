import os


def has_image_in_tree(directory):
    """
    Recursively checks if the directory or any of its subdirectories contain an image.
    Returns True if an image (jpg or png) is found, otherwise returns False.
    """
    for foldername, subfolders, filenames in os.walk(directory):
        if any(filename.lower().endswith(('.jpg', '.png')) for filename in filenames):
            return True
    return False


def folders_without_images(root_directory):
    # Folders without images will be collected in this list
    folders_without_jpg_png = []

    # Directly look at the top-level folders in root_directory
    for foldername in os.listdir(root_directory):
        full_folder_path = os.path.join(root_directory, foldername)

        # Skip if not a directory
        if not os.path.isdir(full_folder_path):
            continue

        # If the top-level folder or any of its subdirectories don't have an image, add to the list
        if not has_image_in_tree(full_folder_path):
            folders_without_jpg_png.append(full_folder_path)

    return folders_without_jpg_png


def main():
    root_directory = input("Enter the root directory to scan: ")

    # Get the list of folders without .jpg or .png files
    result_folders = folders_without_images(root_directory)

    # Save the results to a text file
    with open("folders_without_images.txt", "w", encoding="utf-8") as f:
        for folder in result_folders:
            f.write(folder + "\n")

    print(f"Results saved to folders_without_images.txt")


if __name__ == "__main__":
    main()
