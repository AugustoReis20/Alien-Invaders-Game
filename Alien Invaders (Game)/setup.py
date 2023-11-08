import cx_Freeze
import sys
sys.setrecursionlimit(10000)

executables = [cx_Freeze.Executable('alieninvaders.py')]

cx_Freeze.setup(
    name="Alien Invaders (Game)",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['images', 'audio']}},

    executables = executables
    
)