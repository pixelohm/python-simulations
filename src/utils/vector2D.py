import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, vec2):
        # When the '+' operator is used between two vectors
        return Vector2D(self.x + vec2.x, self.y + vec2.y)


    def __sub__(self, vec2):
        # When the '-' operator is used between two vectors
        return Vector2D(self.x - vec2.x, self.y - vec2.y)


    def __mul__(self, scalar):
        # When the '*' operator is used between two vectors
        # __mul__ is used when this object is on the left side of the operator
        return Vector2D(self.x * scalar, self.y * scalar)
    
    
    def __rmul__(self, scalar):
        # When the '*' operator is used between two vectors
        # __rmul__ is used when this object is on the right side of the operator
        return self.__mul__(scalar)


    def __truediv__(self, scalar):
        # When the '/' operator is used between two vectors
        # __truediv__ is used when this object is on the left side of the operator
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Vector2D(self.x / scalar, self.y / scalar)


    def __rtruediv__(self, scalar):
        # When the '/' operator is used between two vectors
        # __truediv__ is used when this object is on the right side of the operator
        if self.x == 0 or self.y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Vector2D(scalar / self.x, scalar / self.y)


    def magnitude(self):
        # Calculate the magnitude of the vector
        return math.sqrt(self.x**2 + self.y**2)


    def normalised(self):
        # Calculate the nomalised form of the vector.
        # Normalised form is just the direction, it has a magnitude of 1
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)
    

    def normal(self):
        # The unit vector perpendicular to the current vector
        norm_vec = self.normalised()
        return Vector2D(norm_vec.y, -norm_vec.x)


    def dot(self, vec2):
        # Calculate the dot product between two vectors
        return self.x * vec2.x + self.y * vec2.y
    

    def rotate(self, angle_degrees, point):
        # Translate the vector by subtracting the coordinates of the rotation point
        translated_x = self.x - point.x
        translated_y = self.y - point.y

        angle_rad = math.radians(angle_degrees)

        # Apply the rotation to the translated vector
        rotated_x = (math.cos(angle_rad) * translated_x) + (math.sin(angle_rad) * translated_y)
        rotated_y = (-math.sin(angle_rad) * translated_x) + (math.cos(angle_rad) * translated_y)

        # Translate the vector back by adding the coordinates of the rotation point
        final_x = rotated_x + point.x
        final_y = rotated_y + point.y

        return Vector2D(final_x, final_y)


    def reflect(self, vector, point):
        # Translate the vector by subtracting the coordinates of the rotation point
        translated_x = self.x - point.x
        translated_y = self.y - point.y

        theta = math.atan2(vector.y, vector.x)

        # Apply the reflection to the translated vector
        reflected_x = (math.cos(2*theta) * translated_x) + (math.sin(2*theta) * translated_y)
        reflected_y = (math.sin(2*theta) * translated_x) - (math.cos(2*theta) * translated_y)

        # Translate the vector back by adding the coordinates of the rotation point
        final_x = reflected_x + point.x
        final_y = reflected_y + point.y

        return Vector2D(final_x, final_y)
    

    def zero(self):
        # Reset the vector to (0, 0)
        self.x = 0
        self.y = 0


    def as_tuple(self) -> tuple:
        # Return the vector as a tuple
        return (self.x, self.y)


    def __str__(self):
        # This is run when the object is printed
        return f"({self.x}, {self.y})"
