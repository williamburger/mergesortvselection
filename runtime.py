import math
import random
import lower_median
import datetime

def test_runtime(B=[]):
    
    time_merge_initial = datetime.datetime.now() 
    result_merge = lower_median.merge_median(B)
    time_merge_final = datetime.datetime.now()

    time_selection_initial = datetime.datetime.now()
    result_selection = lower_median.selection_median(B)
    time_selection_final = datetime.datetime.now()

    if(result_merge[0] == result_selection[0]):
        return [(time_merge_final-time_merge_initial).total_seconds(), (time_selection_final - time_selection_initial).total_seconds(),result_merge[1],result_selection[1]]
    else:
        print("FAILED")
        return [None,None,None,None]

