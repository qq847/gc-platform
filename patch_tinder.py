#!/usr/bin/env python3
"""Task-014: Projects Tinder card mode for < 480px"""

with open('index.html', 'r') as f:
    html = f.read()

original_len = len(html)

# ─── PATCH 1: Add Tinder CSS (< 480px) ───────────────────────────────────────
# Insert after the existing `#pc-proj-cards { grid-template-columns:repeat(2,1fr) }` block
OLD1 = """  /* Projects grid: 4→2 cols */
  #pc-proj-cards{
    grid-template-columns:repeat(2,1fr) !important;
    gap:12px !important;
  }"""

NEW1 = """  /* Projects grid: 4→2 cols */
  #pc-proj-cards{
    grid-template-columns:repeat(2,1fr) !important;
    gap:12px !important;
  }
}
/* ═══════════════════════════════════════════════════════════════
   MOBILE PHONE: < 480px  — Tinder card mode for Projects
═══════════════════════════════════════════════════════════════ */
@media (max-width:479px){
  /* Tinder mode: hide the grid, show the tinder overlay */
  #pc-proj-cards{
    display:none !important;
  }
  #proj-tinder-wrap{
    display:flex !important;
  }"""

p1_ok = OLD1 in html
if p1_ok:
    html = html.replace(OLD1, NEW1, 1)
    print('PATCH 1 OK: Tinder CSS added')
else:
    print('PATCH 1 FAILED: target not found')

# ─── PATCH 2: Add Tinder HTML inside projects-panel ──────────────────────────
# Insert the tinder overlay div before the closing </div><!-- /projects-panel -->
OLD2 = '  </div>\n</div><!-- /projects-panel -->'

NEW2 = '''  </div>
  <!-- TINDER CARD MODE (mobile < 480px only) -->
  <div id="proj-tinder-wrap" style="display:none;position:absolute;inset:0;top:42px;flex-direction:column;align-items:center;justify-content:center;background:#f3f2ef;padding:16px;gap:16px;z-index:10">
    <!-- Card stack -->
    <div id="proj-tinder-stack" style="position:relative;width:100%;max-width:360px;height:480px">
      <!-- Cards are injected by JS -->
    </div>
    <!-- Action buttons -->
    <div style="display:flex;gap:24px;align-items:center">
      <button onclick="projTinderSwipe('left')" style="width:56px;height:56px;border-radius:50%;background:#fff;border:2px solid #e74c3c;color:#e74c3c;font-size:22px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,0.12);display:flex;align-items:center;justify-content:center" title="Pass">✕</button>
      <button onclick="projTinderSwipe('up')" style="width:44px;height:44px;border-radius:50%;background:#fff;border:2px solid #3498db;color:#3498db;font-size:18px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,0.12);display:flex;align-items:center;justify-content:center" title="View Details">↑</button>
      <button onclick="projTinderSwipe('right')" style="width:56px;height:56px;border-radius:50%;background:#fff;border:2px solid #2ecc71;color:#2ecc71;font-size:22px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,0.12);display:flex;align-items:center;justify-content:center" title="Like">♥</button>
    </div>
    <!-- Counter -->
    <div id="proj-tinder-counter" style="font-size:12px;color:#999"></div>
  </div>
</div><!-- /projects-panel -->'''

p2_ok = OLD2 in html
if p2_ok:
    html = html.replace(OLD2, NEW2, 1)
    print('PATCH 2 OK: Tinder HTML added')
else:
    print('PATCH 2 FAILED: target not found')
    # Try alternate
    ALT2 = '</div>\n</div><!-- /projects-panel -->'
    if ALT2 in html:
        html = html.replace(ALT2, NEW2.replace('  </div>\n', '</div>\n'), 1)
        print('PATCH 2 ALT OK')
    else:
        print('PATCH 2 ALT ALSO FAILED')

# ─── PATCH 3: Add Tinder JS functions ────────────────────────────────────────
# Insert before the closing </script> or before a known function
TINDER_JS = """
// ═══ PROJECTS TINDER MODE ═══════════════════════════════════════════════════
let _tinderCards = [];
let _tinderIdx = 0;
let _tinderTouchStartX = 0;
let _tinderTouchStartY = 0;

function projTinderInit(cards) {
  _tinderCards = cards || [];
  _tinderIdx = 0;
  projTinderRender();
}

function projTinderRender() {
  const stack = document.getElementById('proj-tinder-stack');
  const counter = document.getElementById('proj-tinder-counter');
  if (!stack) return;
  stack.innerHTML = '';
  if (_tinderIdx >= _tinderCards.length) {
    stack.innerHTML = '<div style="text-align:center;padding:40px 20px;color:#999"><div style="font-size:48px;margin-bottom:12px">🎮</div><div style="font-size:15px;font-weight:700;color:#333">You\'ve seen all projects!</div><div style="font-size:12px;margin-top:8px">Check back later for more</div></div>';
    if (counter) counter.textContent = '';
    return;
  }
  // Render top 2 cards (stack effect)
  for (let i = Math.min(_tinderIdx + 1, _tinderCards.length - 1); i >= _tinderIdx; i--) {
    const card = _tinderCards[i];
    const isTop = (i === _tinderIdx);
    const offset = (i - _tinderIdx) * 8;
    const el = document.createElement('div');
    el.className = 'proj-tinder-card';
    el.style.cssText = `position:absolute;inset:0;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 4px 20px rgba(0,0,0,0.15);transform:scale(${isTop?1:0.95}) translateY(${offset}px);transition:transform .3s;z-index:${isTop?2:1}`;
    // Card image
    const imgBg = card.cover || card.img || '';
    const imgStyle = imgBg ? `background-image:url(${imgBg});background-size:cover;background-position:center` : `background:linear-gradient(135deg,#667eea,#764ba2)`;
    el.innerHTML = `
      <div style="width:100%;height:55%;${imgStyle};position:relative;display:flex;align-items:flex-end;padding:16px">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,transparent 40%,rgba(0,0,0,0.6))"></div>
        <div style="position:relative;z-index:1">
          <div style="font-size:10px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:rgba(255,255,255,0.8);margin-bottom:4px">${card.genre||'Game'}</div>
          <div style="font-size:20px;font-weight:800;color:#fff;line-height:1.2">${card.title||'Untitled'}</div>
        </div>
      </div>
      <div style="padding:16px 20px;flex:1">
        <div style="font-size:13px;color:#555;line-height:1.5;margin-bottom:12px">${card.desc||card.description||'No description available.'}</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          ${(card.tags||[card.platform||'PC']).map(t=>`<span style="padding:3px 10px;border-radius:20px;background:#f3f4f6;font-size:11px;font-weight:600;color:#374151">${t}</span>`).join('')}
        </div>
        <div style="margin-top:12px;display:flex;align-items:center;gap:8px">
          <div style="width:28px;height:28px;border-radius:50%;background:var(--orange);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff">${(card.studio||card.company||'?').charAt(0)}</div>
          <div style="font-size:12px;color:#666">${card.studio||card.company||'Independent'}</div>
        </div>
      </div>
    `;
    if (isTop) {
      // Touch events for swipe
      el.addEventListener('touchstart', _tinderTouchStart, {passive:true});
      el.addEventListener('touchend', _tinderTouchEnd, {passive:true});
    }
    stack.appendChild(el);
  }
  if (counter) counter.textContent = `${_tinderIdx + 1} / ${_tinderCards.length}`;
}

function _tinderTouchStart(e) {
  _tinderTouchStartX = e.touches[0].clientX;
  _tinderTouchStartY = e.touches[0].clientY;
}

function _tinderTouchEnd(e) {
  const dx = e.changedTouches[0].clientX - _tinderTouchStartX;
  const dy = e.changedTouches[0].clientY - _tinderTouchStartY;
  const absDx = Math.abs(dx);
  const absDy = Math.abs(dy);
  if (absDx > 60 && absDx > absDy) {
    projTinderSwipe(dx > 0 ? 'right' : 'left');
  } else if (absDy > 60 && absDy > absDx && dy < 0) {
    projTinderSwipe('up');
  }
}

function projTinderSwipe(dir) {
  const stack = document.getElementById('proj-tinder-stack');
  const topCard = stack ? stack.querySelector('.proj-tinder-card:last-child') : null;
  if (!topCard) return;
  // Animate
  const tx = dir === 'left' ? '-120%' : dir === 'right' ? '120%' : '0';
  const ty = dir === 'up' ? '-120%' : '0';
  const rot = dir === 'left' ? '-20deg' : dir === 'right' ? '20deg' : '0';
  topCard.style.transition = 'transform .35s ease-in, opacity .35s';
  topCard.style.transform = `translate(${tx}, ${ty}) rotate(${rot})`;
  topCard.style.opacity = '0';
  if (dir === 'right') {
    // Save to favorites
    const card = _tinderCards[_tinderIdx];
    if (card && card.id) {
      const saved = JSON.parse(localStorage.getItem('gc_saved_projects') || '[]');
      if (!saved.includes(card.id)) { saved.push(card.id); localStorage.setItem('gc_saved_projects', JSON.stringify(saved)); }
    }
  } else if (dir === 'up') {
    // Open detail
    const card = _tinderCards[_tinderIdx];
    if (card && card.id) pcProjOpenDetail && pcProjOpenDetail(card);
  }
  setTimeout(() => {
    _tinderIdx++;
    projTinderRender();
  }, 350);
}

// Hook into pcProjRender to also init tinder mode
const _origPcProjRender = typeof pcProjRender === 'function' ? pcProjRender : null;
"""

# Find a good insertion point - before the closing </script> tag near the end
# or after the pcProjSetGenre function
target3 = 'function toggleRwdDrawer() {'
if target3 in html:
    html = html.replace(target3, TINDER_JS + '\nfunction toggleRwdDrawer() {', 1)
    print('PATCH 3 OK: Tinder JS added')
else:
    print('PATCH 3 FAILED: target not found')

# ─── PATCH 4: Hook Tinder init into pcProjRender ─────────────────────────────
# Find pcProjRender function and add tinder init call at the end
OLD4 = 'function pcProjRender('
p4_ok = OLD4 in html
if p4_ok:
    # Find the function and add tinder init after grid population
    # We look for the end of pcProjRender by finding the next function declaration
    idx = html.index(OLD4)
    # Find where the function body ends (look for the next top-level function)
    # Simple approach: find "  grid.innerHTML = '';" pattern and add tinder init after grid fill
    HOOK_TARGET = 'grid.innerHTML = filtered.map(p => pcProjCardHTML(p)).join(\'\');\n'
    HOOK_NEW = 'grid.innerHTML = filtered.map(p => pcProjCardHTML(p)).join(\'\');\n    // Init tinder mode with same data\n    if (typeof projTinderInit === \'function\') projTinderInit(filtered);\n'
    if HOOK_TARGET in html:
        html = html.replace(HOOK_TARGET, HOOK_NEW, 1)
        print('PATCH 4 OK: Tinder init hooked into pcProjRender')
    else:
        print('PATCH 4 FAILED: grid.innerHTML target not found')
else:
    print('PATCH 4 SKIPPED: pcProjRender not found')

# ─── Save ─────────────────────────────────────────────────────────────────────
with open('index.html', 'w') as f:
    f.write(html)

new_len = len(html)
print(f'\nOriginal: {original_len} chars')
print(f'New:      {new_len} chars')
print(f'Delta:    +{new_len - original_len}')
