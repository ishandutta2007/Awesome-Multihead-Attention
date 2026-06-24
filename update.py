import os
import re

# Create pages
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
    "Autoregressive Text Generation Foundations": {"file": "autoregressive.md", "title": "Autoregressive Text Generation"},
    "Cross-Modal Vision-Language Alignment": {"file": "cross-modal.md", "title": "Cross-Modal Vision-Language Alignment"},
    "Spatio-Temporal Video Synthesis": {"file": "video-synthesis.md", "title": "Spatio-Temporal Video Synthesis"}
}

for key, p in pages.items():
    content = f"# {p['title']}\n\nDetailed information about {p['title']}.\n\n## Diagram\n```mermaid\nflowchart TD\n  Node1 --> Node2\n```\n"
    with open(os.path.join(pages_dir, p["file"]), "w") as f:
        f.write(content)

# Create banner
assets_dir = "assets"
os.makedirs(assets_dir, exist_ok=True)
banner_svg = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#2b2b2b"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="40" fill="#ffffff" font-family="Arial">Awesome Multihead Attention</text>
</svg>'''
with open(os.path.join(assets_dir, "banner.svg"), "w") as f:
    f.write(banner_svg)

# Edit README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Badges
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

banner_md = f"<p align='center'>\\n  <img src='assets/banner.svg' alt='Banner' />\\n</p>\\n<p align='center'>\\n  {left_badges}\\n  {right_badge}\\n</p>\\n"

# Replace heading and add banner
readme = re.sub(r'# Awesome-Multihead-Attention', f'# 🚀 Awesome-Multihead-Attention\\n{banner_md}', readme)
readme = readme.replace('## Multi-Head Attention (MHA): Evolution, Variants, & Applications', '## 🧠 Multi-Head Attention (MHA): Evolution, Variants, & Applications')
readme = readme.replace('## 1. The Chronological Evolution', '## ⏳ 1. The Chronological Evolution')
readme = readme.replace('## 2. Structural & Spatial Masking Variants', '## 🏗️ 2. Structural & Spatial Masking Variants')
readme = readme.replace('## 3. Mathematical & Scale Optimization Types', '## 🧮 3. Mathematical & Scale Optimization Types')
readme = readme.replace('## 4. Cross-Domain Applications', '## 🌐 4. Cross-Domain Applications')

# Link the items in tables
for key, p in pages.items():
    readme = readme.replace(f"**{key}**", f"**[{key}](pages/{p['file']})**")
    # also handle versions with Vaswani et al. etc
    readme = re.sub(rf"\*\*{key}.*?\*\*", f"**[{key}](pages/{p['file']})**", readme)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
