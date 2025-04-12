import os


def remove_tmp_files(directory):
    """
    Remove artifacts created by `show_plot()` from from open_atmos_jupyter_utils
    """

    # Walk through the entire directory
    for dirpath, dirnames, filenames in os.walk(directory):
        # Check each file in the directory
        for file in filenames:
            # Check if the file starts with "tmp" and ends with .pdf or .svg
            if file.startswith("tmp") and (
                file.endswith(".pdf") or file.endswith(".svg") or file.endswith("gif")
            ):
                file_path = os.path.join(dirpath, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    directory = "."
    remove_tmp_files(directory)
