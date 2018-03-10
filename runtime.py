import math
import random
import lower_median
import datetime

def test_runtime(num):
    B = []
    for i in range(0,num):
        B.append(random.randint(0,1000))
    
    time_merge_initial = datetime.datetime.now() 
    result_merge = lower_median.merge_median(B)
    time_merge_final = datetime.datetime.now()

    time_selection_initial = datetime.datetime.now()
    result_selection = lower_median.selection_median(B)
    time_selection_final = datetime.datetime.now()

    if(result_merge == result_selection):
        return [(time_merge_final-time_merge_initial).total_seconds(), (time_selection_final - time_selection_initial).total_seconds()]
    else:
        print("FAILED")
        return None

