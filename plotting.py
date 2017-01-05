import plotly as plt
import plotly.graph_objs as go
import collatz


def plot_collatz_to_file(num:int, filename="temp_file.png"):
    """plots collatz histo of 1 to num, saves graph under name filename"""
    collatz_data = collatz.collatz_from_one_to_x(num)
    plotly_data = [
        go.Histogram(
            x=collatz_data,
            nbinsx=len(set(collatz_data))
        )
    ]

    plt.plotly.image.save_as(plotly_data, "temp_file.png")
    # plt.offline.plot(plotly_data, output_type="div", auto_open=False, image="png")
