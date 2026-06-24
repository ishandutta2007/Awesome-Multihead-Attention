import os
import re
import subprocess

GIT_CMD = ['git', '--git-dir=C:/Users/ishan/Documents/Projects/Awesome-Multihead-Attention/.git', '--work-tree=C:/Users/ishan/Documents/Projects/Awesome-Multihead-Attention']

def run_git(commit_msg):
    print(f"Running git commit: {commit_msg}")
    subprocess.run(GIT_CMD + ['add', '.'])
    subprocess.run(GIT_CMD + ['commit', '-m', commit_msg])
    subprocess.run(GIT_CMD + ['push'])

# Step 1: Create pages
pages_dir = "pages"
os.makedirs(pages_dir, exist_ok=True)
pages = {
    "Standard Multi-Head Attention": {"file": "standard-mha.md", "title": "Standard Multi-Head Attention"},
    "Multi-Query Attention": {"file": "mqa.md", "title": "Multi-Query Attention"},
    "Grouped-Query Attention": {"file": "gqa.md", "title": "Grouped-Query Attention"},
    "Bidirectional Attention (Encoder)": {"file": "bidirectional-attention.md", "title": "Bidirectional Attention"},
    "Causal Attention (Decoder)": {"file": "causal-attention.md", "title": "Causal Attention"},
    "Prefix / Masked Hybrid Attention": {"file": "prefix-attention.md", "title": "Prefix / Masked Hybrid Attention"},
    "FlashAttention Kernels": {"file": "flash-attention.md", "title": "FlashAttention Kernels"},
    "Linear Attention (Performer / Linear Transformer)": {"file": "linear-attention.md", "title": "Linear Attention"},
    "Multi-Head Latent Attention (MLA)": {"file": "mla.md", "title": "Multi-Head Latent Attention"},
    "Autoregressive Text Generation Foundations": {"file": "autoregressive.md", "title": "Autoregressive Text Generation Foundations"},
    "Cross-Modal Vision-Language Alignment": {"file": "cross-modal.md", "title": "Cross-Modal Vision-Language Alignment"},
    "Spatio-Temporal Video Synthesis": {"file": "video-synthesis.md", "title": "Spatio-Temporal Video Synthesis"}
}

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

for key, p in pages.items():
    content = f"# {p['title']}\n\nDetailed information about {p['title']}.\n\n## Diagram\n```mermaid\nflowchart TD\n  Node1 --> Node2\n```\n"
    with open(os.path.join(pages_dir, p["file"]), "w") as f:
        f.write(content)
    # Link the items in tables
    # Find the exact bold text matching the key (possibly with parenthesis like (Vaswani et al.))
    # It might be like **Standard Multi-Head Attention (Vaswani et al., 2017)**
    # We replace it with **[Standard Multi-Head Attention (Vaswani et al., 2017)](pages/...)**
    # But ONLY if it's not already linked!
    if f"](pages/{p['file']})" not in readme:
        if " (" in key:
            # key has parenthesis, match exact
            readme = readme.replace(f"**{key}**", f"**[{key}](pages/{p['file']})**")
        else:
            # key doesn't have parenthesis in the dict, but in README it might
            # Let's use regex
            readme = re.sub(r"\*\*(" + re.escape(key) + r"[^\*]*)\*\*", f"**[\\1](pages/{p['file']})**", readme)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("detailed pages created")

# Step 2: Decorate and SEO
assets_dir = "assets"
os.makedirs(assets_dir, exist_ok=True)
banner_svg = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#2b2b2b"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="40" fill="#ffffff" font-family="Arial">Awesome Multihead Attention</text>
</svg>'''
with open(os.path.join(assets_dir, "banner.svg"), "w") as f:
    f.write(banner_svg)

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

banner_md = f"<p align='center'>\n  <img src='assets/banner.svg' alt='Awesome Multihead Attention Banner' />\n</p>\n<p align='center'>\n  {left_badges}\n  {right_badge}\n</p>\n\n<p align='center'><b>A curated list of awesome multi-head attention variants, optimizations, and applications in modern AI models.</b></p>\n\n"

if "Awesome Multihead Attention Banner" not in readme:
    readme = re.sub(r'# Awesome-Multihead-Attention', f'# 🚀 Awesome-Multihead-Attention\n{banner_md}', readme)
    readme = readme.replace('## Multi-Head Attention (MHA): Evolution, Variants, & Applications', '## 🧠 Multi-Head Attention (MHA): Evolution, Variants, & Applications')
    readme = readme.replace('## 1. The Chronological Evolution', '## ⏳ 1. The Chronological Evolution')
    readme = readme.replace('## 2. Structural & Spatial Masking Variants', '## 🏗️ 2. Structural & Spatial Masking Variants')
    readme = readme.replace('## 3. Mathematical & Scale Optimization Types', '## 🧮 3. Mathematical & Scale Optimization Types')
    readme = readme.replace('## 4. Cross-Domain Applications', '## 🌐 4. Cross-Domain Applications')

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("seo optimised and decorated")

# Step 3: Star History
folder_name = "Awesome-Multihead-Attention"
star_history = f'''
## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
if "Star History Chart" not in readme:
    readme += star_history
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    run_git("star history added")

# Step 4: Fix chartrepos
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

if "chartrepos" in readme:
    readme = readme.replace("chartrepos", "chart?repos")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    run_git("fixed star plot")
else:
    print("No chartrepos found.")

# Step 5: Replace awesome link
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

if "https://github.com/sindresorhus/awesome" in readme:
    readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    run_git("invalid awesome link fixed")
else:
    print("No sindresorhus awesome link found.")

print("All done.")
