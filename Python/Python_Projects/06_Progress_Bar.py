"""
Python Progress Bar:

Create python progress bar with tqdm.

"""

import time
from tqdm import tqdm

# We can prefix a text description to the progress bar by specifying the desc argument
for i in tqdm(range(0, 50), desc="Processing"):
    time.sleep(0.1)

'''
And if we want a more minimal bar we can use the bar format argument to specify just the description bar
and percentage 
'''
for i in tqdm(range(0, 50), desc="Processing", bar_format='{desc}: |{bar}| {percentage:.1f}%'):
    time.sleep(0.1)
