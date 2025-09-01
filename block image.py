# 1-bit image: 0 = black, 1 = white
# We'll store the image as a list of rows, each row a list of 0/1.

def print_bw(image):
    """Render the 1-bit image in the terminal."""
    for row in image:
        line = "".join("█" if px else " " for px in row)  # white=█, black=space
        print(line)

def save_pbm_ascii(image, path):
    """
    Save as PBM (P1) ASCII format:
    - First line: P1
    - Second line: width height
    - Then rows of 0/1
    """
    h = len(image)
    w = len(image[0]) if h else 0
    with open(path, "w", encoding="ascii") as f:
        f.write("P1\n")
        f.write(f"{w} {h}\n")
        for row in image:
            f.write(" ".join(str(int(px)) for px in row) + "\n")

def make_blank(width, height, fill=0):
    return [[fill for _ in range(width)] for _ in range(height)]

def set_pixel(image, x, y, value):
    image[y][x] = 1 if value else 0

# --- Example: an 8x8 smiley (1 = white pixel, 0 = black pixel) ---
smiley = [
    [0,0,1,1,1,1,0,0],
    [0,1,0,0,0,0,1,0],
    [1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,0,1,1,0,0,1],
    [0,1,0,0,0,0,1,0],
    [0,0,1,1,1,1,0,0],
]

# Show in terminal
print("Console render:")
print_bw(smiley)

# Save as PBM you can open with many image viewers/editors
save_pbm_ascii(smiley, "smiley.pbm")
print("\nSaved PBM file: smiley.pbm")
