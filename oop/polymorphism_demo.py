import math

class Shape:
  """
  A base class representing a generic shape.
  """

  def area(self):
    """
    This method is not implemented in the base class and raises a NotImplementedError.
    Derived classes should override this method to calculate their specific area.
    """
    raise NotImplementedError("Area calculation not implemented for base Shape class")

class Rectangle(Shape):
  """
  A class representing a rectangle, inheriting from Shape.
  """

  def __init__(self, length, width):
    """
    Initializes a Rectangle instance with length and width attributes.

    Args:
      length (float): The length of the rectangle.
      width (float): The width of the rectangle.
    """
    self.length = length
    self.width = width

  def area(self):
    """
    Overrides the area() method from Shape to calculate the area of the rectangle.

    Returns:
      float: The calculated area of the rectangle (length x width).
    """
    return self.length * self.width

class Circle(Shape):
  """
  A class representing a circle, inheriting from Shape.
  """

  def __init__(self, radius):
    """
    Initializes a Circle instance with a radius attribute.

    Args:
      radius (float): The radius of the circle.
    """
    self.radius = radius

  def area(self):
    """
    Overrides the area() method from Shape to calculate the area of the circle.

    Returns:
      float: The calculated area of the circle (pi x radius^2).
    """
    return math.pi * self.radius * self.radius

# Provided for Testing (main.py)
def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()