import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.PAGES=['notes/actual_all_circle_geometric_characteristic.html']
m.REDIRECTS={}
m.SHOTS={}
sys.exit(m.main())
