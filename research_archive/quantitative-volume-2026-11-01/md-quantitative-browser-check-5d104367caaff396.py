import importlib.util
s=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
m.PAGES=['index.html','guide/results.html','guide/frontier.html','guide/geometry.html','guide/manuscript.html','guide/audits.html','figures.html']+[
 'notes/actual_all_circle_'+s+'.html' for s in ['quantitative_volume','octahedral_decomposition','angular_octahedra','geometric_completion','preferred_cusp','curvature_filling_limit']]
m.PAGES.append('notes/actual_conway_pointed_quantum_a_volume.html')
m.SHOTS={'notes/actual_all_circle_quantitative_volume.html':'theorem','guide/results.html':'results','guide/geometry.html':'geometry'}
m.main()
