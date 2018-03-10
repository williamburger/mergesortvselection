import runtime
import plotly.plotly as py
import plotly.graph_objs as go

def run_and_plot():
    merge_times = []
    selection_times = []
    times = []
    for i in range(5,1000):
        [x,y] = runtime.test_runtime(i)
        merge_times.append(x)
        selection_times.append(y)
        times.append(i)
    trace0 = go.Scatter(
        x = times,
        y = merge_times,
        mode = 'markers',
        name = 'merge'
    )
    trace1 = go.Scatter(
        x = times,
        y = selection_times,
        mode = 'markers',
        name = 'selection'
    )
    data = [trace0, trace1]
    py.plot(data, filename='scatter-plot')
