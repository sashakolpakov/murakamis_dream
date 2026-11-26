import importlib.util
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.PAGES=['index.html','guide/results.html','guide/frontier.html','guide/audits.html','figures.html','notes/actual_main_meridian_trivalent_component_bound.html','notes/actual_main_meridian_trivalent_filled_volume.html','notes/actual_main_meridian_grouped_wire_packet.html','notes/actual_main_meridian_filled_volume.html','notes/actual_main_meridian_preferred_cusp.html','notes/actual_main_meridian_exact_scalar.html']
m.REDIRECTS={}
m.SHOTS={'guide/results.html':'results','notes/actual_main_meridian_trivalent_filled_volume.html':'trivalent-volume','notes/actual_main_meridian_trivalent_component_bound.html':'trivalent-component'}
m.main()
