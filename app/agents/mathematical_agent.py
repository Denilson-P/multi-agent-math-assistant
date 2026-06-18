import ast
from typing import Any


class MathematicalAgent:
    """
    Agent responsible for executing mathematical expressions
    using mathematical tools.

    This agent must not use LLMs.
    """

    AST_OPERATORS = {
        ast.Add: "add",
        ast.Sub: "subtract",
        ast.Mult: "multiply",
        ast.Div: "divide",
    }

    def __init__(
        self,
        tool_registry: dict,
    ) -> None:
        self._tool_registry = tool_registry

    def calculate(
    self,
    expression: str,
    ) -> dict:
        try:
            parsed_expression = ast.parse(
                expression,
                mode="eval",
            )

            result = self._evaluate_node(
                parsed_expression.body,
            )

        except SyntaxError as error:
            raise ValueError(
                "invalid_expression"
            ) from error

        except ZeroDivisionError as error:
            raise ValueError(
                "division_by_zero"
            ) from error

        except Exception as error:
            raise ValueError(
                "calculation_error"
            ) from error

        return {
            "operation": "expression",
            "operands": expression,
            "result": result,
        }

    def _evaluate_node(
        self,
        node: Any,
    ) -> float:
        if isinstance(node, ast.Constant):
            return float(node.value)

        if isinstance(node, ast.BinOp):
            left_value = self._evaluate_node(node.left)
            right_value = self._evaluate_node(node.right)

            operation = self.AST_OPERATORS.get(type(node.op))

            if operation is None:
                raise ValueError(
                    "Unsupported mathematical operation."
                )

            tool = self._tool_registry[operation]

            return tool(left_value, right_value)

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -self._evaluate_node(node.operand)

        raise ValueError(
            "Invalid mathematical expression."
        )