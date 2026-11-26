import importlib.util
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.PAGES=['index.html','guide/results.html','guide/frontier.html','guide/geometry.html','guide/manuscript.html','guide/audits.html','figures.html']+[
'notes/'+s+'.html' for s in ['actual_all_circle_local_message_volume','actual_all_circle_vertexwise_geometry','exact_tree_messages_and_strip_bounds','actual_main_meridian_filtered_characteristic']]
m.SHOTS={'guide/results.html':'results','notes/actual_all_circle_local_message_volume.html':'local-theorem','notes/actual_main_meridian_filtered_characteristic.html':'characteristic'}
m.main()
