#!/usr/bin/env python3
"""Assemble the Market Access Atlas: inline fonts + logos."""
import pathlib

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"

tpl = (HERE / "atlas.tpl.html").read_text(encoding="utf-8")
out = (tpl
       .replace("/*__FONTFACE__*/", (ASSETS / "fontface.css").read_text(encoding="utf-8"))
       .replace("__SOCIOS__", (ASSETS / "socios_datauri.txt").read_text().strip())
       .replace("__CHILIZ__", (ASSETS / "chiliz_datauri.txt").read_text().strip())
       .replace("__SECURITIZE__", (ASSETS / "securitize_datauri.txt").read_text().strip()))

for ph in ("__SOCIOS__", "__CHILIZ__", "__SECURITIZE__", "__FONTFACE__"):
    assert ph not in out, f"placeholder left unfilled: {ph}"
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written: {len(out):,} bytes")
