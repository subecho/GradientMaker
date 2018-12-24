import collections
import random

from PIL import Image, ImageDraw, ImageColor

def random_image(width=500, height=500, output_file="some.png"):
  image = Image.new("RGB", (width, height))
  draw = ImageDraw.Draw(image)
  for i in range(100000):
    draw.line(
      [get_random_coord(width, height), get_random_coord(width, height)],
      fill=get_random_color()
    )
  image.save(output_file, "PNG")

def get_random_coord(width=500, height=500):
  return (random.randint(0, width), random.randint(0, height))

def get_random_color():
  rgb_val = random.randint

  rgb = (rgb_val(0, 255), rgb_val(0, 255), rgb_val(0, 255))
  return rgb

def draw_gradient(start, end, width, height):
  start_r, start_g, start_b = start
  end_r, end_g, end_b = end
  diff_r = abs(start_r - end_r)
  step_r = round(width / diff_r) if diff_r != 0 else 0
  diff_g = abs(start_g - end_g)
  step_g = round(width / diff_g) if diff_g != 0 else 0
  diff_b = abs(start_b - end_b)
  step_b = round(width / diff_b) if diff_b != 0 else 0

  current_r, current_g, current_b = start
  image = Image.new("RGB", (width, height))
  draw = ImageDraw.Draw(image)
  for i in range(width):
    draw.line([(i, 0), (i, height)], fill=(current_r, current_g, current_b))
    if step_r != 0 and i % step_r == 0 and i < width:
      current_r = _change_current_value(current_r, end_r)
    if step_g != 0 and i % step_g == 0 and i < width:
      current_g = _change_current_value(current_g, end_g)
    if step_b != 0 and i % step_b == 0 and i < width:
      current_b = _change_current_value(current_b, end_b)
  image.save("gradient.png", "PNG")

def _change_current_value(current, final):
  if current < final:
    return current + 1
  else:
    return current - 1

if __name__ == "__main__":
  draw_gradient((185,43,39), (21, 101, 192), 2880, 1800)
