import os
import sys
import glob

if os.path.exists("tempfolder"):
    for CleanUp in glob.glob("tempfolder/*.*"):
        print CleanUp
        if not CleanUp.endswith('form.html'):
            os.remove(CleanUp)
