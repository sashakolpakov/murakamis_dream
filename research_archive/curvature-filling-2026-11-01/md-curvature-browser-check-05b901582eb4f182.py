import importlib.util
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.PAGES=['guide/frontier.html','guide/audits.html','guide/manuscript.html',
         'notes/actual_all_circle_curvature_filling_limit.html',
         'notes/all_circle_uniform_newton_bounds.html']
m.REDIRECTS={'sphinx/mathematics.html':'guide/mechanism.html'}
m.SHOTS={'guide/frontier.html':'frontier',
         'notes/actual_all_circle_curvature_filling_limit.html':'curvature-limit'}
m.main()
