with open('index.html', 'r') as f:
    html = f.read()

OLD = (
    "  /* News mobile: single column */\n"
    "  .news-grid{\n"
    "    grid-template-columns:1fr !important;\n"
    "  }\n"
    "  /* News cards: prevent image overflow */\n"
    "  .news-card img,.news-card-img{\n"
    "    max-width:100% !important;\n"
    "    height:auto !important;\n"
    "  }"
)

NEW = (
    "  /* News mobile: single column */\n"
    "  .news-grid{\n"
    "    grid-template-columns:1fr !important;\n"
    "  }\n"
    "  /* News Hero: 16:9 ratio on mobile */\n"
    "  .news-hero-img, .news-hero-img-placeholder{\n"
    "    height:auto !important;\n"
    "    aspect-ratio:16/9 !important;\n"
    "    max-height:220px !important;\n"
    "  }\n"
    "  /* News grid cards: horizontal row layout on mobile */\n"
    "  .news-grid-card{\n"
    "    display:flex !important;\n"
    "    flex-direction:row !important;\n"
    "    align-items:flex-start !important;\n"
    "    gap:12px !important;\n"
    "  }\n"
    "  .news-grid-img, .news-grid-img-placeholder{\n"
    "    width:90px !important;\n"
    "    min-width:90px !important;\n"
    "    height:68px !important;\n"
    "    flex-shrink:0 !important;\n"
    "    border-radius:6px !important;\n"
    "  }\n"
    "  .news-grid-body{\n"
    "    flex:1 !important;\n"
    "    min-width:0 !important;\n"
    "    padding:8px 12px 8px 0 !important;\n"
    "  }\n"
    "  /* News cards: prevent image overflow */\n"
    "  .news-card img,.news-card-img{\n"
    "    max-width:100% !important;\n"
    "    height:auto !important;\n"
    "  }"
)

if OLD in html:
    html = html.replace(OLD, NEW, 1)
    print('PATCH OK: News Hero 16:9 + grid-card row layout added')
else:
    print('PATCH FAILED - target not found')
    # Debug: show what's around the news-grid section
    idx = html.find('/* News mobile: single column */')
    if idx >= 0:
        print('Found at char', idx)
        print(repr(html[idx:idx+300]))

with open('index.html', 'w') as f:
    f.write(html)
