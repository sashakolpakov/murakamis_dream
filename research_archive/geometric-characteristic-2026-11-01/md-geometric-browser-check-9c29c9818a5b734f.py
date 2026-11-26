from pathlib import Path
import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.NOTES=['actual_all_circle_geometric_characteristic','actual_main_meridian_filtered_characteristic','actual_conway_pointed_quantum_a_volume']
m.PAGES=m.GUIDES+['figures.html']+[f'notes/{stem}.html' for stem in m.NOTES]
m.SHOTS={'index.html':'overview','guide/results.html':'results','notes/actual_all_circle_geometric_characteristic.html':'geometric-longitude'}
sys.exit(m.main())
