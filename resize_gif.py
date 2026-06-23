from PIL import Image, ImageSequence
import sys

def resize_gif(path, save_as, target_height=60):
    im = Image.open(path)
    
    original_width, original_height = im.size
    aspect_ratio = original_width / original_height
    target_width = int(target_height * aspect_ratio)

    frames = []
    
    try:
        for frame in ImageSequence.Iterator(im):
            # Create a new image to paste the frame into to handle transparency properly
            frame_resized = frame.resize((target_width, target_height), Image.Resampling.LANCZOS)
            frames.append(frame_resized)
            
        frames[0].save(
            save_as,
            save_all=True,
            append_images=frames[1:],
            loop=im.info.get('loop', 0),
            duration=im.info.get('duration', 100),
            disposal=2,
            optimize=False
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    resize_gif("files/prelium-logo-filaire.gif", "files/prelium-logo-filaire-signature.gif", 100)
    print("Done")
