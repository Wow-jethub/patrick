import json, sys, pathlib, time
from playwright.sync_api import sync_playwright

base = pathlib.Path(__file__).parent
tl = json.load(open(base/"timeline.json"))
html = (base/"page.html").read_text(encoding="utf-8").replace("__TIMELINE__", json.dumps(tl))
(base/"page_final.html").write_text(html, encoding="utf-8")

mode = sys.argv[1] if len(sys.argv)>1 else "test"
FPS = 30

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", args=["--force-device-scale-factor=1"])
    pg = b.new_page(viewport={"width":1920,"height":1080})
    pg.goto((base/"page_final.html").as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(2500)  # let fonts settle
    if mode == "test":
        samples = [1.6, 8.5, 20.0, 31.0, 42.0, 54.0, 66.0, 78.0, 87.0]
        (base/"test").mkdir(exist_ok=True)
        for t in samples:
            pg.evaluate(f"render({t})")
            pg.screenshot(path=str(base/"test"/f"t{str(t).replace('.','_')}.png"))
        print("test frames done")
    else:
        outdir = base/"frames"; outdir.mkdir(exist_ok=True)
        total = tl["total"]
        nframes = int(total*FPS)
        t0 = time.time()
        for i in range(nframes):
            pg.evaluate(f"render({i/FPS:.4f})")
            pg.screenshot(path=str(outdir/f"f{i:05d}.jpg"), type="jpeg", quality=92)
            if i % 300 == 0:
                el = time.time()-t0
                print(f"{i}/{nframes} frames, {el:.0f}s elapsed", flush=True)
        print(f"done {nframes} frames in {time.time()-t0:.0f}s")
    b.close()
