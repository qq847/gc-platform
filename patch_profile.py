#!/usr/bin/env python3
"""
Task-010: Profile 页面重设计
替换 index.html 中的 profile-panel HTML (lines 2337-2592)
和 populateProfilePanel JS 函数 (lines 3717-3828)
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. 替换 profile-panel HTML ──────────────────────────────────────────────
NEW_PROFILE_PANEL = '''<!-- PROFILE & SETTINGS PANEL -->
<div id="profile-panel" style="display:none;position:fixed;inset:48px 0 0 0;background:#f4f2ef;z-index:200;overflow-y:auto">
  <!-- Guest state -->
  <div id="pp-guest" style="display:none;flex-direction:column;align-items:center;justify-content:center;min-height:calc(100vh - 48px);text-align:center;padding:40px">
    <div style="width:80px;height:80px;border-radius:50%;background:#f0ede8;display:flex;align-items:center;justify-content:center;font-size:36px;margin-bottom:20px">?</div>
    <div style="font-size:22px;font-weight:800;color:var(--text1);margin-bottom:8px">Sign in to view your profile</div>
    <div style="font-size:14px;color:var(--text2);margin-bottom:28px">Connect with publishers, investors, and developers worldwide.</div>
    <button onclick="window.location.href=\'Identity_Login_v1.0_PC.html\'" style="padding:14px 36px;border-radius:30px;background:linear-gradient(135deg,#e8640a,#f59e0b);color:#fff;font-size:15px;font-weight:700;border:none;cursor:pointer">Sign In with Google &#8594;</button>
  </div>
  <!-- Logged-in state -->
  <div id="pp-loggedin" style="display:none">
    <!-- ── HERO COVER + AVATAR ── -->
    <div id="pp-hero" style="position:relative;background:#fff;border-bottom:1px solid #e0ddd8">
      <!-- Cover image -->
      <div id="pp-cover" style="height:200px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 40%,#0f3460 70%,#e94560 100%);position:relative;overflow:hidden">
        <!-- Subtle pattern overlay -->
        <div style="position:absolute;inset:0;background:url(\'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2260%22 height=%2260%22><circle cx=%2230%22 cy=%2230%22 r=%221%22 fill=%22rgba(255,255,255,0.08)%22/></svg>\') repeat;opacity:0.5"></div>
        <!-- Role-specific cover gradient applied by JS via id pp-cover -->
      </div>
      <!-- Avatar + info row -->
      <div style="max-width:900px;margin:0 auto;padding:0 32px">
        <div style="display:flex;align-items:flex-end;gap:20px;margin-top:-52px;padding-bottom:16px;position:relative">
          <!-- Avatar -->
          <div id="pp-avatar" style="width:104px;height:104px;border-radius:50%;background:linear-gradient(135deg,#e8640a,#f59e0b);display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;color:#fff;border:4px solid #fff;box-shadow:0 4px 16px rgba(0,0,0,0.18);flex-shrink:0;overflow:hidden;position:relative;z-index:2">?</div>
          <!-- Name + role + meta -->
          <div style="flex:1;min-width:0;padding-bottom:4px">
            <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
              <div id="pp-name" style="font-size:22px;font-weight:900;color:var(--text1);line-height:1.2">&#8212;</div>
              <span id="pp-role-badge" style="font-size:11px;font-weight:800;padding:3px 10px;border-radius:20px;background:#fdf0ea;color:#e8640a;letter-spacing:.3px">Member</span>
            </div>
            <div id="pp-role" style="font-size:13px;color:var(--text2);margin-top:3px">&#8212;</div>
            <div id="pp-meta" style="font-size:12px;color:var(--text3);margin-top:3px;display:flex;gap:12px;flex-wrap:wrap"></div>
          </div>
          <!-- Action buttons -->
          <div style="display:flex;gap:8px;padding-bottom:4px;flex-shrink:0">
            <button onclick="redoMatching()" style="padding:8px 18px;border-radius:20px;background:var(--orange);color:#fff;border:none;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:5px">&#8634; Redo Matching</button>
            <button onclick="signOutUser()" style="padding:8px 18px;border-radius:20px;background:#fff;color:#555;border:1.5px solid #ddd;font-size:12px;font-weight:600;cursor:pointer">Sign Out</button>
          </div>
        </div>
        <!-- Role tags row -->
        <div id="pp-role-tags" style="display:flex;flex-wrap:wrap;gap:6px;padding-bottom:16px"></div>
      </div>
    </div>

    <!-- ── MAIN CONTENT: 2-column layout ── -->
    <div style="max-width:900px;margin:0 auto;padding:20px 32px 40px;display:grid;grid-template-columns:1fr 320px;gap:20px;align-items:start">

      <!-- LEFT COLUMN: Profile content -->
      <div style="display:flex;flex-direction:column;gap:16px">

        <!-- About / Bio -->
        <div id="pp-bio-card" style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:12px">About</div>
          <div id="pp-bio-text" style="font-size:14px;color:var(--text2);line-height:1.7">No bio yet. Complete your profile to tell others about yourself.</div>
        </div>

        <!-- AI Match Stats (shown when data available) -->
        <div id="pp-match-card" style="display:none;background:linear-gradient(135deg,#fff7f0,#fff);border:1px solid rgba(232,100,10,0.2);border-radius:12px;padding:20px 22px;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px">
            <div style="font-size:16px;font-weight:800;color:var(--text1)">&#10022; AI Match Results</div>
            <span style="font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;background:#fdf0ea;color:#e8640a">Powered by AI</span>
          </div>
          <div id="pp-match-stats" style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px"></div>
        </div>

        <!-- Looking For -->
        <div style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:14px">Looking For</div>
          <div id="pp-looking-grid" style="display:flex;gap:8px;flex-wrap:wrap">
            <span style="font-size:12px;color:var(--text3);font-style:italic">Complete onboarding to set your goals</span>
          </div>
        </div>

        <!-- Games & Projects (role-adaptive: shown for developers, hidden for others unless they have projects) -->
        <div id="pp-games-section" style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
            <div style="font-size:16px;font-weight:800;color:var(--text1)">Games &amp; Projects</div>
            <span id="pp-games-count" style="font-size:11px;color:var(--text3)"></span>
          </div>
          <div id="pp-games-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
            <div style="border-radius:10px;border:1.5px dashed #ddd;background:#fafafa;display:flex;align-items:center;justify-content:center;min-height:110px;color:#aaa;font-size:12px;cursor:pointer" onclick="switchMode(\'projects\')">+ Browse Projects</div>
          </div>
        </div>

        <!-- Experience -->
        <div style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:16px">Experience</div>
          <div id="pp-exp-list" style="display:flex;flex-direction:column;gap:16px">
            <div style="display:flex;align-items:flex-start;gap:14px">
              <div id="pp-exp-logo" style="width:42px;height:42px;border-radius:8px;background:linear-gradient(135deg,#e8640a,#f59e0b);flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff">🎮</div>
              <div style="flex:1">
                <div id="pp-exp-title" style="font-size:14px;font-weight:700;color:var(--text1)">Member</div>
                <div id="pp-exp-company" style="font-size:13px;color:var(--text2);margin-top:1px">Game Connection</div>
                <div style="font-size:11px;color:var(--text3);margin-top:2px">2024 &#8211; Present</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Skills & Interests -->
        <div style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:14px">Skills &amp; Interests</div>
          <div id="pp-skills-list" style="display:flex;flex-wrap:wrap;gap:7px">
            <span style="font-size:12px;color:var(--text3);font-style:italic">No skills added yet</span>
          </div>
        </div>

        <!-- Events Attended -->
        <div style="background:#fff;border-radius:12px;padding:20px 22px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:16px;font-weight:800;color:var(--text1);margin-bottom:16px">Events Attended</div>
          <div style="display:flex;flex-direction:column;gap:14px">
            <div style="display:flex;align-items:center;gap:14px">
              <div style="width:44px;height:44px;border-radius:8px;background:linear-gradient(135deg,#1d4ed8,#0a7fa8);display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:800;color:#fff;text-align:center;line-height:1.2;flex-shrink:0">GDC<br>2026</div>
              <div><div style="font-size:13px;font-weight:600;color:var(--text1)">Game Developers Conference 2026</div><div style="font-size:11px;color:var(--text3)">San Francisco &middot; March 2026</div></div>
            </div>
            <div style="display:flex;align-items:center;gap:14px">
              <div style="width:44px;height:44px;border-radius:8px;background:linear-gradient(135deg,#e8640a,#f59e0b);display:flex;align-items:center;justify-content:center;font-size:7px;font-weight:800;color:#fff;text-align:center;line-height:1.2;flex-shrink:0">GC<br>WEST</div>
              <div><div style="font-size:13px;font-weight:600;color:var(--text1)">Game Connection West 2025</div><div style="font-size:11px;color:var(--text3)">San Francisco &middot; March 2025</div></div>
            </div>
          </div>
        </div>

      </div><!-- /left column -->

      <!-- RIGHT COLUMN: Stats + Settings + People -->
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

        <!-- Account Settings -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:14px">Account</div>
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:30px;height:30px;border-radius:7px;background:#fdf0ea;display:flex;align-items:center;justify-content:center;flex-shrink:0">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#e8640a" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </div>
              <div style="flex:1;min-width:0">
                <div style="font-size:11px;font-weight:600;color:var(--text1)">Email Address</div>
                <div id="pp-email" style="font-size:11px;color:var(--text2);margin-top:1px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">&#8212;</div>
              </div>
            </div>
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:30px;height:30px;border-radius:7px;background:#e8f5e9;display:flex;align-items:center;justify-content:center;flex-shrink:0">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#188038" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <div style="flex:1;min-width:0">
                <div style="font-size:11px;font-weight:600;color:var(--text1)">Google Account</div>
                <div style="font-size:11px;color:#188038;margin-top:1px">Connected</div>
              </div>
              <span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:8px;background:#e8f5e9;color:#188038">&#10003;</span>
            </div>
          </div>
        </div>

        <!-- Notifications -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:14px">Notifications</div>
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Event Reminders</div><div style="font-size:10px;color:var(--text2);margin-top:1px">Before events start</div></div>
              <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">New Matches</div><div style="font-size:10px;color:var(--text2);margin-top:1px">AI found new connections</div></div>
              <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Messages</div><div style="font-size:10px;color:var(--text2);margin-top:1px">New message notifications</div></div>
              <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Weekly Digest</div><div style="font-size:10px;color:var(--text2);margin-top:1px">Industry news every Monday</div></div>
              <div class="pp-toggle" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
          </div>
        </div>

        <!-- Privacy -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:14px">Privacy</div>
          <div style="display:flex;flex-direction:column;gap:12px">
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Profile Visibility</div><div style="font-size:10px;color:var(--text2);margin-top:1px">Visible to all members</div></div>
              <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Show in AI Matching</div><div style="font-size:10px;color:var(--text2);margin-top:1px">Let AI suggest you to others</div></div>
              <div class="pp-toggle on" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between">
              <div><div style="font-size:11px;font-weight:600;color:var(--text1)">Contact Info Visible</div><div style="font-size:10px;color:var(--text2);margin-top:1px">Show email to connections</div></div>
              <div class="pp-toggle" onclick="this.classList.toggle(\'on\')"><div class="pp-thumb"></div></div>
            </div>
          </div>
        </div>

        <!-- Quick Links -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:12px">Quick Links</div>
          <!-- Admin entry: shown via JS for admin accounts only -->
          <div id="pp-admin-entry" style="display:none;margin-bottom:8px">
            <a href="_admin.html" target="_blank" style="display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;border:1.5px solid rgba(229,57,53,0.3);background:rgba(229,57,53,0.04);text-decoration:none;transition:background .12s" onmouseover="this.style.background=\'rgba(229,57,53,0.09)\'" onmouseout="this.style.background=\'rgba(229,57,53,0.04)\'">
              <div style="width:28px;height:28px;border-radius:7px;background:linear-gradient(135deg,#b71c1c,#e53935);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0">⚙️</div>
              <div><div style="font-size:11px;font-weight:700;color:#e53935">Admin Dashboard</div><div style="font-size:10px;color:var(--text2)">Super admin control panel</div></div>
              <div style="margin-left:auto;font-size:11px;color:#e53935">↗</div>
            </a>
          </div>
          <div style="display:flex;flex-direction:column;gap:7px">
            <a href="DealFlow_v1_PC.html" style="display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;border:1px solid #e4e6ea;text-decoration:none;transition:background .12s" onmouseover="this.style.background=\'#f7f8fa\'" onmouseout="this.style.background=\'#fff\'">
              <div style="width:28px;height:28px;border-radius:7px;background:linear-gradient(135deg,#312e81,#4f46e5);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0">🤝</div>
              <div><div style="font-size:11px;font-weight:700;color:var(--text1)">Deal Room</div><div style="font-size:10px;color:var(--text2)">Publisher &amp; investor pipeline</div></div>
              <div style="margin-left:auto;font-size:11px;color:var(--text3)">↗</div>
            </a>
            <a href="EventHQ_Dashboard_v1_PC.html" style="display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:9px;border:1px solid #e4e6ea;text-decoration:none;transition:background .12s" onmouseover="this.style.background=\'#f7f8fa\'" onmouseout="this.style.background=\'#fff\'">
              <div style="width:28px;height:28px;border-radius:7px;background:linear-gradient(135deg,#1c1a17,#2a2520);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0">⚡</div>
              <div><div style="font-size:11px;font-weight:700;color:var(--text1)">Event HQ</div><div style="font-size:10px;color:var(--text2)">Organizer dashboard</div></div>
              <div style="margin-left:auto;font-size:11px;color:var(--text3)">↗</div>
            </a>
          </div>
        </div>

        <!-- Danger zone -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#dc2626;text-transform:uppercase;margin-bottom:12px">Danger Zone</div>
          <div style="display:flex;flex-direction:column;gap:8px">
            <button onclick="signOutUser()" style="width:100%;padding:9px;border-radius:9px;border:1.5px solid #dc2626;background:#fff;color:#dc2626;font-size:12px;font-weight:700;cursor:pointer;text-align:left">Sign Out of All Devices</button>
            <button style="width:100%;padding:9px;border-radius:9px;border:1.5px solid #ddd;background:#fff;color:#666;font-size:12px;font-weight:600;cursor:pointer;text-align:left">Delete Account</button>
          </div>
        </div>

        <!-- People You May Know -->
        <div style="background:#fff;border-radius:12px;padding:18px 20px;border:1px solid #e0ddd8;box-shadow:0 1px 3px rgba(0,0,0,0.04)">
          <div style="font-size:13px;font-weight:800;color:var(--text1);margin-bottom:14px">People You May Know</div>
          <div id="pp-people-list" style="display:flex;flex-direction:column;gap:10px"></div>
        </div>

      </div><!-- /right column -->
    </div><!-- /main content grid -->
  </div><!-- /pp-loggedin -->
</div><!-- /profile-panel -->'''

# Find and replace the profile panel HTML
old_start = '<!-- PROFILE & SETTINGS PANEL -->'
old_end = '</div><!-- /profile-panel -->'

start_idx = content.find(old_start)
end_idx = content.find(old_end, start_idx) + len(old_end)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find profile panel markers!")
    exit(1)

print(f"Found profile panel: chars {start_idx} to {end_idx}")
content = content[:start_idx] + NEW_PROFILE_PANEL + content[end_idx:]
print("Profile panel HTML replaced successfully")

# ── 2. 替换 populateProfilePanel JS 函数 ────────────────────────────────────
NEW_POPULATE_JS = '''// ── Populate Profile Panel (full-screen) ──
function populateProfilePanel(data){
  const profile = data.profile || {};
  const stats = (data.aiResult && data.aiResult.stats) || [];
  const selections = data.selections || {};
  const name = profile.name || 'Your Name';
  const company = profile.company || 'Game Connection';
  const initials = name.split(\' \').map(w=>w[0]).join(\'\').slice(0,2).toUpperCase();
  const roles = selections.roles || [];
  const goals = selections.goals || [];

  // ── Role → visual config ──
  const _ROLE_CFG = {
    publisher:  { label:\'Publisher\',  badge:\'background:#fdf0ea;color:#e8640a\', cover:\'135deg,#1a0a00 0%,#3d1a00 40%,#7c3a00 70%,#e8640a 100%\' },
    investor:   { label:\'Investor\',   badge:\'background:#eff6ff;color:#2563eb\', cover:\'135deg,#0a0f2e 0%,#0f1f5c 40%,#1d3a8a 70%,#2563eb 100%\' },
    developer:  { label:\'Developer\',  badge:\'background:#f0fdf4;color:#16a34a\', cover:\'135deg,#001a0a 0%,#003d1a 40%,#005c2a 70%,#16a34a 100%\' },
    media:      { label:\'Media\',      badge:\'background:#fdf4ff;color:#9333ea\', cover:\'135deg,#1a0028 0%,#3d0060 40%,#6b0099 70%,#9333ea 100%\' },
    organizer:  { label:\'Organizer\',  badge:\'background:#fff7ed;color:#ea580c\', cover:\'135deg,#1a0500 0%,#3d1200 40%,#7c2a00 70%,#ea580c 100%\' },
  };
  // Detect primary role
  const primaryRole = (function(){
    const r = (roles[0] || \'\').toLowerCase();
    if (/publisher|publish/i.test(r)) return \'publisher\';
    if (/investor|invest|vc|fund/i.test(r)) return \'investor\';
    if (/developer|studio|indie|dev/i.test(r)) return \'developer\';
    if (/media|press|journal/i.test(r)) return \'media\';
    if (/organizer|organis|event/i.test(r)) return \'organizer\';
    return null;
  })();
  const roleCfg = _ROLE_CFG[primaryRole] || { label:\'Member\', badge:\'background:#f3f4f6;color:#374151\', cover:\'135deg,#1a1a2e 0%,#16213e 40%,#0f3460 70%,#e94560 100%\' };

  // ── Avatar ──
  const av = document.getElementById(\'pp-avatar\');
  if(av){
    if(profile.avatar){
      av.style.backgroundImage = \'url(\' + profile.avatar + \')\';
      av.style.backgroundSize = \'cover\';
      av.textContent = \'\';
    } else {
      av.textContent = initials;
    }
  }

  // ── Cover gradient (role-based) ──
  const cover = document.getElementById(\'pp-cover\');
  if(cover) cover.style.background = \'linear-gradient(\' + roleCfg.cover + \')\';

  // ── Name + role badge ──
  const nm = document.getElementById(\'pp-name\');
  if(nm) nm.textContent = name;
  const badge = document.getElementById(\'pp-role-badge\');
  if(badge){ badge.textContent = roleCfg.label; badge.style.cssText += \';\' + roleCfg.badge; }
  const rl = document.getElementById(\'pp-role\');
  if(rl) rl.textContent = (profile.title || \'Member\') + \' · \' + company;

  // ── Meta (location + website) ──
  const meta = document.getElementById(\'pp-meta\');
  if(meta){
    meta.innerHTML = \'\';
    if(profile.country){ const s=document.createElement(\'span\'); s.textContent=\'📍 \'+(profile.city?profile.city+\', \':\'\')+profile.country; meta.appendChild(s); }
    if(profile.website){ const s=document.createElement(\'a\'); s.href=profile.website; s.target=\'_blank\'; s.style.cssText=\'color:var(--text3);text-decoration:none\'; s.textContent=\'🌐 Website\'; meta.appendChild(s); }
    if(profile.email && !profile.country){ const s=document.createElement(\'span\'); s.textContent=\'✉️ \'+profile.email; meta.appendChild(s); }
  }

  // ── Role tags ──
  const tagsEl = document.getElementById(\'pp-role-tags\');
  if(tagsEl){
    tagsEl.innerHTML = \'\';
    const allTags = [...roles.slice(0,3)];
    if(goals[0]) allTags.push(\'🎯 \'+goals[0]);
    allTags.forEach(r => {
      const t = document.createElement(\'span\');
      t.style.cssText = \'font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px;background:rgba(0,0,0,0.08);color:var(--text2);border:1px solid rgba(0,0,0,0.1)\';
      t.textContent = r;
      tagsEl.appendChild(t);
    });
  }

  // ── Bio ──
  const bioText = document.getElementById(\'pp-bio-text\');
  const bio = profile.bio || _GC_DEMO_MEMBERS.find(m => m.email === profile.email)?.bio || \'\';
  if(bioText) bioText.textContent = bio || \'No bio yet. Complete your profile to tell others about yourself.\';

  // ── AI Match Stats ──
  const matchCard = document.getElementById(\'pp-match-card\');
  const matchStats = document.getElementById(\'pp-match-stats\');
  if(matchCard && matchStats && stats.length > 0){
    matchCard.style.display = \'block\';
    matchStats.innerHTML = \'\';
    stats.forEach(s => {
      const col = document.createElement(\'div\');
      col.style.cssText = \'text-align:center;padding:12px 8px;background:rgba(232,100,10,0.06);border-radius:10px;border:1px solid rgba(232,100,10,0.15)\';
      col.innerHTML = \'<div style="font-size:22px;font-weight:900;color:#e8640a">\'+s.num+\'</div><div style="font-size:10px;color:var(--text2);margin-top:3px;line-height:1.3">\'+s.label+\'</div>\';
      matchStats.appendChild(col);
    });
  }

  // ── Email ──
  const emailEl = document.getElementById(\'pp-email\');
  if(emailEl && profile.email) emailEl.textContent = profile.email;

  // ── Looking For ──
  const lookingEl = document.getElementById(\'pp-looking-grid\');
  if(lookingEl){
    lookingEl.innerHTML = \'\';
    const icons = {\'Find co-publishing deals\':\'🤝\',\'Source new games\':\'🎮\',\'Meet investors\':\'💰\',\'Discover studios\':\'🏢\',\'Hire talent\':\'👥\',\'Explore events\':\'📅\',\'Do market research\':\'📊\',\'Pitch my game / studio\':\'🚀\',\'Scout new titles\':\'🔍\',\'Build partnerships\':\'🤝\',\'Raise funding\':\'💰\',\'Find service providers\':\'🛠️\',\'Network with peers\':\'🌐\'};
    if(goals.length > 0){
      goals.forEach(g => {
        const span = document.createElement(\'span\');
        span.style.cssText = \'font-size:12px;font-weight:600;padding:6px 14px;border-radius:20px;border:1.5px solid rgba(232,100,10,0.3);color:#e8640a;background:#fff7f0;display:inline-flex;align-items:center;gap:5px\';
        span.textContent = (icons[g] || \'✦\') + \' \' + g;
        lookingEl.appendChild(span);
      });
    } else {
      lookingEl.innerHTML = \'<span style="font-size:12px;color:var(--text3);font-style:italic">Complete onboarding to set your goals</span>\';
    }
  }

  // ── Skills ──
  const skillsEl = document.getElementById(\'pp-skills-list\');
  if(skillsEl){
    skillsEl.innerHTML = \'\';
    const focuses = selections.focuses || [];
    const allSkills = [...focuses, \'Game Industry\', \'Networking\', \'Events\'];
    if(allSkills.length > 0){
      allSkills.forEach((f, i) => {
        const t = document.createElement(\'span\');
        t.style.cssText = i < focuses.length
          ? \'font-size:12px;font-weight:700;padding:5px 14px;border-radius:20px;background:rgba(232,100,10,0.1);color:#e8640a;border:1px solid rgba(232,100,10,0.2)\'
          : \'font-size:12px;font-weight:600;padding:5px 14px;border-radius:20px;background:#f3f4f6;color:#555;border:1px solid #e4e6ea\';
        t.textContent = f;
        skillsEl.appendChild(t);
      });
    }
  }

  // ── Experience ──
  const expTitle = document.getElementById(\'pp-exp-title\');
  const expCo = document.getElementById(\'pp-exp-company\');
  if(expTitle) expTitle.textContent = profile.title || \'Member\';
  if(expCo) expCo.textContent = company;

  // ── People You May Know ──
  loadProfilePeople(selections);

  // ── Games (always load from Supabase) ──
  loadProfileGames(true);
}'''

# Find and replace populateProfilePanel function
old_func_start = '// ── Populate Profile Panel (full-screen) ──'
old_func_end = '  loadProfileGames(isDeveloper);\n}'

func_start_idx = content.find(old_func_start)
func_end_idx = content.find(old_func_end, func_start_idx) + len(old_func_end)

if func_start_idx == -1 or func_end_idx == -1:
    print("ERROR: Could not find populateProfilePanel function!")
    print(f"func_start_idx={func_start_idx}, func_end_idx={func_end_idx}")
    exit(1)

print(f"Found populateProfilePanel: chars {func_start_idx} to {func_end_idx}")
content = content[:func_start_idx] + NEW_POPULATE_JS + content[func_end_idx:]
print("populateProfilePanel JS replaced successfully")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! index.html written successfully")
print(f"New total chars: {len(content)}")
