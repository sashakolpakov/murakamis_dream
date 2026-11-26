from pathlib import Path
import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.NOTES=[]
m.PAGES=['guide/frontier.html','notes/actual_balanced_terminal_fan_volume.html']
m.SHOTS={'guide/frontier.html':'frontier','notes/actual_balanced_terminal_fan_volume.html':'final-planar-note'}
sys.exit(m.main())
