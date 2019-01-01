import random

from PIL import Image, ImageDraw


def random_image(width=500, height=500, num_lines=100000,
                 base_color=0) -> Image:
  """Create an image generated with a bunch of random colored lines.

    Arguments:
      width (int): The width of the resulting image in pixels.
      height (int): The height of the resulting image in pixels.
      num_lines (int): The number of random lines to draw in the image.
      base_color (int): The "base" color of an image. 0 is black.

    Returns:
      (PIL.Image) object representing the created image.
  """
  image = Image.new("RGB", (width, height), base_color)
  draw = ImageDraw.Draw(image)
  for i in range(num_lines):
    draw.line(
      [get_random_coord(width, height), get_random_coord(width, height)],
      fill=get_random_color()
    )
  return image


def get_random_coord(width: int, height: int) -> (int, int):
  """Get a random, two-dimensional coordinate in the form (width, height).

    Arguments:
      width (int): The maximum width of the coordinate plane.
      height (int): The maximum height of the coordinate plane.

    Returns:
      (int, int): A tuple containing a random width and height pair.
  """
  return random.randint(0, width), random.randint(0, height)


def get_random_color() -> (int, int, int):
  """Gets a random RGB value in the form (r, g, b)

    Returns:
      (int, int, int): A tuple representing an RGB color.
  """
  rgb_val = random.randint

  rgb = (rgb_val(0, 255), rgb_val(0, 255), rgb_val(0, 255))
  return rgb


def draw_gradient(start: (int, int, int), end: (int, int, int), width: int,
                  height: int) -> Image:
  """Draw a left-to-right gradient starting the start color and ending with
  the end color of the specified size.

  :param start: The starting color of the gradient in an (r, g, b) tuple.
  :param end: The ending color of the gradient in an (r, g, b) tuple.
  :param width: The width of the resulting image in pixels.
  :param height: The height of the resulting image in pixels.
  :return: An Image object with the created gradient.
  """
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
  return image


def _change_current_value(current: int, final: int) -> int:
  if current < final:
    return current + 1
  else:
    return current - 1


def _get_rgb_from_string(a_str: str) -> int:
  return int(a_str, base=16)


def hex_color_code_to_rgb(hex_code: str) -> (int, int, int):
  if len(hex_code) != 6:
    raise ValueError("Hex Code must be exactly six characters long (got %s)"
                     % hex_code)
  r = _get_rgb_from_string(hex_code[0:2])
  g = _get_rgb_from_string(hex_code[2:4])
  b = _get_rgb_from_string(hex_code[4:6])

  def validate_rgb_value(value: int) -> bool:
    return 0 <= value <= 255

  if validate_rgb_value(r) and validate_rgb_value(g) and validate_rgb_value(b):
    return r, g, b
  else:
    raise ValueError("Invalid RGB value (%s, %s, %s)" % (r, g, b))


if __name__ == "__main__":
  image = draw_gradient(hex_color_code_to_rgb("0575E6"),
                        hex_color_code_to_rgb("021B79"),
                        2880,
                        1800)
  image.save("gradient.png", "PNG")
