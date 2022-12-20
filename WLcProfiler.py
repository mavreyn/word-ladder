#
#
# I'm going to try to find out what's taking so long with the code
# Going to use the cProfile module and myabe SnakeViz
#
# Maverick Reynolds
# 02-22-2022
#
#

from WordLadder import *
# import cProfile, pstats



att_wrds_prnts = []
print(is_word_present('masks', 'tasks', 15))

#profiler = cProfile.Profile()
#profiler.enable()

# cProfile.run('is_word_present(\'masks\', \'break\', 20)', sort='time')

# profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('tottime')
# stats.print_stats()