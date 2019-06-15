from PIL import Image, ImageOps

def resize(img_path):
    desired_size = 400
    im = Image.open(img_path)

    # Add padding
    delta_w = desired_size - im.size[0]  #im.size is list [width, height]
    delta_h = desired_size - im.size[1]
    padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
    new_im = ImageOps.expand(im, padding)
    new_im.save(img_path)
    return img_path