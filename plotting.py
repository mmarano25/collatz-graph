import plotly as plt
import plotly.graph_objs as go
import collatz


def plot_collatz_to_file(num:int, filename:str):
    """plots collatz histo of 1 to num, saves graph under name filename"""
    collatz_data = collatz.collatz_from_one_to_x(num)
    plotly_data = [
        go.Histogram(
            x=collatz_data,
            nbinsx=len(set(collatz_data))
        )
    ]

    plt.offline.plot(plotly_data, output_type="file", filename=filename)
