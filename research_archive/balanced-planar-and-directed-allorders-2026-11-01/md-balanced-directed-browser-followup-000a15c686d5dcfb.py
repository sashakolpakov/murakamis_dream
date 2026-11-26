from pathlib import Path
import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.NOTES=[]
m.PAGES=['guide/frontier.html']
m.SHOTS={'guide/frontier.html':'frontier'}
sys.exit(m.main())
