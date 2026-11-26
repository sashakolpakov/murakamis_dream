from pathlib import Path
import importlib.util,sys
spec=importlib.util.spec_from_file_location('checks','/private/tmp/md-editorial-browser-check.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.NOTES=['actual_balanced_terminal_fan_volume','actual_all_circle_directed_all_orders']
m.PAGES=m.GUIDES+['figures.html']+[f'notes/{stem}.html' for stem in m.NOTES]
m.SHOTS={'index.html':'overview','guide/results.html':'results','notes/actual_balanced_terminal_fan_volume.html':'planar-proof','notes/actual_all_circle_directed_all_orders.html':'directed-allorders'}
sys.exit(m.main())
