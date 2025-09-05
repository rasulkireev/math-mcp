from fastmcp import FastMCP
import math
import random
import statistics
from typing import List, Union, Tuple
from fractions import Fraction
from decimal import Decimal, getcontext
from starlette.requests import Request
from starlette.responses import PlainTextResponse

# Set high precision for decimal calculations
getcontext().prec = 50

mcp = FastMCP(
    name="Math MCP Server"
)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

# Basic arithmetic operations
@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b. Returns error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent

@mcp.tool
def square_root(number: float) -> float:
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)

@mcp.tool
def nth_root(number: float, n: int) -> float:
    """Calculate the nth root of a number."""
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    return number ** (1/n)

# Trigonometric functions
@mcp.tool
def sin(angle: float, degrees: bool = False) -> float:
    """Calculate sine of an angle. Angle in radians by default, set degrees=True for degrees."""
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)

@mcp.tool
def cos(angle: float, degrees: bool = False) -> float:
    """Calculate cosine of an angle. Angle in radians by default, set degrees=True for degrees."""
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)

@mcp.tool
def tan(angle: float, degrees: bool = False) -> float:
    """Calculate tangent of an angle. Angle in radians by default, set degrees=True for degrees."""
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)

@mcp.tool
def asin(value: float, degrees: bool = False) -> float:
    """Calculate arcsine of a value. Returns in radians by default, set degrees=True for degrees."""
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    result = math.asin(value)
    return math.degrees(result) if degrees else result

@mcp.tool
def acos(value: float, degrees: bool = False) -> float:
    """Calculate arccosine of a value. Returns in radians by default, set degrees=True for degrees."""
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    result = math.acos(value)
    return math.degrees(result) if degrees else result

@mcp.tool
def atan(value: float, degrees: bool = False) -> float:
    """Calculate arctangent of a value. Returns in radians by default, set degrees=True for degrees."""
    result = math.atan(value)
    return math.degrees(result) if degrees else result

# Logarithmic functions
@mcp.tool
def log(number: float, base: float = math.e) -> float:
    """Calculate logarithm of a number with specified base (natural log by default)."""
    if number <= 0:
        raise ValueError("Number must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(number, base)

@mcp.tool
def log10(number: float) -> float:
    """Calculate base-10 logarithm of a number."""
    if number <= 0:
        raise ValueError("Number must be positive")
    return math.log10(number)

@mcp.tool
def ln(number: float) -> float:
    """Calculate natural logarithm of a number."""
    if number <= 0:
        raise ValueError("Number must be positive")
    return math.log(number)

# Number theory functions
@mcp.tool
def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

@mcp.tool
def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers."""
    return math.gcd(a, b)

@mcp.tool
def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two integers."""
    return abs(a * b) // math.gcd(a, b) if a != 0 and b != 0 else 0

@mcp.tool
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

@mcp.tool
def prime_factors(n: int) -> List[int]:
    """Find all prime factors of a number."""
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

@mcp.tool
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Statistics functions
@mcp.tool
def mean(numbers: List[float]) -> float:
    """Calculate arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.mean(numbers)

@mcp.tool
def median(numbers: List[float]) -> float:
    """Calculate median of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.median(numbers)

@mcp.tool
def mode(numbers: List[float]) -> float:
    """Calculate mode of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.mode(numbers)

@mcp.tool
def standard_deviation(numbers: List[float], sample: bool = True) -> float:
    """Calculate standard deviation. Set sample=False for population standard deviation."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.stdev(numbers) if sample else statistics.pstdev(numbers)

@mcp.tool
def variance(numbers: List[float], sample: bool = True) -> float:
    """Calculate variance. Set sample=False for population variance."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.variance(numbers) if sample else statistics.pvariance(numbers)

# Geometry functions
@mcp.tool
def circle_area(radius: float) -> float:
    """Calculate area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

@mcp.tool
def circle_circumference(radius: float) -> float:
    """Calculate circumference of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

@mcp.tool
def rectangle_area(length: float, width: float) -> float:
    """Calculate area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

@mcp.tool
def triangle_area(base: float, height: float) -> float:
    """Calculate area of a triangle given base and height."""
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

@mcp.tool
def sphere_volume(radius: float) -> float:
    """Calculate volume of a sphere given its radius."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4/3) * math.pi * radius ** 3

@mcp.tool
def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate Euclidean distance between two 2D points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

@mcp.tool
def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# Advanced math functions
@mcp.tool
def combinations(n: int, r: int) -> int:
    """Calculate combinations (n choose r)."""
    if r < 0 or r > n or n < 0:
        raise ValueError("Invalid values for n and r")
    return math.comb(n, r)

@mcp.tool
def permutations(n: int, r: int) -> int:
    """Calculate permutations (n permute r)."""
    if r < 0 or r > n or n < 0:
        raise ValueError("Invalid values for n and r")
    return math.perm(n, r)

@mcp.tool
def solve_quadratic(a: float, b: float, c: float) -> Tuple[Union[float, complex], Union[float, complex]]:
    """Solve quadratic equation ax² + bx + c = 0. Returns tuple of two solutions."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for quadratic equation")

    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return (x1, x2)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return (x1, x2)

@mcp.tool
def random_number(min_val: float = 0, max_val: float = 1) -> float:
    """Generate a random float between min_val and max_val."""
    return random.uniform(min_val, max_val)

@mcp.tool
def random_integer(min_val: int = 0, max_val: int = 100) -> int:
    """Generate a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

@mcp.tool
def absolute_value(number: float) -> float:
    """Calculate absolute value of a number."""
    return abs(number)

@mcp.tool
def ceiling(number: float) -> int:
    """Round number up to nearest integer."""
    return math.ceil(number)

@mcp.tool
def floor(number: float) -> int:
    """Round number down to nearest integer."""
    return math.floor(number)

@mcp.tool
def round_number(number: float, decimals: int = 0) -> float:
    """Round number to specified decimal places."""
    return round(number, decimals)

@mcp.tool
def fraction_from_decimal(decimal_num: float) -> str:
    """Convert decimal to fraction representation."""
    frac = Fraction(decimal_num).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"

@mcp.tool
def percentage(part: float, whole: float) -> float:
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100


app = mcp.http_app()
