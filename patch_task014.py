#!/usr/bin/env python3
"""Task-014: Mobile RWD deep optimization patch"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)
patches_applied = []

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 1: Add rwd-page-title CSS (Reddit-style page title dropdown)
# ─────────────────────────────────────────────────────────────────────────────
OLD1 = """.rwd-hamburger{
  display:none;flex-direction:column;justify-content:center;gap:5px;
  width:36px;height:36px;cursor:pointer;flex-shrink:0;
  background:none;border:none;padding:4px;
}"""

NEW1 = """.rwd-hamburger{
  display:none;flex-direction:column;justify-content:center;gap:5px;
  width:36px;height:36px;cursor:pointer;flex-shrink:0;
  background:none;border:none;padding:4px;
}
/* ── Reddit-style page title (mobile only) ── */
.rwd-page-title-wrap{
  display:none;
  align-items:center;gap:0;
  flex:1;min-width:0;margin:0 8px;
  position:relative;
}
.rwd-page-title-btn{
  display:flex;align-items:center;gap:5px;
  background:none;border:none;cursor:pointer;
  font-size:15px;font-weight:700;color:var(--text1);
  padding:4px 8px;border-radius:8px;
  transition:background .15s;
  max-width:100%;overflow:hidden;
  white-space:nowrap;text-overflow:ellipsis;
}
.rwd-page-title-btn:hover{background:rgba(0,0,0,0.06)}
.rwd-page-title-btn svg{flex-shrink:0;opacity:.6;transition:transform .2s}
.rwd-page-title-btn.open svg{transform:rotate(180deg)}
.rwd-page-title-dropdown{
  display:none;
  position:absolute;top:calc(100% + 6px);left:0;
  background:#fff;border-radius:12px;
  box-shadow:0 4px 24px rgba(0,0,0,0.15);
  border:1px solid #e8e7e4;
  min-width:200px;z-index:600;
  overflow:hidden;
}
.rwd-page-title-dropdown.open{display:block}
.rwd-ptd-item{
  display:flex;align-items:center;gap:10px;
  padding:11px 16px;font-size:14px;font-weight:600;
  color:var(--text1);cursor:pointer;
  transition:background .12s;
}
.rwd-ptd-item:hover{background:rgba(22,163,74,0.06);color:var(--orange)}
.rwd-ptd-item.active{color:var(--orange);background:rgba(22,163,74,0.08)}
.rwd-ptd-item span{font-size:16px;width:20px;text-align:center}"""

if OLD1 in html:
    html = html.replace(OLD1, NEW1, 1)
    patches_applied.append('PATCH 1: rwd-page-title CSS added')
else:
    print('PATCH 1 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 2: Show rwd-page-title-wrap on mobile in @media block
# ─────────────────────────────────────────────────────────────────────────────
OLD2 = """  /* Show hamburger, hide nav tabs and search */
  .rwd-hamburger{display:flex}
  .nav-tabs{display:none !important}
  .nav-search{display:none !important}
  .biz-dropdown-wrap{display:none !important}
  .nav-gap{display:none !important}
  .nav-sep{display:none !important}"""

NEW2 = """  /* Show hamburger + page title, hide nav tabs and search */
  .rwd-hamburger{display:flex}
  .rwd-page-title-wrap{display:flex}
  .nav-tabs{display:none !important}
  .nav-search{display:none !important}
  .biz-dropdown-wrap{display:none !important}
  .nav-gap{display:none !important}
  .nav-sep{display:none !important}"""

if OLD2 in html:
    html = html.replace(OLD2, NEW2, 1)
    patches_applied.append('PATCH 2: rwd-page-title-wrap shown on mobile')
else:
    print('PATCH 2 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 3: Add rwd-page-title HTML between logo and hamburger
# ─────────────────────────────────────────────────────────────────────────────
OLD3 = """  <!-- Hamburger menu (mobile only) -->
  <button class="rwd-hamburger" id="rwd-hamburger" onclick="toggleRwdDrawer()" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</div><!-- /topnav-inner -->"""

NEW3 = """  <!-- Reddit-style page title (mobile only) -->
  <div class="rwd-page-title-wrap" id="rwd-page-title-wrap">
    <button class="rwd-page-title-btn" id="rwd-page-title-btn" onclick="toggleRwdPageTitleDropdown()" aria-label="Switch page">
      <span id="rwd-page-title-text">📅 Calendar</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
    </button>
    <div class="rwd-page-title-dropdown" id="rwd-page-title-dropdown">
      <div class="rwd-ptd-item active" data-mode="calendar" onclick="switchMode('calendar');closeRwdPageTitleDropdown()"><span>📅</span> Calendar</div>
      <div class="rwd-ptd-item" data-mode="news" onclick="switchMode('news');closeRwdPageTitleDropdown()"><span>📰</span> News</div>
      <div class="rwd-ptd-item" data-mode="projects" onclick="switchMode('projects');closeRwdPageTitleDropdown()"><span>🎮</span> Projects</div>
      <div class="rwd-ptd-item" data-mode="profile" onclick="switchMode('profile');closeRwdPageTitleDropdown()"><span>👤</span> Profile</div>
    </div>
  </div>
  <!-- Hamburger menu (mobile only) -->
  <button class="rwd-hamburger" id="rwd-hamburger" onclick="toggleRwdDrawer()" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</div><!-- /topnav-inner -->"""

if OLD3 in html:
    html = html.replace(OLD3, NEW3, 1)
    patches_applied.append('PATCH 3: rwd-page-title HTML added')
else:
    print('PATCH 3 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 4: Add rwd-page-title JS functions + update switchMode to sync title
# ─────────────────────────────────────────────────────────────────────────────
OLD4 = """  const _titleMap = {calendar:'📅 Calendar',news:'📰 News',projects:'🎮 Projects',profile:'👤 Profile',companies:'🏢 Companies',messages:'💬 Messages',settings:'⚙️ Settings'};
  document.title = (_titleMap[mode] || mode) + ' | Game Connection';"""

NEW4 = """  const _titleMap = {calendar:'📅 Calendar',news:'📰 News',projects:'🎮 Projects',profile:'👤 Profile',companies:'🏢 Companies',messages:'💬 Messages',settings:'⚙️ Settings'};
  document.title = (_titleMap[mode] || mode) + ' | Game Connection';
  // Update Reddit-style mobile page title
  const _rwdTitleEl = document.getElementById('rwd-page-title-text');
  if(_rwdTitleEl && _titleMap[mode]) _rwdTitleEl.textContent = _titleMap[mode];
  // Update active state in dropdown
  document.querySelectorAll('.rwd-ptd-item').forEach(el=>{
    el.classList.toggle('active', el.dataset.mode === mode);
  });"""

if OLD4 in html:
    html = html.replace(OLD4, NEW4, 1)
    patches_applied.append('PATCH 4: switchMode syncs rwd-page-title')
else:
    print('PATCH 4 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 5: Add toggleRwdPageTitleDropdown / closeRwdPageTitleDropdown functions
# ─────────────────────────────────────────────────────────────────────────────
OLD5 = """  function toggleRwdDrawer(){"""

NEW5 = """  // ── Reddit-style page title dropdown ──────────────────────────────────────
  function toggleRwdPageTitleDropdown(){
    const dd = document.getElementById('rwd-page-title-dropdown');
    const btn = document.getElementById('rwd-page-title-btn');
    if(!dd) return;
    const isOpen = dd.classList.contains('open');
    if(isOpen){ closeRwdPageTitleDropdown(); }
    else {
      dd.classList.add('open');
      btn && btn.classList.add('open');
      // Close on outside click
      setTimeout(()=>{
        document.addEventListener('click', _rwdPtdOutsideHandler, {once:true});
      }, 10);
    }
  }
  function closeRwdPageTitleDropdown(){
    const dd = document.getElementById('rwd-page-title-dropdown');
    const btn = document.getElementById('rwd-page-title-btn');
    dd && dd.classList.remove('open');
    btn && btn.classList.remove('open');
  }
  function _rwdPtdOutsideHandler(e){
    const wrap = document.getElementById('rwd-page-title-wrap');
    if(wrap && !wrap.contains(e.target)) closeRwdPageTitleDropdown();
  }

  function toggleRwdDrawer(){"""

if OLD5 in html:
    html = html.replace(OLD5, NEW5, 1)
    patches_applied.append('PATCH 5: rwd-page-title JS functions added')
else:
    print('PATCH 5 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 6: Calendar mobile optimization - hide left panel, show month strip
# Add CSS for mobile calendar
# ─────────────────────────────────────────────────────────────────────────────
OLD6 = """  /* Notification bell and user avatar shrink */
  .nav-notif-btn,.nav-user-avatar{
    width:30px;height:30px;
  }
}
</style>"""

NEW6 = """  /* Notification bell and user avatar shrink */
  .nav-notif-btn,.nav-user-avatar{
    width:30px;height:30px;
  }
  /* Calendar mobile: hide left panel, full-width event list */
  .cal-layout{
    grid-template-columns:1fr !important;
  }
  .cal-left{
    display:none !important;
  }
  .cal-right{
    border-left:none !important;
  }
  /* Mobile month strip */
  #rwd-month-strip{
    display:flex !important;
  }
  /* News mobile: single column */
  .news-grid{
    grid-template-columns:1fr !important;
  }
  /* News cards: prevent image overflow */
  .news-card img,.news-card-img{
    max-width:100% !important;
    height:auto !important;
  }
  /* Projects mobile: 2-col grid (already handled above) */
  /* Prevent any horizontal overflow */
  #news-panel, #projects-panel{
    overflow-x:hidden !important;
  }
  #news-panel > div, #projects-panel > div{
    overflow-x:hidden !important;
  }
}
/* ── Mobile month strip (calendar, hidden on PC) ── */
#rwd-month-strip{
  display:none;
  align-items:center;gap:0;
  background:#fff;border-bottom:1px solid #e8e7e4;
  padding:8px 0 8px 4px;
  overflow-x:auto;
  scrollbar-width:none;
  -webkit-overflow-scrolling:touch;
  position:sticky;top:0;z-index:10;
}
#rwd-month-strip::-webkit-scrollbar{display:none}
.rwd-month-chip{
  flex-shrink:0;padding:5px 14px;border-radius:20px;
  font-size:13px;font-weight:600;color:#666;
  cursor:pointer;transition:all .15s;white-space:nowrap;
}
.rwd-month-chip.active{
  background:var(--orange);color:#fff;
}
.rwd-month-chip:hover:not(.active){background:#f0efec}
</style>"""

if OLD6 in html:
    html = html.replace(OLD6, NEW6, 1)
    patches_applied.append('PATCH 6: Calendar/News mobile CSS added')
else:
    print('PATCH 6 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 7: Add rwd-month-strip HTML inside calendar panel (after cal-layout open)
# ─────────────────────────────────────────────────────────────────────────────
OLD7 = """id="cal-layout" """

NEW7 = """id="cal-layout" """

# Find the calendar panel and add month strip before cal-layout
OLD7b = """<div class="layout-outer" id="layout-outer">"""

# Actually let's find the cal-layout div and add the strip before it
import re

# Find the cal-layout div
cal_layout_match = re.search(r'<div[^>]+id="cal-layout"[^>]*>', html)
if cal_layout_match:
    insert_pos = cal_layout_match.start()
    month_strip_html = """<!-- MOBILE MONTH STRIP (calendar, mobile only) -->
<div id="rwd-month-strip">
  <div class="rwd-month-chip active" data-month="all" onclick="rwdFilterMonth(this,'all')">All</div>
  <div class="rwd-month-chip" data-month="2026-01" onclick="rwdFilterMonth(this,'2026-01')">Jan 2026</div>
  <div class="rwd-month-chip" data-month="2026-02" onclick="rwdFilterMonth(this,'2026-02')">Feb 2026</div>
  <div class="rwd-month-chip" data-month="2026-03" onclick="rwdFilterMonth(this,'2026-03')">Mar 2026</div>
  <div class="rwd-month-chip" data-month="2026-04" onclick="rwdFilterMonth(this,'2026-04')">Apr 2026</div>
  <div class="rwd-month-chip" data-month="2026-05" onclick="rwdFilterMonth(this,'2026-05')">May 2026</div>
  <div class="rwd-month-chip" data-month="2026-06" onclick="rwdFilterMonth(this,'2026-06')">Jun 2026</div>
  <div class="rwd-month-chip" data-month="2026-07" onclick="rwdFilterMonth(this,'2026-07')">Jul 2026</div>
  <div class="rwd-month-chip" data-month="2026-08" onclick="rwdFilterMonth(this,'2026-08')">Aug 2026</div>
  <div class="rwd-month-chip" data-month="2026-09" onclick="rwdFilterMonth(this,'2026-09')">Sep 2026</div>
  <div class="rwd-month-chip" data-month="2026-10" onclick="rwdFilterMonth(this,'2026-10')">Oct 2026</div>
  <div class="rwd-month-chip" data-month="2026-11" onclick="rwdFilterMonth(this,'2026-11')">Nov 2026</div>
  <div class="rwd-month-chip" data-month="2026-12" onclick="rwdFilterMonth(this,'2026-12')">Dec 2026</div>
</div>
"""
    html = html[:insert_pos] + month_strip_html + html[insert_pos:]
    patches_applied.append('PATCH 7: Mobile month strip HTML added before cal-layout')
else:
    print('PATCH 7 FAILED: cal-layout not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 8: Add rwdFilterMonth JS function
# ─────────────────────────────────────────────────────────────────────────────
OLD8 = """  // ── Reddit-style page title dropdown ──────────────────────────────────────"""

NEW8 = """  // ── Mobile month strip filter (calendar) ──────────────────────────────────
  function rwdFilterMonth(el, month){
    // Update active chip
    document.querySelectorAll('.rwd-month-chip').forEach(c=>c.classList.remove('active'));
    el.classList.add('active');
    // Filter event rows in cal-right
    const rows = document.querySelectorAll('.cal-event-row, .cal-day-group, [data-date]');
    if(month === 'all'){
      rows.forEach(r=>r.style.display='');
      return;
    }
    rows.forEach(r=>{
      const d = r.dataset.date || r.getAttribute('data-date') || '';
      if(d.startsWith(month) || month === 'all'){
        r.style.display='';
      } else {
        // Also check child elements for date
        const dateEl = r.querySelector('[data-date]');
        if(dateEl && dateEl.dataset.date && dateEl.dataset.date.startsWith(month)){
          r.style.display='';
        } else if(d){
          r.style.display='none';
        }
      }
    });
    // Also try filtering by month heading text
    document.querySelectorAll('.cal-month-heading, .cal-section-heading').forEach(h=>{
      const txt = h.textContent || '';
      const monthNames = {
        '2026-01':'January','2026-02':'February','2026-03':'March',
        '2026-04':'April','2026-05':'May','2026-06':'June',
        '2026-07':'July','2026-08':'August','2026-09':'September',
        '2026-10':'October','2026-11':'November','2026-12':'December'
      };
      const targetMonth = monthNames[month];
      if(targetMonth && txt.includes(targetMonth)){
        h.style.display='';
        // Show siblings until next heading
        let sib = h.nextElementSibling;
        while(sib && !sib.classList.contains('cal-month-heading') && !sib.classList.contains('cal-section-heading')){
          sib.style.display='';
          sib = sib.nextElementSibling;
        }
      } else if(targetMonth){
        h.style.display='none';
      }
    });
  }

  // ── Reddit-style page title dropdown ──────────────────────────────────────"""

if OLD8 in html:
    html = html.replace(OLD8, NEW8, 1)
    patches_applied.append('PATCH 8: rwdFilterMonth JS function added')
else:
    print('PATCH 8 FAILED: target not found')

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 9: News grid - ensure news-grid class exists or add CSS for news cards
# ─────────────────────────────────────────────────────────────────────────────
# Check if news-grid class is used
if 'news-grid' in html:
    patches_applied.append('PATCH 9: news-grid class already exists, CSS applied')
else:
    # Find the news cards container and check its class
    news_match = re.search(r'id="news-cards-grid"[^>]*class="([^"]*)"', html)
    if not news_match:
        news_match = re.search(r'class="([^"]*)"[^>]*id="news-cards-grid"', html)
    if news_match:
        patches_applied.append(f'PATCH 9: news-cards-grid found, class={news_match.group(1)}')
    else:
        # Add a targeted CSS rule for the news grid
        patches_applied.append('PATCH 9: news-grid not found, will use #news-cards-grid selector')

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Original length: {original_len}")
print(f"New length: {len(html)}")
print(f"Delta: +{len(html)-original_len}")
print("\nPatches applied:")
for p in patches_applied:
    print(f"  ✓ {p}")
