import runtime
import plotly as py
import plotly.graph_objs as go
import inversions
import random

def run_and_plot(test_cases):
    merge_times = []
    selection_times = []
    times = []
    initial_inversions = []
    merge_inversions_ratios = []
    select_inversions_ratios = []
    for i in test_cases:
        B = []
        mergearray = []
        selectarray = []
        for j in range(0,i):
            B.append(random.randint(0,1000))
        [numinversions, trash] = inversions.count_inversions(B)
        initial_inversions.append(numinversions)
        try:
            [x, y, mergearray, selectarray] = runtime.test_runtime(B)
        except:
            print("BOOOO")
        merge_inversions_ratios.append(inversions.count_inversions(mergearray)[0]/numinversions)
        select_inversions_ratios.append(float(inversions.count_inversions(selectarray)[0])/numinversions)
        merge_times.append(x)
        selection_times.append(y)
        times.append(i)
    layout = go.Layout(
        title='Selection Sort Versus Merge Sort',
        xaxis=dict(
            title='size of array',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
       yaxis=dict(
            title='time in seconds',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
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
    trace2 = go.Scatter(
        x = select_inversions_ratios,
        y = selection_times,
        mode = 'markers',
        name = 'inversions ratio versus run time'
    ) 
    trace3 = go.Scatter(
        x = initial_inversions,
        y = selection_times,
        mode = 'markers',
        name = 'inversions number versus run time'
    )
    trace4 = go.Scatter(
        x = initial_inversions,
        y = select_inversions_ratios,
        mode = 'markers',
        name = 'inversions number versus run time'
    ) 
    data = [trace0, trace1]
    fig = go.Figure(data=data,layout=layout)
    py.offline.plot(fig,filename='selectionvsmerge.html')
    layout = go.Layout(
        title='Inversions Ratios versus time for Selection Sort',
        xaxis=dict(
            title='Inversions Ratio',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
       yaxis=dict(
            title='time in seconds',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=[trace2],layout=layout)
    py.offline.plot(fig,filename='inversionsratios.html')
    layout = go.Layout(
        title='Initial Inversions number versus the time for Selection Sort',
        xaxis=dict(
            title='Number of initial Inversions in Array',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
       yaxis=dict(
            title='time in seconds',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=[trace3],layout=layout)
    py.offline.plot(fig,filename='inversions.html')
    layout = go.Layout(
        title='Number of inversions versus the inversion ratio for Selection Sort',
        xaxis=dict(
            title='Number of initial inversions',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
       yaxis=dict(
            title='inversions ratio',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=[trace4],layout=layout)
    py.offline.plot(fig ,filename='numvratio') 
