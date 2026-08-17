#!/usr/bin/env python3
"""Assembles marvel_rewatch_app.html from app_shell.html + data.js + the embedded fonts.
Run from this directory: python3 build.py
"""
import pathlib

here = pathlib.Path(__file__).parent
shell = (here / "app_shell.html").read_text(encoding="utf-8")
data_js = (here / "data.js").read_text(encoding="utf-8")
anton = (here / "fonts" / "anton-400.b64").read_text(encoding="utf-8")
pop400 = (here / "fonts" / "poppins-400.b64").read_text(encoding="utf-8")
pop500 = (here / "fonts" / "poppins-500.b64").read_text(encoding="utf-8")
pop600 = (here / "fonts" / "poppins-600.b64").read_text(encoding="utf-8")
pop700 = (here / "fonts" / "poppins-700.b64").read_text(encoding="utf-8")

out = (shell.replace("__DATA_JS__", data_js)
            .replace("__FONT_ANTON__", anton)
            .replace("__FONT_POPPINS_400__", pop400)
            .replace("__FONT_POPPINS_500__", pop500)
            .replace("__FONT_POPPINS_600__", pop600)
            .replace("__FONT_POPPINS_700__", pop700))
out_path = here / "marvel_rewatch_app.html"
out_path.write_text(out, encoding="utf-8")
print(f"Built {out_path} ({len(out):,} bytes)")
