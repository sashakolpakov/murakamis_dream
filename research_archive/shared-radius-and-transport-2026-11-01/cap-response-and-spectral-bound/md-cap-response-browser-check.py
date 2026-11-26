from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import json
from playwright.sync_api import sync_playwright

ROOT = Path("/private/tmp/murakamis_dream-publication/docs")
OUT = Path("/private/tmp/md-cap-response-browser")
OUT.mkdir(exist_ok=True)

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_address[1]}/"
pages = ["guide/methods.html", "guide/frontier.html", "guide/audits.html",
 "notes/research_cap_common_axis_bound.html", "notes/research_cap_uniform_spectral_gap.html",
 "notes/research_cap_dirichlet_response_region.html", "notes/research_protected_cap_coupled_norm.html"]
results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for width in (1440, 390):
        page = browser.new_page(viewport={"width": width, "height": 1000})
        for url in pages:
            errors = []
            def capture(error):
                errors.append(str(error))
            page.on("pageerror", capture)
            response = page.goto(base + url, wait_until="networkidle")
            data = page.evaluate("""() => ({
                math: document.querySelectorAll('math').length,
                mathErrors: document.querySelectorAll('merror').length,
                invisibleMath: [...document.querySelectorAll('math')].filter(
                    x => !x.getBoundingClientRect().width || !x.getBoundingClientRect().height
                ).length,
                brokenImages: [...document.images].filter(
                    x => !x.complete || !x.naturalWidth
                ).map(x => x.src),
                documentOverflow: document.documentElement.scrollWidth > innerWidth + 2
            })""")
            data.update(page=url, width=width, http=response.status, scriptErrors=errors)
            results.append(data)
            if url == "guide/methods.html":
                page.locator("#summing-the-exterior-before-estimating-the-cap").scroll_into_view_if_needed()
                page.screenshot(path=str(OUT / f"methods-{width}.png"))
                page.locator('img[src*="cap-dirichlet-response"]').scroll_into_view_if_needed()
                page.screenshot(path=str(OUT / f"response-figure-{width}.png"))
                if width == 1440:
                    page.locator('img[src*="cap-dirichlet-response"]').screenshot(path=str(OUT / 'response-figure.png'))
            page.remove_listener("pageerror", capture)
        page.goto(base + "sphinx/mathematics.html", wait_until="networkidle")
        results.append({"legacy": "sphinx/mathematics.html", "width": width,
                        "redirectedToGuide": "/guide/mechanism.html" in page.url})
        page.close()
    browser.close()
server.shutdown()
failures = [r for r in results if
            (r.get("http", 200) != 200 or r.get("mathErrors") or r.get("invisibleMath")
             or r.get("brokenImages") or r.get("documentOverflow") or r.get("scriptErrors")
             or r.get("redirectedToGuide") is False)]
report = {"checks": len(results), "failures": failures, "pages": results}
(OUT / "results.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"checks": len(results), "failures": failures}, indent=2))
if failures:
    raise SystemExit(1)
