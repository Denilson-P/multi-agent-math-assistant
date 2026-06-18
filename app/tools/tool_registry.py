from app.tools.math_tools import (
    add,
    divide,
    multiply,
    subtract,
)


TOOL_REGISTRY = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}