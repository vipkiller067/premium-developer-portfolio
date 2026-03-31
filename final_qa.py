import os
import re

print("Running Final Vercel QA and Form Integration...")

index_path = r"c:\Users\ADMIN\Desktop\portfolio website\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Contact Form Setup
old_form_action = r'action="https://formspree.io/f/YOUR_FORMSPREE_ENDPOINT"'
new_form_action = 'action="https://formspree.io/f/mlgondbj"'
html = html.replace(old_form_action, new_form_action)

# Also removing onsubmit just in case the legacy string persists
html = re.sub(r'onsubmit="event\.preventDefault\(\); alert\(\'Backend not yet connected\.\'\);"', '', html)

# 2. SEO Fixes
html = re.sub(r'<title>.*?</title>', '<title>Vaibhav Pandey | Software Developer Portfolio</title>', html, count=1)
html = re.sub(r'<meta name="description".*?>', '<meta name="description" content="Vaibhav Pandey - B.Tech IT student and developer building real-world projects.">', html, count=1)
if 'name="viewport"' in html:
    html = re.sub(r'<meta name="viewport".*?>', '<meta name="viewport" content="width=device-width, initial-scale=1.0">', html, count=1)

# Ensure Favicon matches exactly
if 'href="static/images/favicon.svg"' not in html:
    html = re.sub(r'<link rel="icon".*?>', '<link rel="icon" type="image/svg+xml" href="static/images/favicon.svg">', html, count=1)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Final Vercel QA successfully embedded.")
