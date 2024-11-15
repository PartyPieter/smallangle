import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    pass


@cmd_group.command()
#@click.argument("smallangle")
@click.option(
    "--number",
    "-n",
    default = 10

)
def sin(number):
    """Calculate the sin of NUMBER values between 0 and 2 pi

    NUMBER is the amount values between 0 and 2 pi that the sin is calculated of
"""  
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
#@click.argument("smallangle")
@click.option(
    "--number",
    "-n",
    default = 10

)
def tan(number):
    """Calculate the tan of NUMBER values between 0 and 2 pi

       NUMBER is the amount values between 0 and 2 pi that the tan is calculated of
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)






if __name__ == "__main__":
    cmd_group()

