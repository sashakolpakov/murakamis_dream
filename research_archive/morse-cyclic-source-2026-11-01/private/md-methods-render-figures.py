from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path('/private/tmp/murakamis_dream-publication')
out=Path('/private/tmp/md-methods-browser-validation')
exe='/Users/sasha/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=exe)
    page=b.new_page(viewport={'width':1000,'height':680},device_scale_factor=1)
    page.goto((root/'book/figures/methods-proof-map.svg').as_uri())
    page.screenshot(path=str(out/'proof-map.png'))
    b.close()
