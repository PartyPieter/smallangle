import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(    
    "--number",
    "-n",
    default = 10
)

def sin(number):
    """Calculate the sin of [NUMBER] values between 0 and 2 pi

    NUMBER is the amount of values between 0 and 2 pi that the sin is calculated of
"""  
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    help = "amount of values betwee 0 and 2 pi",
    default = 10
)

def tan(number):
    """Calculate the tan of [NUMBER] values between 0 and 2 pi
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

@cmd_group.command()
@click.argument("value" , type = float)
def approx(value):
    """Calculates the biggest angle for which the small angle approximation is still valid in radians

    Args:
    value (float): The value for which the biggest angle that upholds the small angle approximation is given
    """    
    x = 0.000
    while np.abs(x - np.sin(x)) < value:
        x = x + 0.001

    x = x - 0.001    
    print(f"Biggest angle for which the small angle approx is given: {x} rads")

if __name__ == "__main__":
    cmd_group()

