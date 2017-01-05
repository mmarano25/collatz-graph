import plotly as plt
import plotly.graph_objs as go

TESTS_ON = True

def collatz_steps(num: int) -> int:
    """runs the collatz conjecture on num, returns number of steps"""
    if num == 0:
        return 0
    n = 0
    while num != 1:
        n += 1
        if (num % 2) == 0:
            num /= 2
        else:
            num = (num * 3) + 1
    return n


# tests:
if TESTS_ON:
    assert collatz_steps(0) == 0
    assert collatz_steps(10) == 6
    assert collatz_steps(1000) == 111
    assert collatz_steps(123214) == 211

"""
plotly_data = [
    go.Histogram(
        "data here"
    )
]

plt.offline.plot(plotly_data)
"""