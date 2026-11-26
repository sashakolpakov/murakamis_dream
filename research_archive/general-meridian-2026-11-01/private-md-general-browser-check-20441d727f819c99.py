import importlib.util
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.PAGES=['index.html','guide/results.html','guide/frontier.html','guide/audits.html','guide/manuscript.html','figures.html','notes/actual_main_meridian_same_index_obstruction.html','notes/actual_main_meridian_high_fourier_reflection.html','notes/actual_main_meridian_component_pressure.html','notes/actual_main_meridian_general_component_comparison.html','notes/actual_main_meridian_grouped_wire_packet.html','notes/actual_main_meridian_joint_filling_transform.html','notes/actual_main_meridian_filled_volume.html','notes/actual_main_meridian_preferred_cusp.html','notes/actual_main_meridian_exact_scalar.html']
m.REDIRECTS={'sphinx/mathematics.html':'guide/mechanism.html'}
m.SHOTS={'guide/results.html':'results','notes/actual_main_meridian_general_component_comparison.html':'general-component','notes/actual_main_meridian_component_pressure.html':'component-pressure','guide/manuscript.html':'manuscript'}
m.main()
