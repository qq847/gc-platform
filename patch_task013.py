#!/usr/bin/env python3
"""
Task-013: Profile 页面深度重设计
1. Settings 独立成页（新建 settings-panel）
2. Profile 右侧栏重构（只保留 Stats + Connect/Message + AI Match + People）
3. Hero 区域添加 ⚙️ Settings 入口
4. 角色差异化模块（Developer/Publisher/Organizer 显示不同内容）
5. 导航栏头像下拉菜单添加 Settings 入口
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 1: Profile Hero 区域 - 添加 ⚙️ Settings 按钮（替换 Sign Out 按钮旁边）
# ─────────────────────────────────────────────────────────────────────────────
OLD_HERO_BUTTONS = '''          <!-- Action buttons -->
          <div style="display:flex;gap:8px;padding-bottom:4px;flex-shrink:0">
            <button onclick="redoMatching()" style="padding:8px 18px;border-radius:20px;background:var(--orange);color:#fff;border:none;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:5px">&#8634; Redo Matching</button>
            <button onclick="signOutUser()" style="padding:8px 18px;border-radius:20px;background:#fff;color:#555;border:1.5px solid #ddd;font-size:12px;font-weight:600;cursor:pointer">Sign Out</button>
          </div>'''

NEW_HERO_BUTTONS = '''          <!-- Action buttons -->
          <div style="display:flex;gap:8px;padding-bottom:4px;flex-shrink:0;align-items:center">
            <button onclick="redoMatching()" style="padding:8px 18px;border-radius:20px;background:var(--orange);color:#fff;border:none;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:5px">&#8634; Redo Matching</button>
            <button onclick="signOutUser()" style="padding:8px 18px;border-radius:20px;background:#fff;color:#555;border:1.5px solid #ddd;font-size:12px;font-weight:600;cursor:pointer">Sign Out</button>
            <button onclick="switchMode(\'settings\')" title="Settings" style="width:34px;height:34px;border-radius:50%;background:#fff;color:#666;border:1.5px solid #ddd;font-size:16px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s" onmouseover="this.style.background=\'#f5f5f5\';this.style.color=\'#333\'" onmouseout="this.style.background=\'#fff\';this.style.color=\'#666\'">&#9881;</button>
          </div>'''

if OLD_HERO_BUTTONS in html:
    html = html.replace(OLD_HERO_BUTTONS, NEW_HERO_BUTTONS, 1)
    print("✅ PATCH 1: Hero Settings button added")
else:
    print("❌ PATCH 1 FAILED: Hero buttons not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 2: Profile 右侧栏重构
# 移除：Account, Notifications, Privacy, Quick Links, Danger Zone
# 保留：Stats, AI Match (移到右侧), Connect/Message buttons, People You May Know
# ─────────────────────────────────────────────────────────────────────────────
OLD_RIGHT_COL_START = '      <!-- RIGHT COLUMN: Stats + Settings + People -->'
OLD_RIGHT_COL_END = '      </div><!-- /right column -->'

# Find the right column block
start_idx = html.find(OLD_RIGHT_COL_START)
end_idx = html.find(OLD_RIGHT_COL_END)

if start_idx != -1 and end_idx != -1:
    end_idx += len(OLD_RIGHT_COL_END)
    
    NEW_RIGHT_COL = '''      <!-- RIGHT COLUMN: Stats + AI Match + Actions + People -->
      <div style="display:flex;flex-direction:column;gap:16px">
        <!-- Profile Stats card -->
        <div style="background:#fff;border-radius:12px;border:1px solid #e0ddd8;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr">
            <div style="text-align:center;padding:16px 8px;border-right:1px solid #e0ddd8">
              <div id="pp-stat-games" style="font-size:20px;font-weight:900;color:var(--text1)">&#8212;</div>
              <div style="font-size:9px;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Games</div>
            </div>
            <div style="text-align:center;padding:16px 8px;border-right:1px solid #e0ddd8">
              <div id="pp-stat-connections" style="font-size:20px;font-weight:900;color:var(--text1)">&#8212;</div>
              <div style="font-size:9px;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Connections</div>
            </div>
            <div style="text-align:center;padding:16px 8px">
              <div id="pp-stat-events" style="font-size:20px;font-weight:900;color:var(--text1)">&#8212;</div>
              <div style="font-size:9px;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Events</div>
            </div>
          </div>
        </div>
        <!-- Connect / Message actions -->
        <div id="pp-actions-card" style="background:#fff;border-radius:12px;padding:16px 18px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;flex-direction:column;gap:8px">
            <button style="width:100%;padding:10px;border-radius:10px;background:var(--orange);color:#fff;border:none;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px" onclick="switchMode(\'messages\')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              Message
            </button>
            <button style="width:100%;padding:10px;border-radius:10px;background:#fff;color:var(--text1);border:1.5px solid #ddd;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
              Connect
            </button>
            <button onclick="switchMode(\'settings\')" style="width:100%;padding:9px;border-radius:10px;background:#f8f7f5;color:var(--text2);border:1px solid #e0ddd8;font-size:12px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
              Account Settings
            </button>
          </div>
        </div>
        <!-- AI Match Results (right sidebar version) -->
        <div id="pp-match-card-sidebar" style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
            <div style="font-size:13px;font-weight:800;color:var(--text1)">&#10022; AI Match Results</div>
            <span style="font-size:9px;font-weight:700;padding:2px 7px;border-radius:8px;background:rgba(232,100,10,0.1);color:#e8640a">Powered by AI</span>
          </div>
          <div id="pp-match-stats-sidebar" style="display:flex;flex-direction:column;gap:8px"></div>
        </div>
        <!-- People You May Know -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:14px">People You May Know</div>
          <div id="pp-people-list" style="display:flex;flex-direction:column;gap:10px"></div>
        </div>
      </div><!-- /right column -->'''
    
    html = html[:start_idx] + NEW_RIGHT_COL + html[end_idx:]
    print("✅ PATCH 2: Right column restructured (Settings removed, Connect/Message added)")
else:
    print(f"❌ PATCH 2 FAILED: Right column not found (start={start_idx}, end={end_idx})")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 3: Profile 左侧主内容区 - 移除 AI Match 卡片（移到右侧栏）
# 添加 Publisher 的 Investment Focus 模块 和 Organizer 的 Events Organized 模块
# ─────────────────────────────────────────────────────────────────────────────
OLD_AI_MATCH_SECTION = '''        <!-- AI Match Results -->
        <div id="pp-match-card" style="display:none;background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
            <div style="font-size:16px;font-weight:800;color:var(--text1)">&#10022; AI Match Results</div>
            <span style="font-size:10px;font-weight:700;padding:3px 9px;border-radius:10px;background:rgba(232,100,10,0.1);color:#e8640a">Powered by AI</span>
          </div>
          <div id="pp-match-stats" style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px"></div>
        </div>'''

NEW_AI_MATCH_SECTION = '''        <!-- Publisher: Investment Focus (role-specific, shown via JS) -->
        <div id="pp-investment-section" style="display:none;background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:14px">Investment Focus</div>
          <div id="pp-investment-list" style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;gap:12px;padding:12px;border-radius:10px;background:#fdf8f5;border:1px solid #f0e8e0">
              <div style="width:36px;height:36px;border-radius:8px;background:linear-gradient(135deg,#92400e,#d97706);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0">🎮</div>
              <div><div style="font-size:13px;font-weight:700;color:var(--text1)">Indie Games</div><div style="font-size:11px;color:var(--text2);margin-top:1px">Action, RPG, Puzzle · PC &amp; Mobile</div></div>
            </div>
            <div style="display:flex;align-items:center;gap:12px;padding:12px;border-radius:10px;background:#fdf8f5;border:1px solid #f0e8e0">
              <div style="width:36px;height:36px;border-radius:8px;background:linear-gradient(135deg,#1e3a5f,#2563eb);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0">🌍</div>
              <div><div style="font-size:13px;font-weight:700;color:var(--text1)">Global Markets</div><div style="font-size:11px;color:var(--text2);margin-top:1px">Asia Pacific, Europe, North America</div></div>
            </div>
          </div>
        </div>
        <!-- Organizer: Events Organized (role-specific, shown via JS) -->
        <div id="pp-events-organized-section" style="display:none;background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
            <div style="font-size:16px;font-weight:800;color:var(--text1)">Events Organized</div>
            <span id="pp-events-org-count" style="font-size:11px;color:var(--text3)"></span>
          </div>
          <div id="pp-events-org-list" style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;gap:14px;padding:12px;border-radius:10px;background:#fdf8f5;border:1px solid #f0e8e0">
              <div style="width:44px;height:44px;border-radius:8px;background:linear-gradient(135deg,#e8640a,#f59e0b);display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:800;color:#fff;text-align:center;line-height:1.2;flex-shrink:0">GDC<br>2026</div>
              <div style="flex:1"><div style="font-size:13px;font-weight:700;color:var(--text1)">Game Developers Conference 2026</div><div style="font-size:11px;color:var(--text2);margin-top:1px">San Francisco · March 2026 · 28,000+ attendees</div></div>
              <span style="font-size:10px;font-weight:700;padding:3px 8px;border-radius:8px;background:#dcfce7;color:#16a34a;flex-shrink:0">Live</span>
            </div>
          </div>
        </div>'''

if OLD_AI_MATCH_SECTION in html:
    html = html.replace(OLD_AI_MATCH_SECTION, NEW_AI_MATCH_SECTION, 1)
    print("✅ PATCH 3: AI Match moved to sidebar, role-specific modules added")
else:
    print("❌ PATCH 3 FAILED: AI Match section not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 4: 在 profile-panel 结束标签之前插入 settings-panel
# ─────────────────────────────────────────────────────────────────────────────
SETTINGS_PANEL = '''</div><!-- /profile-panel -->

<!-- ══════════════════════════════════════════════════════════════════════════
     SETTINGS PANEL (独立页面，从 Profile 分离)
     ══════════════════════════════════════════════════════════════════════════ -->
<div id="settings-panel" style="display:none;position:fixed;inset:48px 0 0 0;background:#f4f2ef;z-index:200;overflow-y:auto">
  <div style="max-width:680px;margin:0 auto;padding:32px 24px 60px">
    <!-- Header -->
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:28px">
      <button onclick="switchMode(\'profile\')" style="width:36px;height:36px;border-radius:50%;background:#fff;border:1.5px solid #ddd;color:#555;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0" title="Back to Profile">&#8592;</button>
      <div>
        <div style="font-size:22px;font-weight:900;color:var(--text1)">Account Settings</div>
        <div style="font-size:13px;color:var(--text2);margin-top:2px">Manage your account, notifications and privacy</div>
      </div>
    </div>

    <!-- Account -->
    <div style="background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04);margin-bottom:16px">
      <div style="font-size:15px;font-weight:800;color:var(--text1);margin-bottom:18px;display:flex;align-items:center;gap:8px">
        <span style="width:28px;height:28px;border-radius:7px;background:#fdf0ea;display:flex;align-items:center;justify-content:center;font-size:14px">📧</span>
        Account
      </div>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div style="flex:1;min-width:0">
            <div style="font-size:12px;font-weight:700;color:var(--text1)">Email Address</div>
            <div id="st-email" style="font-size:12px;color:var(--text2);margin-top:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">&#8212;</div>
          </div>
          <button style="padding:6px 14px;border-radius:8px;background:#fff;border:1.5px solid #ddd;font-size:11px;font-weight:600;color:#555;cursor:pointer">Change</button>
        </div>
        <div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div style="flex:1;min-width:0">
            <div style="font-size:12px;font-weight:700;color:var(--text1)">Google Account</div>
            <div style="font-size:12px;color:#188038;margin-top:2px">Connected ✓</div>
          </div>
          <button style="padding:6px 14px;border-radius:8px;background:#fff;border:1.5px solid #ddd;font-size:11px;font-weight:600;color:#555;cursor:pointer">Disconnect</button>
        </div>
        <div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div style="flex:1;min-width:0">
            <div style="font-size:12px;font-weight:700;color:var(--text1)">Password</div>
            <div style="font-size:12px;color:var(--text2);margin-top:2px">Set via Google OAuth</div>
          </div>
          <button style="padding:6px 14px;border-radius:8px;background:#fff;border:1.5px solid #ddd;font-size:11px;font-weight:600;color:#555;cursor:pointer">Reset</button>
        </div>
      </div>
    </div>

    <!-- Notifications -->
    <div style="background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04);margin-bottom:16px">
      <div style="font-size:15px;font-weight:800;color:var(--text1);margin-bottom:18px;display:flex;align-items:center;gap:8px">
        <span style="width:28px;height:28px;border-radius:7px;background:#fdf0ea;display:flex;align-items:center;justify-content:center;font-size:14px">🔔</span>
        Notifications
      </div>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Event Reminders</div><div style="font-size:11px;color:var(--text2);margin-top:2px">Get notified before events start</div></div>
          <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">New Matches</div><div style="font-size:11px;color:var(--text2);margin-top:2px">AI found new connections for you</div></div>
          <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Messages</div><div style="font-size:11px;color:var(--text2);margin-top:2px">New message notifications</div></div>
          <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Weekly Digest</div><div style="font-size:11px;color:var(--text2);margin-top:2px">Industry news every Monday</div></div>
          <div class="pp-toggle" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
      </div>
    </div>

    <!-- Privacy -->
    <div style="background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04);margin-bottom:16px">
      <div style="font-size:15px;font-weight:800;color:var(--text1);margin-bottom:18px;display:flex;align-items:center;gap:8px">
        <span style="width:28px;height:28px;border-radius:7px;background:#fdf0ea;display:flex;align-items:center;justify-content:center;font-size:14px">🔒</span>
        Privacy
      </div>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Profile Visibility</div><div style="font-size:11px;color:var(--text2);margin-top:2px">Visible to all members</div></div>
          <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Show in AI Matching</div><div style="font-size:11px;color:var(--text2);margin-top:2px">Let AI suggest you to others</div></div>
          <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:10px;background:#fafaf8;border:1px solid #eee">
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Contact Info Visible</div><div style="font-size:11px;color:var(--text2);margin-top:2px">Show email to connections</div></div>
          <div class="pp-toggle" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
        </div>
      </div>
    </div>

    <!-- Quick Links -->
    <div style="background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04);margin-bottom:16px">
      <div style="font-size:15px;font-weight:800;color:var(--text1);margin-bottom:18px;display:flex;align-items:center;gap:8px">
        <span style="width:28px;height:28px;border-radius:7px;background:#fdf0ea;display:flex;align-items:center;justify-content:center;font-size:14px">&#128279;</span>
        Quick Links
      </div>
      <!-- Admin entry: shown via JS for admin accounts only -->
      <div id="st-admin-entry" style="display:none;margin-bottom:10px">
        <a href="_admin.html" target="_blank" style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;border:1.5px solid rgba(229,57,53,0.3);background:rgba(229,57,53,0.04);text-decoration:none;transition:background .12s" onmouseover="this.style.background=\'rgba(229,57,53,0.09)\'" onmouseout="this.style.background=\'rgba(229,57,53,0.04)\'">
          <div style="width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#b71c1c,#e53935);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0">&#9881;&#65039;</div>
          <div><div style="font-size:12px;font-weight:700;color:#e53935">Admin Dashboard</div><div style="font-size:11px;color:var(--text2)">Super admin control panel</div></div>
          <div style="margin-left:auto;font-size:12px;color:#e53935">&#8599;</div>
        </a>
      </div>
      <div style="display:flex;flex-direction:column;gap:8px">
        <a href="DealFlow_v1_PC.html" style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;border:1px solid #e4e6ea;text-decoration:none;transition:background .12s;background:#fff" onmouseover="this.style.background=\'#f7f8fa\'" onmouseout="this.style.background=\'#fff\'">
          <div style="width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#312e81,#4f46e5);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0">&#129309;</div>
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Deal Room</div><div style="font-size:11px;color:var(--text2)">Publisher &amp; investor pipeline</div></div>
          <div style="margin-left:auto;font-size:12px;color:var(--text3)">&#8599;</div>
        </a>
        <a href="EventHQ_Dashboard_v1_PC.html" style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:10px;border:1px solid #e4e6ea;text-decoration:none;transition:background .12s;background:#fff" onmouseover="this.style.background=\'#f7f8fa\'" onmouseout="this.style.background=\'#fff\'">
          <div style="width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#1c1a17,#2a2520);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0">&#9889;</div>
          <div><div style="font-size:12px;font-weight:700;color:var(--text1)">Event HQ</div><div style="font-size:11px;color:var(--text2)">Organizer dashboard</div></div>
          <div style="margin-left:auto;font-size:12px;color:var(--text3)">&#8599;</div>
        </a>
      </div>
    </div>

    <!-- Danger Zone -->
    <div style="background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #fecaca;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
      <div style="font-size:13px;font-weight:700;letter-spacing:1px;color:#dc2626;text-transform:uppercase;margin-bottom:16px">&#9888; Danger Zone</div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <button onclick="signOutUser()" style="width:100%;padding:11px;border-radius:10px;border:1.5px solid #dc2626;background:#fff;color:#dc2626;font-size:13px;font-weight:700;cursor:pointer;text-align:left;display:flex;align-items:center;gap:8px">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
          Sign Out of All Devices
        </button>
        <button style="width:100%;padding:11px;border-radius:10px;border:1.5px solid #ddd;background:#fff;color:#666;font-size:13px;font-weight:600;cursor:pointer;text-align:left;display:flex;align-items:center;gap:8px">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>
          Delete Account
        </button>
      </div>
    </div>
  </div>
</div><!-- /settings-panel -->'''

OLD_PROFILE_END = '</div><!-- /profile-panel -->'
if OLD_PROFILE_END in html:
    html = html.replace(OLD_PROFILE_END, SETTINGS_PANEL, 1)
    print("✅ PATCH 4: settings-panel created")
else:
    print("❌ PATCH 4 FAILED: profile-panel end not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 5: switchMode 函数 - 添加 settings 模式处理
# ─────────────────────────────────────────────────────────────────────────────
OLD_SWITCH_PANELS = '''  const projectsPanel = document.getElementById('projects-panel');
  const companiesPanel = document.getElementById('companies-panel');
  const newsPanel = document.getElementById('news-panel');
  const profilePanel = document.getElementById('profile-panel');
  // Hide all full-screen panels by default
  projectsPanel.style.display = 'none';
  companiesPanel.style.display = 'none';
  if (newsPanel) newsPanel.style.display = 'none';
  profilePanel.style.display = 'none';'''

NEW_SWITCH_PANELS = '''  const projectsPanel = document.getElementById('projects-panel');
  const companiesPanel = document.getElementById('companies-panel');
  const newsPanel = document.getElementById('news-panel');
  const profilePanel = document.getElementById('profile-panel');
  const settingsPanel = document.getElementById('settings-panel');
  // Hide all full-screen panels by default
  projectsPanel.style.display = 'none';
  companiesPanel.style.display = 'none';
  if (newsPanel) newsPanel.style.display = 'none';
  profilePanel.style.display = 'none';
  if (settingsPanel) settingsPanel.style.display = 'none';'''

if OLD_SWITCH_PANELS in html:
    html = html.replace(OLD_SWITCH_PANELS, NEW_SWITCH_PANELS, 1)
    print("✅ PATCH 5a: switchMode - settings panel hide added")
else:
    print("❌ PATCH 5a FAILED")

# Add settings mode handler after profile mode handler
OLD_SETTINGS_PLACEHOLDER = '''  } else {
    homePanel.style.display = 'none';
    confBar.style.display = 'flex';
    layout.style.display = 'grid';'''

NEW_SETTINGS_HANDLER = '''  } else if (mode === 'settings') {
    homePanel.style.display = 'none';
    confBar.style.display = 'none';
    layout.style.display = 'none';
    if (layoutOuter) layoutOuter.style.display = 'none';
    if (settingsPanel) {
      settingsPanel.style.display = 'block';
      // Populate settings email
      const _stEmail = document.getElementById('st-email');
      const _stUser = gcGetUser();
      if (_stEmail && _stUser && _stUser.email) _stEmail.textContent = _stUser.email;
      else if (_stEmail) {
        try { const _d = JSON.parse(localStorage.getItem('gc_wizard')); if (_d && _d.profile && _d.profile.email) _stEmail.textContent = _d.profile.email; } catch(e){}
      }
      // Show admin entry for admin accounts
      const _stAdminEntry = document.getElementById('st-admin-entry');
      if (_stAdminEntry) {
        const _ADMIN = ['qq@connection-events.com'];
        _stAdminEntry.style.display = (_stUser && _stUser.email && _ADMIN.includes(_stUser.email.toLowerCase())) ? 'block' : 'none';
      }
    }
    document.title = '⚙️ Settings | Game Connection';
    history.replaceState(null, '', '#settings');
  } else {
    homePanel.style.display = 'none';
    confBar.style.display = 'flex';
    layout.style.display = 'grid';'''

if OLD_SETTINGS_PLACEHOLDER in html:
    html = html.replace(OLD_SETTINGS_PLACEHOLDER, NEW_SETTINGS_HANDLER, 1)
    print("✅ PATCH 5b: switchMode settings handler added")
else:
    print("❌ PATCH 5b FAILED")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 6: populateProfilePanel - 更新 AI Match 到右侧栏 + 角色差异化模块
# ─────────────────────────────────────────────────────────────────────────────
OLD_MATCH_STATS_JS = '''  // ── AI Match Stats ──
  const matchCard = document.getElementById('pp-match-card');
  const matchStats = document.getElementById('pp-match-stats');
  if(matchCard && matchStats && stats.length > 0){
    matchCard.style.display = 'block';
    matchStats.innerHTML = '';
    stats.forEach(s => {
      const col = document.createElement('div');
      col.style.cssText = 'text-align:center;padding:12px 8px;background:rgba(232,100,10,0.06);border-radius:10px;border:1px solid rgba(232,100,10,0.15)';
      col.innerHTML = '<div style="font-size:22px;font-weight:900;color:#e8640a">'+s.num+'</div><div style="font-size:10px;color:var(--text2);margin-top:3px;line-height:1.3">'+s.label+'</div>';
      matchStats.appendChild(col);
    });
  }'''

NEW_MATCH_STATS_JS = '''  // ── AI Match Stats (right sidebar) ──
  const matchStatsSidebar = document.getElementById('pp-match-stats-sidebar');
  if(matchStatsSidebar){
    matchStatsSidebar.innerHTML = '';
    if(stats.length > 0){
      stats.forEach(s => {
        const row = document.createElement('div');
        row.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:8px 12px;background:rgba(232,100,10,0.05);border-radius:9px;border:1px solid rgba(232,100,10,0.12)';
        row.innerHTML = '<div style="font-size:11px;color:var(--text2)">'+s.label+'</div><div style="font-size:18px;font-weight:900;color:#e8640a">'+s.num+'</div>';
        matchStatsSidebar.appendChild(row);
      });
    } else {
      matchStatsSidebar.innerHTML = '<div style="font-size:12px;color:var(--text3);font-style:italic;text-align:center;padding:8px">Complete onboarding to see matches</div>';
    }
  }
  // ── Role-specific modules ──
  const roleKey = _detectRole(roles);
  const investSection = document.getElementById('pp-investment-section');
  const eventsOrgSection = document.getElementById('pp-events-organized-section');
  const gamesSection = document.getElementById('pp-games-section');
  if(investSection) investSection.style.display = (roleKey === 'publisher') ? 'block' : 'none';
  if(eventsOrgSection) eventsOrgSection.style.display = (roleKey === 'organizer') ? 'block' : 'none';
  if(gamesSection) gamesSection.style.display = (roleKey === 'investor' || roleKey === 'media') ? 'none' : 'block';'''

if OLD_MATCH_STATS_JS in html:
    html = html.replace(OLD_MATCH_STATS_JS, NEW_MATCH_STATS_JS, 1)
    print("✅ PATCH 6: AI Match moved to sidebar, role-specific modules JS added")
else:
    print("❌ PATCH 6 FAILED: AI Match JS not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 7: profile-drawer 添加 Settings 入口（导航栏头像下拉菜单）
# ─────────────────────────────────────────────────────────────────────────────
OLD_DRAWER_SIGNOUT = '''    <button class="pd-signout-btn" onclick="signOutUser()">Sign Out</button>'''
NEW_DRAWER_SIGNOUT = '''    <button onclick="closeProfileDrawer();switchMode(\'settings\')" style="width:100%;padding:10px 16px;border-radius:10px;border:1px solid #e0ddd8;background:#fff;color:var(--text1);font-size:13px;font-weight:600;cursor:pointer;text-align:left;display:flex;align-items:center;gap:8px;margin-bottom:8px">&#9881; Account Settings</button>
    <button class="pd-signout-btn" onclick="signOutUser()">Sign Out</button>'''

if OLD_DRAWER_SIGNOUT in html:
    html = html.replace(OLD_DRAWER_SIGNOUT, NEW_DRAWER_SIGNOUT, 1)
    print("✅ PATCH 7: Settings entry added to profile-drawer")
else:
    print("❌ PATCH 7 FAILED: pd-signout-btn not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 8: _titleMap 添加 settings
# ─────────────────────────────────────────────────────────────────────────────
OLD_TITLE_MAP = "const _titleMap = {calendar:'📅 Calendar',news:'📰 News',projects:'🎮 Projects',profile:'👤 Profile',companies:'🏢 Companies',messages:'💬 Messages'};"
NEW_TITLE_MAP = "const _titleMap = {calendar:'📅 Calendar',news:'📰 News',projects:'🎮 Projects',profile:'👤 Profile',companies:'🏢 Companies',messages:'💬 Messages',settings:'⚙️ Settings'};"

if OLD_TITLE_MAP in html:
    html = html.replace(OLD_TITLE_MAP, NEW_TITLE_MAP, 1)
    print("✅ PATCH 8: _titleMap updated with settings")
else:
    print("❌ PATCH 8 FAILED: _titleMap not found")

# ─────────────────────────────────────────────────────────────────────────────
# PATCH 9: URL hash 处理 - 支持 #settings
# ─────────────────────────────────────────────────────────────────────────────
OLD_HASH_HANDLER = "const _initMode = ['calendar','news','projects','profile','companies','messages','home'].includes(window.location.hash.slice(1)) ? window.location.hash.slice(1) : 'calendar';"
NEW_HASH_HANDLER = "const _initMode = ['calendar','news','projects','profile','companies','messages','home','settings'].includes(window.location.hash.slice(1)) ? window.location.hash.slice(1) : 'calendar';"

if OLD_HASH_HANDLER in html:
    html = html.replace(OLD_HASH_HANDLER, NEW_HASH_HANDLER, 1)
    print("✅ PATCH 9: URL hash handler updated")
else:
    print("⚠️  PATCH 9 SKIPPED: hash handler not found (may not exist)")

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ All patches applied. index.html updated.")
