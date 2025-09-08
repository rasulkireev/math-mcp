from fastmcp import FastMCP, Context
import math
import random
import statistics
from typing import List, Union, Tuple
from fractions import Fraction
from decimal import Decimal, getcontext
from starlette.requests import Request
from starlette.responses import PlainTextResponse

# from src.logging import logger
from fastmcp.utilities import logging

logger = logging.get_logger()


# Set high precision for decimal calculations
getcontext().prec = 50

mcp = FastMCP(
    name="Math MCP Server"
)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    logger.info("Health check request received")
    return PlainTextResponse("OK")

# Basic arithmetic operations
@mcp.tool
async def add(a: float, b: float, ctx: Context) -> float:
    """Add two numbers."""
    print(f"MCP tool called: add {a} and {b}")
    logger.info("MCP tool called: add", a=a, b=b)
    await ctx.info(
      "MCP tool called: add",
      extra={
        "a": a,
        "b": b
      }
    )
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    logger.info("MCP tool called: subtract", a=a, b=b)
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    logger.info("MCP tool called: multiply", a=a, b=b)
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b. Returns error if b is zero."""
    logger.info("MCP tool called: divide", a=a, b=b)
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

@mcp.tool
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    logger.info("MCP tool called: power", base=base, exponent=exponent)
    return base ** exponent

@mcp.tool
def square_root(number: float) -> float:
    """Calculate the square root of a number."""
    logger.info("MCP tool called: square_root", number=number)
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)

@mcp.tool
def nth_root(number: float, n: int) -> float:
    """Calculate the nth root of a number."""
    logger.info("MCP tool called: nth_root", number=number, n=n)
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    return number ** (1/n)

# Trigonometric functions
@mcp.tool
def sin(angle: float, degrees: bool = False) -> float:
    """Calculate sine of an angle. Angle in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: sin", angle=angle, degrees=degrees)
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)

@mcp.tool
def cos(angle: float, degrees: bool = False) -> float:
    """Calculate cosine of an angle. Angle in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: cos", angle=angle, degrees=degrees)
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)

@mcp.tool
def tan(angle: float, degrees: bool = False) -> float:
    """Calculate tangent of an angle. Angle in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: tan", angle=angle, degrees=degrees)
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)

@mcp.tool
def asin(value: float, degrees: bool = False) -> float:
    """Calculate arcsine of a value. Returns in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: asin", value=value, degrees=degrees)
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    result = math.asin(value)
    return math.degrees(result) if degrees else result

@mcp.tool
def acos(value: float, degrees: bool = False) -> float:
    """Calculate arccosine of a value. Returns in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: acos", value=value, degrees=degrees)
    if not -1 <= value <= 1:
        raise ValueError("Value must be between -1 and 1")
    result = math.acos(value)
    return math.degrees(result) if degrees else result

@mcp.tool
def atan(value: float, degrees: bool = False) -> float:
    """Calculate arctangent of a value. Returns in radians by default, set degrees=True for degrees."""
    logger.info("MCP tool called: atan", value=value, degrees=degrees)
    result = math.atan(value)
    return math.degrees(result) if degrees else result

# Logarithmic functions
@mcp.tool
def log(number: float, base: float = math.e) -> float:
    """Calculate logarithm of a number with specified base (natural log by default)."""
    logger.info("MCP tool called: log", number=number, base=base)
    if number <= 0:
        raise ValueError("Number must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(number, base)

@mcp.tool
def log10(number: float) -> float:
    """Calculate base-10 logarithm of a number."""
    logger.info("MCP tool called: log10", number=number)
    if number <= 0:
        raise ValueError("Number must be positive")
    return math.log10(number)

@mcp.tool
def ln(number: float) -> float:
    """Calculate natural logarithm of a number."""
    logger.info("MCP tool called: ln", number=number)
    if number <= 0:
        raise ValueError("Number must be positive")
    return math.log(number)

# Number theory functions
@mcp.tool
def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    logger.info("MCP tool called: factorial", n=n)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

@mcp.tool
def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers."""
    logger.info("MCP tool called: gcd", a=a, b=b)
    return math.gcd(a, b)

@mcp.tool
def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two integers."""
    logger.info("MCP tool called: lcm", a=a, b=b)
    return abs(a * b) // math.gcd(a, b) if a != 0 and b != 0 else 0

@mcp.tool
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    logger.info("MCP tool called: is_prime", n=n)
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
    logger.info("MCP tool called: prime_factors", n=n)
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
    logger.info("MCP tool called: fibonacci", n=n)
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
    logger.info("MCP tool called: mean", numbers=numbers)
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.mean(numbers)

@mcp.tool
def median(numbers: List[float]) -> float:
    """Calculate median of a list of numbers."""
    logger.info("MCP tool called: median", numbers=numbers)
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.median(numbers)

@mcp.tool
def mode(numbers: List[float]) -> float:
    """Calculate mode of a list of numbers."""
    logger.info("MCP tool called: mode", numbers=numbers)
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.mode(numbers)

@mcp.tool
def standard_deviation(numbers: List[float], sample: bool = True) -> float:
    """Calculate standard deviation. Set sample=False for population standard deviation."""
    logger.info("MCP tool called: standard_deviation", numbers=numbers, sample=sample)
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.stdev(numbers) if sample else statistics.pstdev(numbers)

@mcp.tool
def variance(numbers: List[float], sample: bool = True) -> float:
    """Calculate variance. Set sample=False for population variance."""
    logger.info("MCP tool called: variance", numbers=numbers, sample=sample)
    if not numbers:
        raise ValueError("List cannot be empty")
    return statistics.variance(numbers) if sample else statistics.pvariance(numbers)

# Geometry functions
@mcp.tool
def circle_area(radius: float) -> float:
    """Calculate area of a circle given its radius."""
    logger.info("MCP tool called: circle_area", radius=radius)
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

@mcp.tool
def circle_circumference(radius: float) -> float:
    """Calculate circumference of a circle given its radius."""
    logger.info("MCP tool called: circle_circumference", radius=radius)
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

@mcp.tool
def rectangle_area(length: float, width: float) -> float:
    """Calculate area of a rectangle."""
    logger.info("MCP tool called: rectangle_area", length=length, width=width)
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

@mcp.tool
def triangle_area(base: float, height: float) -> float:
    """Calculate area of a triangle given base and height."""
    logger.info("MCP tool called: triangle_area", base=base, height=height)
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

@mcp.tool
def sphere_volume(radius: float) -> float:
    """Calculate volume of a sphere given its radius."""
    logger.info("MCP tool called: sphere_volume", radius=radius)
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4/3) * math.pi * radius ** 3

@mcp.tool
def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate Euclidean distance between two 2D points."""
    logger.info("MCP tool called: distance_2d", x1=x1, y1=y1, x2=x2, y2=y2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

@mcp.tool
def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculate Euclidean distance between two 3D points."""
    logger.info("MCP tool called: distance_3d", x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# Advanced math functions
@mcp.tool
def combinations(n: int, r: int) -> int:
    """Calculate combinations (n choose r)."""
    logger.info("MCP tool called: combinations", n=n, r=r)
    if r < 0 or r > n or n < 0:
        raise ValueError("Invalid values for n and r")
    return math.comb(n, r)

@mcp.tool
def permutations(n: int, r: int) -> int:
    """Calculate permutations (n permute r)."""
    logger.info("MCP tool called: permutations", n=n, r=r)
    if r < 0 or r > n or n < 0:
        raise ValueError("Invalid values for n and r")
    return math.perm(n, r)

@mcp.tool
def solve_quadratic(a: float, b: float, c: float) -> Tuple[Union[float, complex], Union[float, complex]]:
    """Solve quadratic equation ax² + bx + c = 0. Returns tuple of two solutions."""
    logger.info("MCP tool called: solve_quadratic", a=a, b=b, c=c)
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
    logger.info("MCP tool called: random_number", min_val=min_val, max_val=max_val)
    return random.uniform(min_val, max_val)

@mcp.tool
def random_integer(min_val: int = 0, max_val: int = 100) -> int:
    """Generate a random integer between min_val and max_val (inclusive)."""
    logger.info("MCP tool called: random_integer", min_val=min_val, max_val=max_val)
    return random.randint(min_val, max_val)

@mcp.tool
def absolute_value(number: float) -> float:
    """Calculate absolute value of a number."""
    logger.info("MCP tool called: absolute_value", number=number)
    return abs(number)

@mcp.tool
def ceiling(number: float) -> int:
    """Round number up to nearest integer."""
    logger.info("MCP tool called: ceiling", number=number)
    return math.ceil(number)

@mcp.tool
def floor(number: float) -> int:
    """Round number down to nearest integer."""
    logger.info("MCP tool called: floor", number=number)
    return math.floor(number)

@mcp.tool
def round_number(number: float, decimals: int = 0) -> float:
    """Round number to specified decimal places."""
    logger.info("MCP tool called: round_number", number=number, decimals=decimals)
    return round(number, decimals)

@mcp.tool
def fraction_from_decimal(decimal_num: float) -> str:
    """Convert decimal to fraction representation."""
    logger.info("MCP tool called: fraction_from_decimal", decimal_num=decimal_num)
    frac = Fraction(decimal_num).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"

@mcp.tool
def percentage(part: float, whole: float) -> float:
    """Calculate what percentage 'part' is of 'whole'."""
    logger.info("MCP tool called: percentage", part=part, whole=whole)
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100


app = mcp.http_app()
