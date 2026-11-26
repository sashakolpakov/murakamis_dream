import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.GUIDES.insert(4,'guide/methods.html')
m.PAGES=['index.html','guide/methods.html','guide/notation.html','guide/manuscript.html','guide/frontier.html','notes/actual_morse_geometric_contribution.html','notes/actual_morse_cross_filling_period.html']
m.SHOTS={'guide/methods.html':'methods','guide/notation.html':'notation','guide/manuscript.html':'manuscript','guide/frontier.html':'frontier'}
sys.exit(m.main())
