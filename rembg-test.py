import numpy as np
import io
from PIL import Image
import rembg.bg


def run():
    input_path = '120181612175884_.pic_hd.jpg'
    output_path = '12018161217588411_.png'

    f = np.fromfile(input_path)
    result = rembg.bg.remove(f,
                             alpha_matting=True,
                             alpha_matting_foreground_threshold=240,
                             alpha_matting_background_threshold=10,
                             alpha_matting_erode_structure_size=10,
                             alpha_matting_base_size=1000,)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
