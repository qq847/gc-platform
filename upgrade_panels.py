#!/usr/bin/env python3
"""
One-shot panel upgrade script for EventHQ_Dashboard_v3_PC.html
Replaces all module panel HTML with upgraded versions.
"""

import re

FILE = '/home/ubuntu/gc-platform/EventHQ_Dashboard_v3_PC.html'

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
STAT_CARD = lambda num, label, color: f'''<div class="editor-card" style="flex:1;text-align:center;padding:18px 12px">
            <div style="font-size:26px;font-weight:800;color:{color};letter-spacing:-1px">{num}</div>
            <div style="font-size:11px;color:#6b7280;margin-top:2px;text-transform:uppercase;letter-spacing:.5px">{label}</div>
          </div>'''

TOPBAR = lambda title, left_btns, right_btns: f'''<div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)">{title}</span>
            {left_btns}
          </div>
          <div class="editor-topbar-right">
            {right_btns}
          </div>
        </div>'''

SECTION_HEAD = lambda title, btn='': f'''<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">{title}</div>
            {btn}
          </div>'''

TAG = lambda text, bg, color: f'<span style="font-size:11px;background:{bg};color:{color};padding:3px 9px;border-radius:20px;font-weight:600">{text}</span>'

# ─────────────────────────────────────────────────────────────────────────────
# ATTENDEES  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_ATTENDEES = '''      <!-- ══ VIEW: Attendees ══ -->
      <div id="viewAttendees" style="display:none">
        <div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)" id="attEventTitle">Attendees</span>
          </div>
          <div class="editor-topbar-right">
            <button class="btn-secondary" onclick="exportAttendeesCSV()">⬇ Export CSV</button>
            <button class="btn-primary" onclick="showToast('Invite sent!')">+ Invite</button>
          </div>
        </div>

        <!-- Stats row -->
        <div style="display:flex;gap:12px;margin-bottom:20px">
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#2563eb" id="att-stat-total">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Registered</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#16a34a" id="att-stat-checkedin">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Checked In</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#d97706" id="att-stat-pending">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Not Yet</div>
          </div>
          <div class="editor-card" style="flex:1;padding:16px">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px">Check-in Rate</div>
            <div style="height:8px;background:#e5e7eb;border-radius:4px;overflow:hidden">
              <div id="att-checkin-bar" style="height:100%;background:#16a34a;border-radius:4px;transition:width .4s;width:0%"></div>
            </div>
            <div style="font-size:13px;font-weight:700;color:#16a34a;margin-top:4px" id="att-checkin-pct">0%</div>
          </div>
        </div>

        <!-- Filter tabs + search -->
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;gap:12px;flex-wrap:wrap">
          <div style="display:flex;gap:4px;background:#f3f4f6;border-radius:8px;padding:3px">
            <button id="att-tab-all" onclick="filterAttendeesByTab('all')" style="padding:6px 14px;border-radius:6px;border:none;font-size:12px;font-weight:600;cursor:pointer;background:#fff;color:#111827;box-shadow:0 1px 3px rgba(0,0,0,.1)">All</button>
            <button id="att-tab-in" onclick="filterAttendeesByTab('in')" style="padding:6px 14px;border-radius:6px;border:none;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#6b7280">Checked In</button>
            <button id="att-tab-out" onclick="filterAttendeesByTab('out')" style="padding:6px 14px;border-radius:6px;border:none;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#6b7280">Pending</button>
          </div>
          <input id="att-search" class="form-input" type="text" placeholder="Search name, company, role…" style="max-width:280px" oninput="filterAttendees()">
        </div>

        <div class="editor-card" style="padding:0;overflow:hidden">
          <table style="width:100%;border-collapse:collapse">
            <thead>
              <tr style="background:#f8f9fa;border-bottom:2px solid #e5e7eb">
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Name</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Company</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Role</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Registered</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Check-in</th>
                <th style="padding:11px 16px;width:40px"></th>
              </tr>
            </thead>
            <tbody id="att-tbody"></tbody>
          </table>
          <div id="att-empty" style="display:none;padding:56px;text-align:center;color:#9ca3af">
            <div style="font-size:40px;margin-bottom:10px">👥</div>
            <div style="font-weight:600;font-size:15px;color:#374151">No attendees yet</div>
            <div style="font-size:13px;margin-top:4px">Registrations will appear here once people sign up.</div>
          </div>
        </div>
        <div id="att-footer" style="margin-top:10px;font-size:12px;color:#9ca3af"></div>
      </div>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROJECTS  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PROJECTS = '''      <!-- ══ VIEW: Projects ══ -->
      <div id="viewProjects" style="display:none">
        <div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)" id="projEventTitle">Projects</span>
          </div>
          <div class="editor-topbar-right">
            <button class="btn-secondary" onclick="exportProjectsCSV()">⬇ Export CSV</button>
            <button class="btn-primary" onclick="showToast('Add project coming soon')">+ Add Project</button>
          </div>
        </div>

        <!-- Stats -->
        <div style="display:flex;gap:12px;margin-bottom:20px">
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#2563eb" id="proj-stat-total">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Submitted</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#16a34a" id="proj-stat-approved">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Approved</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#d97706" id="proj-stat-pending">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Pending Review</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#dc2626" id="proj-stat-rejected">0</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Rejected</div>
          </div>
        </div>

        <!-- Submission settings -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
            <div style="font-weight:700;font-size:15px">🎮 Submission Settings</div>
          </div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Submission Deadline</div>
              <input type="date" class="form-input" value="2027-01-15">
            </div>
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Max Projects per Company</div>
              <input type="number" value="3" min="1" class="form-input">
            </div>
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Open for Submissions</div>
              <label style="display:flex;align-items:center;gap:8px;cursor:pointer;margin-top:8px">
                <input type="checkbox" checked style="width:16px;height:16px;accent-color:#16a34a">
                <span style="font-size:13px;font-weight:500">Accepting submissions</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Search + table -->
        <div style="margin-bottom:12px">
          <input id="proj-search" class="form-input" type="text" placeholder="Search by project name or company…" style="max-width:320px" oninput="filterProjects()">
        </div>
        <div class="editor-card" style="padding:0;overflow:hidden">
          <table style="width:100%;border-collapse:collapse">
            <thead>
              <tr style="background:#f8f9fa;border-bottom:2px solid #e5e7eb">
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Project</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Company</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Genre</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Platform</th>
                <th style="padding:11px 16px;text-align:left;font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Status</th>
                <th style="padding:11px 16px;width:80px"></th>
              </tr>
            </thead>
            <tbody id="proj-tbody"></tbody>
          </table>
          <div id="proj-empty" style="display:none;padding:56px;text-align:center;color:#9ca3af">
            <div style="font-size:40px;margin-bottom:10px">🎮</div>
            <div style="font-weight:600;font-size:15px;color:#374151">No projects submitted yet</div>
            <div style="font-size:13px;margin-top:4px">Projects will appear here once developers submit them.</div>
          </div>
        </div>
        <div id="proj-footer" style="margin-top:10px;font-size:12px;color:#9ca3af"></div>
      </div>
'''

# ─────────────────────────────────────────────────────────────────────────────
# FREE TICKET  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_FREE_TICKET = '''      <!-- ══ VIEW: Free Ticket ══ -->
      <div id="viewFreeTicket" style="display:none">
        <div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)">Free Ticket</span>
          </div>
          <div class="editor-topbar-right">
            <button class="btn-secondary" onclick="showToast('Preview form coming soon')">👁 Preview Form</button>
            <button class="btn-primary" onclick="showToast('Changes saved')">Save Changes</button>
          </div>
        </div>

        <!-- Stats -->
        <div style="display:flex;gap:12px;margin-bottom:20px">
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#2563eb">347</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Claimed</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#16a34a">153</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Remaining</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#d97706">24</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Pending Approval</div>
          </div>
          <div class="editor-card" style="flex:1;padding:16px">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px">Capacity Used</div>
            <div style="height:8px;background:#e5e7eb;border-radius:4px;overflow:hidden">
              <div style="height:100%;background:#2563eb;border-radius:4px;width:69%"></div>
            </div>
            <div style="font-size:13px;font-weight:700;color:#2563eb;margin-top:4px">69%</div>
          </div>
        </div>

        <!-- Status toggle -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <div>
              <div style="font-weight:700;font-size:15px;margin-bottom:2px">🎫 Accept Free Registrations</div>
              <div style="font-size:12px;color:#6b7280">When enabled, attendees can claim a free ticket</div>
            </div>
            <label style="position:relative;display:inline-block;width:44px;height:24px;flex-shrink:0">
              <input type="checkbox" checked style="opacity:0;width:0;height:0">
              <span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background:#16a34a;border-radius:24px;transition:.3s" onclick="this.previousElementSibling.click()"></span>
            </label>
          </div>
        </div>

        <!-- Ticket types -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">Ticket Types</div>
            <button class="btn-secondary" style="font-size:12px;padding:6px 12px" onclick="showToast('Add type coming soon')">+ Add Type</button>
          </div>
          <div style="display:flex;flex-direction:column;gap:8px">
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px;display:flex;align-items:center;gap:14px">
              <span style="font-size:22px">🎫</span>
              <div style="flex:1">
                <div style="font-size:14px;font-weight:700">General Admission</div>
                <div style="font-size:12px;color:#6b7280;margin-top:2px">Standard free entry · Max 1 per person · Unlimited capacity</div>
                <div style="height:5px;background:#e5e7eb;border-radius:3px;margin-top:8px;max-width:200px"><div style="width:69%;height:100%;background:#2563eb;border-radius:3px"></div></div>
              </div>
              <div style="text-align:right">
                <span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:3px 9px;border-radius:20px;font-weight:600">Active</span>
                <div style="font-size:12px;color:#6b7280;margin-top:6px">347 / 500</div>
              </div>
              <button style="border:none;background:none;cursor:pointer;color:#9ca3af;font-size:14px" onclick="showToast('Edit coming soon')">✏️</button>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px;display:flex;align-items:center;gap:14px">
              <span style="font-size:22px">⭐</span>
              <div style="flex:1">
                <div style="font-size:14px;font-weight:700">Speaker Pass</div>
                <div style="font-size:12px;color:#6b7280;margin-top:2px">Speakers &amp; panelists · Invite only · Includes backstage access</div>
              </div>
              <div style="text-align:right">
                <span style="font-size:11px;background:#dbeafe;color:#1e40af;padding:3px 9px;border-radius:20px;font-weight:600">Invite Only</span>
                <div style="font-size:12px;color:#6b7280;margin-top:6px">38 issued</div>
              </div>
              <button style="border:none;background:none;cursor:pointer;color:#9ca3af;font-size:14px" onclick="showToast('Edit coming soon')">✏️</button>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px;display:flex;align-items:center;gap:14px">
              <span style="font-size:22px">🏢</span>
              <div style="flex:1">
                <div style="font-size:14px;font-weight:700">Press Pass</div>
                <div style="font-size:12px;color:#6b7280;margin-top:2px">Media &amp; journalists · Application required · Includes press room</div>
              </div>
              <div style="text-align:right">
                <span style="font-size:11px;background:#fef3c7;color:#d97706;padding:3px 9px;border-radius:20px;font-weight:600">Application</span>
                <div style="font-size:12px;color:#6b7280;margin-top:6px">12 approved</div>
              </div>
              <button style="border:none;background:none;cursor:pointer;color:#9ca3af;font-size:14px" onclick="showToast('Edit coming soon')">✏️</button>
            </div>
          </div>
        </div>

        <!-- Capacity & deadline -->
        <div class="editor-card">
          <div style="font-weight:700;font-size:15px;margin-bottom:14px">🎯 Capacity &amp; Deadline</div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Total Capacity</div>
              <input type="number" value="500" class="form-input">
            </div>
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Claim Deadline</div>
              <input type="date" class="form-input">
            </div>
            <div>
              <div style="font-size:11px;color:#6b7280;margin-bottom:4px">Waitlist</div>
              <label style="display:flex;align-items:center;gap:8px;cursor:pointer;margin-top:8px">
                <input type="checkbox" style="width:16px;height:16px;accent-color:#16a34a">
                <span style="font-size:13px">Enable waitlist</span>
              </label>
            </div>
          </div>
        </div>
      </div>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PAID TICKET  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PAID_TICKET = '''      <!-- ══ VIEW: Paid Ticket ══ -->
      <div id="viewPaidTicket" style="display:none">
        <div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)">Paid Ticket</span>
          </div>
          <div class="editor-topbar-right">
            <button class="btn-secondary" onclick="showToast('Opening Stripe dashboard…')">💳 Stripe Dashboard</button>
            <button class="btn-secondary" onclick="showToast('Orders exported')">⬇ Export Orders</button>
            <button class="btn-primary" onclick="showToast('Changes saved')">Save Changes</button>
          </div>
        </div>

        <!-- Stats -->
        <div style="display:flex;gap:12px;margin-bottom:20px">
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#16a34a">€18,450</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Total Revenue</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#2563eb">98</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Tickets Sold</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#d97706">272</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Remaining</div>
          </div>
          <div class="editor-card" style="flex:1;text-align:center;padding:16px">
            <div style="font-size:26px;font-weight:800;color:#9333ea">€188</div>
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Avg. Ticket Price</div>
          </div>
        </div>

        <!-- Ticket types -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">Ticket Types</div>
            <button class="btn-secondary" style="font-size:12px;padding:6px 12px" onclick="showToast('Add type coming soon')">+ Add Type</button>
          </div>
          <div style="display:flex;flex-direction:column;gap:10px">
            <!-- Early Bird -->
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;border-left:4px solid #16a34a">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
                <div>
                  <div style="font-size:15px;font-weight:700">Early Bird</div>
                  <div style="font-size:12px;color:#6b7280">Sale ends Mar 31 · Max 2 per order</div>
                </div>
                <div style="display:flex;gap:6px;align-items:center">
                  <span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:3px 9px;border-radius:20px;font-weight:600">Active</span>
                  <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="showToast('Edit coming soon')">✏️ Edit</button>
                </div>
              </div>
              <div style="font-size:24px;font-weight:800;color:#16a34a;margin-bottom:12px">€99 <span style="font-size:13px;font-weight:400;color:#6b7280">/ ticket</span></div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px">
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Inventory</div><div style="font-weight:700;font-size:18px">50</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Sold</div><div style="font-weight:700;font-size:18px;color:#16a34a">23</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Left</div><div style="font-weight:700;font-size:18px">27</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Revenue</div><div style="font-weight:700;font-size:16px">€2,277</div></div>
              </div>
              <div style="height:6px;background:#e5e7eb;border-radius:3px"><div style="width:46%;height:100%;background:#16a34a;border-radius:3px"></div></div>
              <div style="font-size:11px;color:#6b7280;margin-top:4px">46% sold</div>
            </div>
            <!-- Standard -->
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;border-left:4px solid #2563eb">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
                <div>
                  <div style="font-size:15px;font-weight:700">Standard</div>
                  <div style="font-size:12px;color:#6b7280">Sale ends Jun 10 · Max 5 per order</div>
                </div>
                <div style="display:flex;gap:6px;align-items:center">
                  <span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:3px 9px;border-radius:20px;font-weight:600">Active</span>
                  <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="showToast('Edit coming soon')">✏️ Edit</button>
                </div>
              </div>
              <div style="font-size:24px;font-weight:800;color:#2563eb;margin-bottom:12px">€149 <span style="font-size:13px;font-weight:400;color:#6b7280">/ ticket</span></div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px">
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Inventory</div><div style="font-weight:700;font-size:18px">200</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Sold</div><div style="font-weight:700;font-size:18px;color:#16a34a">67</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Left</div><div style="font-weight:700;font-size:18px">133</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Revenue</div><div style="font-weight:700;font-size:16px">€9,983</div></div>
              </div>
              <div style="height:6px;background:#e5e7eb;border-radius:3px"><div style="width:33%;height:100%;background:#2563eb;border-radius:3px"></div></div>
              <div style="font-size:11px;color:#6b7280;margin-top:4px">33% sold</div>
            </div>
            <!-- VIP -->
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;border-left:4px solid #9333ea">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
                <div>
                  <div style="font-size:15px;font-weight:700">VIP All-Access</div>
                  <div style="font-size:12px;color:#6b7280">Includes dinner, lounge &amp; networking · Max 1 per order</div>
                </div>
                <div style="display:flex;gap:6px;align-items:center">
                  <span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:3px 9px;border-radius:20px;font-weight:600">Active</span>
                  <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="showToast('Edit coming soon')">✏️ Edit</button>
                </div>
              </div>
              <div style="font-size:24px;font-weight:800;color:#9333ea;margin-bottom:12px">€399 <span style="font-size:13px;font-weight:400;color:#6b7280">/ ticket</span></div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px">
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Inventory</div><div style="font-weight:700;font-size:18px">20</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Sold</div><div style="font-weight:700;font-size:18px;color:#16a34a">8</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Left</div><div style="font-weight:700;font-size:18px">12</div></div>
                <div><div style="font-size:10px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Revenue</div><div style="font-weight:700;font-size:16px">€3,192</div></div>
              </div>
              <div style="height:6px;background:#e5e7eb;border-radius:3px"><div style="width:40%;height:100%;background:#9333ea;border-radius:3px"></div></div>
              <div style="font-size:11px;color:#6b7280;margin-top:4px">40% sold</div>
            </div>
          </div>
          <button style="width:100%;margin-top:10px;padding:12px;border:1.5px dashed #d1d5db;border-radius:8px;background:none;font-size:13px;font-weight:600;color:#6b7280;cursor:pointer" onclick="showToast('Add ticket type coming soon')">+ Add New Ticket Type</button>
        </div>

        <!-- Recent orders -->
        <div class="editor-card">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">Recent Orders</div>
            <button class="btn-secondary" style="font-size:12px;padding:6px 12px" onclick="showToast('All orders coming soon')">View All</button>
          </div>
          <table style="width:100%;border-collapse:collapse">
            <thead><tr style="border-bottom:2px solid #e5e7eb">
              <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px">Buyer</th>
              <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px">Ticket</th>
              <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px">Amount</th>
              <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px">Date</th>
              <th style="text-align:left;padding:8px 0;font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px">Status</th>
            </tr></thead>
            <tbody>
              <tr style="border-bottom:1px solid #f3f4f6">
                <td style="padding:10px 0"><div style="font-size:13px;font-weight:600">Yuki Tanaka</div><div style="font-size:11px;color:#9ca3af">Bandai Namco</div></td>
                <td style="padding:10px 0;font-size:13px">Early Bird</td>
                <td style="padding:10px 0;font-size:13px;font-weight:600">€99</td>
                <td style="padding:10px 0;font-size:12px;color:#6b7280">Apr 2, 2026</td>
                <td style="padding:10px 0"><span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:2px 8px;border-radius:4px;font-weight:600">Paid</span></td>
              </tr>
              <tr style="border-bottom:1px solid #f3f4f6">
                <td style="padding:10px 0"><div style="font-size:13px;font-weight:600">Priya Sharma</div><div style="font-size:11px;color:#9ca3af">Ubisoft</div></td>
                <td style="padding:10px 0;font-size:13px">VIP All-Access</td>
                <td style="padding:10px 0;font-size:13px;font-weight:600">€399</td>
                <td style="padding:10px 0;font-size:12px;color:#6b7280">Apr 1, 2026</td>
                <td style="padding:10px 0"><span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:2px 8px;border-radius:4px;font-weight:600">Paid</span></td>
              </tr>
              <tr>
                <td style="padding:10px 0"><div style="font-size:13px;font-weight:600">Marcus Weber</div><div style="font-size:11px;color:#9ca3af">EA Games</div></td>
                <td style="padding:10px 0;font-size:13px">Standard ×2</td>
                <td style="padding:10px 0;font-size:13px;font-weight:600">€298</td>
                <td style="padding:10px 0;font-size:12px;color:#6b7280">Mar 30, 2026</td>
                <td style="padding:10px 0"><span style="font-size:11px;background:#fef3c7;color:#d97706;padding:2px 8px;border-radius:4px;font-weight:600">Pending</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
'''

# ─────────────────────────────────────────────────────────────────────────────
# PREVIEW  (full public event page)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PREVIEW = '''      <!-- ══ VIEW: Preview ══ -->
      <div id="viewPreview" style="display:none">
        <div class="editor-topbar">
          <div class="editor-topbar-left">
            <button class="back-link" onclick="showEventEditor()">← Event Info</button>
            <span style="font-size:14px;font-weight:700;color:var(--text1)">Preview — Public Event Page</span>
          </div>
          <div class="editor-topbar-right">
            <button class="btn-secondary" onclick="showToast('Link copied!')">🔗 Copy Link</button>
            <button class="btn-primary" onclick="showToast('Opening public page…')">↗ Open Public Page</button>
          </div>
        </div>

        <!-- Hero banner -->
        <div class="editor-card" style="padding:0;overflow:hidden;margin-bottom:20px">
          <div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a8a 60%,#1d4ed8 100%);min-height:200px;display:flex;align-items:flex-end;padding:32px;position:relative">
            <div style="position:absolute;top:20px;right:20px">
              <span id="prev-status-badge" style="font-size:12px;background:rgba(255,255,255,.15);color:#fff;padding:5px 14px;border-radius:20px;font-weight:600;backdrop-filter:blur(4px)">● Draft</span>
            </div>
            <div>
              <div style="font-size:28px;font-weight:900;color:#fff;letter-spacing:-0.5px" id="prev-title">Event Name</div>
              <div style="font-size:14px;color:rgba(255,255,255,0.75);margin-top:6px;display:flex;gap:16px;flex-wrap:wrap">
                <span id="prev-meta-date">📅 Date TBD</span>
                <span id="prev-meta-city">📍 City TBD</span>
                <span id="prev-meta-venue">🏛 Venue TBD</span>
                <span id="prev-meta-format">🎯 In-Person</span>
              </div>
            </div>
          </div>
          <div style="padding:20px 28px;border-bottom:1px solid #e5e7eb">
            <div style="font-size:14px;color:#374151;line-height:1.7" id="prev-desc">No description yet. Add one in Event Info.</div>
          </div>
          <!-- Quick stats -->
          <div style="display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #e5e7eb">
            <div style="padding:16px 20px;text-align:center;border-right:1px solid #e5e7eb">
              <div style="font-size:22px;font-weight:800;color:#2563eb" id="prev-attendees">0</div>
              <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Registered</div>
            </div>
            <div style="padding:16px 20px;text-align:center;border-right:1px solid #e5e7eb">
              <div style="font-size:22px;font-weight:800;color:#16a34a" id="prev-modules">0</div>
              <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Active Modules</div>
            </div>
            <div style="padding:16px 20px;text-align:center;border-right:1px solid #e5e7eb">
              <div style="font-size:22px;font-weight:800;color:#d97706" id="prev-days">—</div>
              <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Days to Event</div>
            </div>
            <div style="padding:16px 20px;text-align:center">
              <div style="font-size:22px;font-weight:800;color:#9333ea" id="prev-website-short">—</div>
              <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Website</div>
            </div>
          </div>
        </div>

        <!-- Two-column layout: actions + info -->
        <div style="display:grid;grid-template-columns:1fr 340px;gap:20px;align-items:start">

          <!-- Left: attendee actions -->
          <div>
            <!-- Register / Tickets section -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:16px">🎫 Get Your Ticket</div>
              <div style="display:flex;flex-direction:column;gap:10px">
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;display:flex;align-items:center;justify-content:space-between">
                  <div>
                    <div style="font-size:14px;font-weight:700">Free Registration</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">General admission · Free</div>
                  </div>
                  <button class="btn-primary" style="font-size:13px;padding:8px 18px" onclick="showToast('Registration form coming soon')">Register Free</button>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;display:flex;align-items:center;justify-content:space-between">
                  <div>
                    <div style="font-size:14px;font-weight:700">Early Bird Ticket</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">Sale ends Mar 31 · Limited availability</div>
                  </div>
                  <div style="text-align:right">
                    <div style="font-size:18px;font-weight:800;color:#16a34a">€99</div>
                    <button class="btn-primary" style="font-size:12px;padding:6px 14px;margin-top:4px" onclick="showToast('Checkout coming soon')">Buy Now</button>
                  </div>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;display:flex;align-items:center;justify-content:space-between">
                  <div>
                    <div style="font-size:14px;font-weight:700">Standard Ticket</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">Full access · Available until Jun 10</div>
                  </div>
                  <div style="text-align:right">
                    <div style="font-size:18px;font-weight:800;color:#2563eb">€149</div>
                    <button class="btn-primary" style="font-size:12px;padding:6px 14px;margin-top:4px" onclick="showToast('Checkout coming soon')">Buy Now</button>
                  </div>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;display:flex;align-items:center;justify-content:space-between;background:linear-gradient(135deg,#faf5ff,#ede9fe)">
                  <div>
                    <div style="font-size:14px;font-weight:700">VIP All-Access</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">Dinner + lounge + networking · Limited to 20</div>
                  </div>
                  <div style="text-align:right">
                    <div style="font-size:18px;font-weight:800;color:#9333ea">€399</div>
                    <button style="font-size:12px;padding:6px 14px;margin-top:4px;background:#9333ea;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600" onclick="showToast('Checkout coming soon')">Buy VIP</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Exhibition Booths -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">🏢 Exhibition Booths</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Showcase your games and products to thousands of industry professionals</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px">
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px">
                  <div style="font-size:13px;font-weight:700">Free Booth</div>
                  <div style="font-size:12px;color:#6b7280;margin-top:2px">Standard 3×3m · Application required</div>
                  <div style="font-size:16px;font-weight:800;color:#16a34a;margin-top:8px">Free</div>
                  <button class="btn-secondary" style="font-size:12px;padding:6px 12px;margin-top:8px;width:100%" onclick="showToast('Booth application coming soon')">Apply</button>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px">
                  <div style="font-size:13px;font-weight:700">Paid Booth</div>
                  <div style="font-size:12px;color:#6b7280;margin-top:2px">Premium 6×6m · Priority placement</div>
                  <div style="font-size:16px;font-weight:800;color:#2563eb;margin-top:8px">From €2,500</div>
                  <button class="btn-primary" style="font-size:12px;padding:6px 12px;margin-top:8px;width:100%" onclick="showToast('Booth booking coming soon')">Book Now</button>
                </div>
              </div>
            </div>

            <!-- Sponsorship -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">🤝 Sponsorship Packages</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Partner with us to reach the global games industry</div>
              <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">
                <div style="border:2px solid #ffd700;border-radius:10px;padding:12px;text-align:center;background:linear-gradient(135deg,#fffbeb,#fef3c7)">
                  <div style="font-size:11px;font-weight:700;color:#92400e;text-transform:uppercase;letter-spacing:.5px">Platinum</div>
                  <div style="font-size:18px;font-weight:800;color:#92400e;margin:6px 0">€50K</div>
                  <button style="font-size:11px;padding:5px 10px;background:#92400e;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600;width:100%" onclick="showToast('Sponsorship enquiry sent')">Enquire</button>
                </div>
                <div style="border:2px solid #c0c0c0;border-radius:10px;padding:12px;text-align:center;background:linear-gradient(135deg,#f8fafc,#f1f5f9)">
                  <div style="font-size:11px;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:.5px">Gold</div>
                  <div style="font-size:18px;font-weight:800;color:#475569;margin:6px 0">€25K</div>
                  <button style="font-size:11px;padding:5px 10px;background:#475569;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600;width:100%" onclick="showToast('Sponsorship enquiry sent')">Enquire</button>
                </div>
                <div style="border:2px solid #cd7f32;border-radius:10px;padding:12px;text-align:center;background:linear-gradient(135deg,#fff7ed,#ffedd5)">
                  <div style="font-size:11px;font-weight:700;color:#9a3412;text-transform:uppercase;letter-spacing:.5px">Silver</div>
                  <div style="font-size:18px;font-weight:800;color:#9a3412;margin:6px 0">€10K</div>
                  <button style="font-size:11px;padding:5px 10px;background:#9a3412;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600;width:100%" onclick="showToast('Sponsorship enquiry sent')">Enquire</button>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:12px;text-align:center">
                  <div style="font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:.5px">Bronze</div>
                  <div style="font-size:18px;font-weight:800;color:#6b7280;margin:6px 0">€5K</div>
                  <button style="font-size:11px;padding:5px 10px;background:#6b7280;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600;width:100%" onclick="showToast('Sponsorship enquiry sent')">Enquire</button>
                </div>
              </div>
            </div>

            <!-- Meeting Pods -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">🎮 Meeting Pods</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Private meeting spaces for B2B discussions</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px">
                  <div style="font-size:13px;font-weight:700">Free Pod</div>
                  <div style="font-size:12px;color:#6b7280;margin-top:2px">20-min sessions · Shared scheduling</div>
                  <div style="font-size:16px;font-weight:800;color:#16a34a;margin-top:8px">Free</div>
                  <button class="btn-secondary" style="font-size:12px;padding:6px 12px;margin-top:8px;width:100%" onclick="showToast('Pod application coming soon')">Apply</button>
                </div>
                <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px">
                  <div style="font-size:13px;font-weight:700">Paid Pod</div>
                  <div style="font-size:12px;color:#6b7280;margin-top:2px">Dedicated pod · Full-day booking</div>
                  <div style="font-size:16px;font-weight:800;color:#2563eb;margin-top:8px">From €800</div>
                  <button class="btn-primary" style="font-size:12px;padding:6px 12px;margin-top:8px;width:100%" onclick="showToast('Pod booking coming soon')">Book Now</button>
                </div>
              </div>
            </div>

            <!-- Game Showcase -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">🕹 Submit Your Game</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Get your game in front of publishers, investors, and press</div>
              <div style="border:1px solid #e5e7eb;border-radius:10px;padding:16px;display:flex;align-items:center;justify-content:space-between">
                <div>
                  <div style="font-size:14px;font-weight:700">Game Showcase</div>
                  <div style="font-size:12px;color:#6b7280;margin-top:2px">Submission deadline: Jan 15, 2027 · Max 3 games per studio</div>
                  <div style="font-size:12px;color:#16a34a;margin-top:4px;font-weight:600">✓ 51 games approved so far</div>
                </div>
                <button class="btn-primary" style="font-size:13px;padding:8px 18px;flex-shrink:0" onclick="showToast('Game submission form coming soon')">Submit Game</button>
              </div>
            </div>

            <!-- Award nominations -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">🏆 Award Nominations</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Nominate your game for the industry's most prestigious awards</div>
              <div style="display:flex;flex-direction:column;gap:8px">
                <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border:1px solid #e5e7eb;border-radius:8px">
                  <div><span style="font-size:14px">🏆</span> <span style="font-size:13px;font-weight:600">Best Indie Game</span> <span style="font-size:12px;color:#6b7280">· 12 nominees</span></div>
                  <button class="btn-secondary" style="font-size:12px;padding:5px 12px" onclick="showToast('Nomination form coming soon')">Nominate</button>
                </div>
                <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border:1px solid #e5e7eb;border-radius:8px">
                  <div><span style="font-size:14px">🎨</span> <span style="font-size:13px;font-weight:600">Best Art Direction</span> <span style="font-size:12px;color:#6b7280">· 8 nominees</span></div>
                  <button class="btn-secondary" style="font-size:12px;padding:5px 12px" onclick="showToast('Nomination form coming soon')">Nominate</button>
                </div>
                <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border:1px solid #e5e7eb;border-radius:8px">
                  <div><span style="font-size:14px">📝</span> <span style="font-size:13px;font-weight:600">Best Narrative</span> <span style="font-size:12px;color:#6b7280">· 9 nominees</span></div>
                  <button class="btn-secondary" style="font-size:12px;padding:5px 12px" onclick="showToast('Nomination form coming soon')">Nominate</button>
                </div>
              </div>
            </div>

            <!-- Buyer Invitation -->
            <div class="editor-card">
              <div style="font-weight:700;font-size:16px;margin-bottom:4px">💼 Hosted Buyer Programme</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:14px">Qualified buyers receive complimentary passes, hotel, and pre-scheduled meetings</div>
              <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:16px;margin-bottom:12px">
                <div style="font-size:13px;font-weight:600;color:#1e40af;margin-bottom:4px">Eligibility Requirements</div>
                <div style="font-size:12px;color:#1e40af;line-height:1.6">• Annual acquisition budget ≥ €500K<br>• Publisher, distributor, investor, or platform holder<br>• Decision-making authority</div>
              </div>
              <button class="btn-primary" style="font-size:13px;padding:9px 20px" onclick="showToast('Buyer application coming soon')">Apply as Hosted Buyer</button>
            </div>
          </div>

          <!-- Right: event info sidebar -->
          <div>
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:15px;margin-bottom:14px">📋 Event Details</div>
              <div style="display:flex;flex-direction:column;gap:10px">
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px;flex-shrink:0">📅</span>
                  <div>
                    <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Date</div>
                    <div style="font-size:13px;font-weight:600" id="prev-detail-date">TBD</div>
                  </div>
                </div>
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px;flex-shrink:0">📍</span>
                  <div>
                    <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Location</div>
                    <div style="font-size:13px;font-weight:600" id="prev-detail-venue">TBD</div>
                  </div>
                </div>
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px;flex-shrink:0">🎯</span>
                  <div>
                    <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Format</div>
                    <div style="font-size:13px;font-weight:600" id="prev-detail-format">In-Person</div>
                  </div>
                </div>
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px;flex-shrink:0">🔗</span>
                  <div>
                    <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Website</div>
                    <div style="font-size:13px;font-weight:600" id="prev-detail-website">—</div>
                  </div>
                </div>
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px;flex-shrink:0">📧</span>
                  <div>
                    <div style="font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px">Contact</div>
                    <div style="font-size:13px;font-weight:600" id="prev-detail-contact">—</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Let's Meet CTA -->
            <div class="editor-card" style="margin-bottom:16px;background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-color:#bbf7d0">
              <div style="font-weight:700;font-size:15px;margin-bottom:6px">🤝 Let's Meet</div>
              <div style="font-size:13px;color:#166534;margin-bottom:12px">Request 1-on-1 meetings with other attendees, exhibitors, and speakers</div>
              <button style="width:100%;padding:9px;background:#16a34a;color:#fff;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer" onclick="showToast('Meeting request coming soon')">Request a Meeting</button>
            </div>

            <!-- Panel/Session -->
            <div class="editor-card" style="margin-bottom:16px">
              <div style="font-weight:700;font-size:15px;margin-bottom:6px">🎤 Speak at the Event</div>
              <div style="font-size:13px;color:#6b7280;margin-bottom:12px">Submit a talk proposal for our conference programme</div>
              <button class="btn-secondary" style="width:100%;padding:9px;font-size:13px" onclick="showToast('Speaker application coming soon')">Submit a Talk</button>
            </div>

            <!-- Share -->
            <div class="editor-card">
              <div style="font-weight:700;font-size:15px;margin-bottom:10px">📣 Share This Event</div>
              <div style="display:flex;gap:8px">
                <button style="flex:1;padding:8px;background:#1877f2;color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer" onclick="showToast('Shared on Facebook!')">Facebook</button>
                <button style="flex:1;padding:8px;background:#0a66c2;color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer" onclick="showToast('Shared on LinkedIn!')">LinkedIn</button>
                <button style="flex:1;padding:8px;background:#000;color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer" onclick="showToast('Shared on X!')">X</button>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

# ─────────────────────────────────────────────────────────────────────────────
# ATTENDEES JS  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_ATTENDEES_JS = '''let _attAll = [];
let _attTab = 'all';

function showAttendees() {
  document.getElementById('viewMyEvents').style.display = 'none';
  document.getElementById('viewEventEditor').style.display = 'none';
  document.getElementById('viewAttendees').style.display = 'block';

  const title = currentEvent ? (currentEvent.name || 'Untitled Event') : '';
  document.getElementById('attEventTitle').textContent = title || 'Attendees';

  const regs = (() => { try { return JSON.parse(localStorage.getItem('gc_registrations') || '[]'); } catch(e){ return []; } })();
  let data = title ? regs.filter(r => r.eventTitle === title) : regs;

  if (!data.length) {
    data = [
      {name:'Ray Zhang',  company:'Game Connection', jobTitle:'CEO',              checkedIn:true,  registeredAt:'2026-03-01'},
      {name:'Alex Chen',  company:'Ubisoft',          jobTitle:'Producer',         checkedIn:true,  registeredAt:'2026-03-02'},
      {name:'Sarah Kim',  company:'EA Games',         jobTitle:'Art Director',     checkedIn:false, registeredAt:'2026-03-03'},
      {name:'Tom Wu',     company:'Tencent',          jobTitle:'Director',         checkedIn:true,  registeredAt:'2026-03-04'},
      {name:'Lisa Park',  company:'Sony Interactive', jobTitle:'Dev Manager',      checkedIn:false, registeredAt:'2026-03-05'},
      {name:'Yuki Tanaka',company:'Bandai Namco',     jobTitle:'Business Dev',     checkedIn:true,  registeredAt:'2026-03-06'},
      {name:'Priya Sharma',company:'Ubisoft',         jobTitle:'Producer',         checkedIn:false, registeredAt:'2026-03-07'},
    ];
  } else {
    data = data.map((r, i) => ({...r, checkedIn: i % 3 !== 2}));
  }

  _attAll = data;
  _attTab = 'all';
  document.getElementById('att-search').value = '';

  // Update stats
  const total = data.length;
  const ci = data.filter(r => r.checkedIn).length;
  const pct = total ? Math.round(ci/total*100) : 0;
  document.getElementById('att-stat-total').textContent = total;
  document.getElementById('att-stat-checkedin').textContent = ci;
  document.getElementById('att-stat-pending').textContent = total - ci;
  document.getElementById('att-checkin-bar').style.width = pct + '%';
  document.getElementById('att-checkin-pct').textContent = pct + '%';

  filterAttendeesByTab('all');
}

function filterAttendeesByTab(tab) {
  _attTab = tab;
  ['all','in','out'].forEach(t => {
    const btn = document.getElementById('att-tab-'+t);
    if (btn) {
      btn.style.background = t === tab ? '#fff' : 'transparent';
      btn.style.color = t === tab ? '#111827' : '#6b7280';
      btn.style.boxShadow = t === tab ? '0 1px 3px rgba(0,0,0,.1)' : 'none';
    }
  });
  filterAttendees();
}

function filterAttendees() {
  const q = document.getElementById('att-search').value.toLowerCase().trim();
  let rows = _attAll;
  if (_attTab === 'in')  rows = rows.filter(r => r.checkedIn);
  if (_attTab === 'out') rows = rows.filter(r => !r.checkedIn);
  if (q) rows = rows.filter(r =>
    (r.name||'').toLowerCase().includes(q) ||
    (r.company||'').toLowerCase().includes(q) ||
    (r.jobTitle||r.role||'').toLowerCase().includes(q)
  );
  renderAttendeesTable(rows);
}

function exportAttendeesCSV() {
  if (!_attAll.length) { showToast('No attendees to export'); return; }
  const csv = ['Name,Company,Role,Registered,Checked In',
    ..._attAll.map(r => [r.name||'',r.company||'',r.jobTitle||r.role||'',r.registeredAt||'',r.checkedIn?'Yes':'No']
      .map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(','))
  ].join('\\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([csv],{type:'text/csv'}));
  a.download = 'attendees.csv'; a.click();
  showToast('CSV exported');
}

function renderAttendeesTable(rows) {
  const tbody = document.getElementById('att-tbody');
  const empty = document.getElementById('att-empty');
  const footer = document.getElementById('att-footer');
  const badge = document.getElementById('att-count-badge');
  if (badge) badge.textContent = rows.length + ' attendees';
  if (!rows.length) {
    tbody.innerHTML = '';
    empty.style.display = 'block';
    footer.textContent = '';
    return;
  }
  empty.style.display = 'none';
  tbody.innerHTML = rows.map((r, i) => {
    const ci = r.checkedIn
      ? '<span style="display:inline-flex;align-items:center;gap:4px;font-size:12px;background:#dcfce7;color:#16a34a;padding:3px 10px;border-radius:20px;font-weight:600">✓ Checked in</span>'
      : '<span style="display:inline-flex;align-items:center;gap:4px;font-size:12px;background:#f3f4f6;color:#9ca3af;padding:3px 10px;border-radius:20px;font-weight:600">○ Pending</span>';
    return `<tr style="border-bottom:1px solid #f3f4f6" onmouseover="this.style.background='#f9fafb'" onmouseout="this.style.background=''">
      <td style="padding:12px 16px">
        <div style="display:flex;align-items:center;gap:10px">
          <div style="width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,#1e3a8a,#2563eb);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0">${(r.name||'?').charAt(0)}</div>
          <div style="font-weight:600;font-size:14px">${r.name||'—'}</div>
        </div>
      </td>
      <td style="padding:12px 16px;font-size:13px;color:#374151">${r.company||'—'}</td>
      <td style="padding:12px 16px;font-size:13px;color:#6b7280">${r.jobTitle||r.role||'—'}</td>
      <td style="padding:12px 16px;font-size:12px;color:#9ca3af">${r.registeredAt||'—'}</td>
      <td style="padding:12px 16px">${ci}</td>
      <td style="padding:12px 16px;text-align:right">
        <button style="border:none;background:none;cursor:pointer;color:#9ca3af;font-size:13px;padding:4px 8px;border-radius:4px" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='none'" onclick="showToast('Attendee details coming soon')">⋯</button>
      </td>
    </tr>`;
  }).join('');
  const ci = rows.filter(r => r.checkedIn).length;
  footer.textContent = `Showing ${rows.length} attendee${rows.length!==1?'s':''} · ${ci} checked in · ${rows.length-ci} pending`;
}
'''

# ─────────────────────────────────────────────────────────────────────────────
# PROJECTS JS  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PROJECTS_JS = '''// ── Projects ────────────────────────────────────────────────────────────────────────────────
let _projAll = [];

function showProjects() {
  hideAllViews();
  document.getElementById('viewProjects').style.display = 'block';

  const ev = currentEvent;
  document.getElementById('projEventTitle').textContent = ev ? ev.name || 'Projects' : 'Projects';

  let projects = [];
  try { projects = JSON.parse(localStorage.getItem('gc_projects') || '[]'); } catch(e) {}
  if (ev) projects = projects.filter(p => p.eventId === ev.id);

  if (!projects.length) {
    projects = [
      { name:'Stellar Drift',  company:'Indie Forge',       genre:'Action RPG',  platform:'PC / Console', status:'Approved' },
      { name:'Neon Abyss 2',   company:'Veewo Games',       genre:'Roguelite',   platform:'PC / Switch',  status:'Pending' },
      { name:'Echo Protocol',  company:'Tarsier Studios',   genre:'Puzzle',      platform:'PC',           status:'Approved' },
      { name:'Void Hunters',   company:'Funcom',            genre:'Survival',    platform:'PC / Console', status:'Rejected' },
      { name:'Pixel Odyssey',  company:'Devolver Digital',  genre:'Platformer',  platform:'All',          status:'Pending' },
      { name:'Arcane Depths',  company:'Raw Fury',          genre:'Dungeon RPG', platform:'PC',           status:'Approved' },
    ];
  }
  _projAll = projects;

  // Stats
  const total    = projects.length;
  const approved = projects.filter(p => p.status==='Approved').length;
  const pending  = projects.filter(p => p.status==='Pending').length;
  const rejected = projects.filter(p => p.status==='Rejected').length;
  document.getElementById('proj-stat-total').textContent    = total;
  document.getElementById('proj-stat-approved').textContent = approved;
  document.getElementById('proj-stat-pending').textContent  = pending;
  document.getElementById('proj-stat-rejected').textContent = rejected;

  renderProjectsTable(_projAll);
}

function filterProjects() {
  const q = document.getElementById('proj-search').value.toLowerCase();
  renderProjectsTable(q ? _projAll.filter(p => (p.name||'').toLowerCase().includes(q) || (p.company||'').toLowerCase().includes(q)) : _projAll);
}

function renderProjectsTable(rows) {
  const tbody = document.getElementById('proj-tbody');
  const empty = document.getElementById('proj-empty');
  const footer = document.getElementById('proj-footer');
  const badge = document.getElementById('proj-count-badge');
  if (badge) badge.textContent = rows.length + ' submitted';
  if (!rows.length) {
    tbody.innerHTML = '';
    empty.style.display = 'block';
    footer.textContent = '';
    return;
  }
  empty.style.display = 'none';
  const statusStyle = {
    Approved: 'background:#dcfce7;color:#16a34a',
    Pending:  'background:#fef3c7;color:#d97706',
    Rejected: 'background:#fee2e2;color:#dc2626'
  };
  tbody.innerHTML = rows.map(p => `
    <tr style="border-bottom:1px solid #f3f4f6" onmouseover="this.style.background='#f9fafb'" onmouseout="this.style.background=''">
      <td style="padding:12px 16px;font-size:14px;font-weight:600;color:var(--text1)">${p.name||'-'}</td>
      <td style="padding:12px 16px;font-size:13px;color:#374151">${p.company||'-'}</td>
      <td style="padding:12px 16px;font-size:13px;color:#6b7280">${p.genre||'-'}</td>
      <td style="padding:12px 16px;font-size:13px;color:#6b7280">${p.platform||'-'}</td>
      <td style="padding:12px 16px">
        <span style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px;${statusStyle[p.status]||'background:#f3f4f6;color:#6b7280'}">${p.status||'-'}</span>
      </td>
      <td style="padding:12px 16px;text-align:right">
        <button style="border:none;background:none;cursor:pointer;color:#9ca3af;font-size:13px;padding:4px 8px;border-radius:4px" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='none'" onclick="showToast('Project details coming soon')">⋯</button>
      </td>
    </tr>`).join('');
  const approved = rows.filter(r => r.status==='Approved').length;
  const pending  = rows.filter(r => r.status==='Pending').length;
  footer.textContent = `Showing ${rows.length} projects · ${approved} approved · ${pending} pending`;
}

function exportProjectsCSV() {
  if (!_projAll.length) return;
  const header = 'Project,Company,Genre,Platform,Status';
  const rows = _projAll.map(p => [p.name,p.company,p.genre,p.platform,p.status].map(v=>`"${(v||'').replace(/"/g,'""')}"`).join(','));
  const blob = new Blob([header+'\\n'+rows.join('\\n')], {type:'text/csv'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
  a.download = 'projects.csv'; a.click();
}
'''

# ─────────────────────────────────────────────────────────────────────────────
# PREVIEW JS  (upgraded)
# ─────────────────────────────────────────────────────────────────────────────
NEW_PREVIEW_JS = '''function showPreview() {
  hideAllViews();
  const el = document.getElementById('viewPreview');
  if (!el) return;
  el.style.display = 'block';
  const ev = currentEvent || {};
  const name = ev.name || 'Untitled Event';
  document.getElementById('prev-title').textContent = name;
  const start = ev.startDate || '';
  const end   = ev.endDate   || '';
  const city  = ev.city      || '';
  const venue = ev.venue     || '';
  document.getElementById('prev-meta-date').textContent   = '📅 ' + (start ? (end && end !== start ? start + ' – ' + end : start) : 'Date TBD');
  document.getElementById('prev-meta-city').textContent   = '📍 ' + (city || 'City TBD');
  document.getElementById('prev-meta-venue').textContent  = '🏛 ' + (venue || 'Venue TBD');
  document.getElementById('prev-meta-format').textContent = '🎯 ' + (ev.format || 'In-Person');
  document.getElementById('prev-desc').textContent = ev.description || 'No description yet. Add one in Event Info.';
  document.getElementById('prev-detail-date').textContent    = start ? (end && end !== start ? start + ' – ' + end : start) : 'TBD';
  document.getElementById('prev-detail-venue').textContent   = (city && venue) ? venue + ', ' + city : (city || venue || 'TBD');
  document.getElementById('prev-detail-format').textContent  = ev.format || 'In-Person';
  document.getElementById('prev-detail-website').textContent = ev.website || '—';
  document.getElementById('prev-detail-contact').textContent = ev.contactEmail || '—';
  document.getElementById('prev-website-short').textContent  = ev.website ? '🔗' : '—';
  // Status badge
  const badge = document.getElementById('prev-status-badge');
  if (badge) {
    const isLive = ev.status === 'live';
    badge.textContent = isLive ? '● Live' : '● Draft';
    badge.style.background = isLive ? 'rgba(22,163,74,.8)' : 'rgba(255,255,255,.15)';
  }
  // Attendees count
  const regs = (() => { try { return JSON.parse(localStorage.getItem('gc_registrations') || '[]'); } catch(e){ return []; } })();
  document.getElementById('prev-attendees').textContent = regs.filter(r => r.eventTitle === name).length || 0;
  // Active modules
  document.getElementById('prev-modules').textContent = (ev.modules || []).filter(m => m.enabled).length || 0;
  // Days to event
  if (start) {
    const diff = Math.ceil((new Date(start) - new Date()) / 86400000);
    document.getElementById('prev-days').textContent = diff > 0 ? diff : 0;
  } else {
    document.getElementById('prev-days').textContent = '—';
  }
}
'''

# ─────────────────────────────────────────────────────────────────────────────
# PERFORM REPLACEMENTS
# ─────────────────────────────────────────────────────────────────────────────

def replace_view(html, view_id, new_content, next_view_comment):
    """Replace a VIEW block from its comment to the next VIEW comment."""
    start_marker = f'<!-- ══ VIEW: {view_id} ══ -->'
    end_marker   = f'<!-- ══ VIEW: {next_view_comment} ══ -->'
    start = html.find(start_marker)
    end   = html.find(end_marker)
    if start == -1 or end == -1:
        print(f'WARNING: Could not find markers for {view_id}')
        return html
    return html[:start] + new_content + html[end:]

# Replace HTML panels
html = replace_view(html, 'Attendees',   NEW_ATTENDEES,   'Projects')
html = replace_view(html, 'Projects',    NEW_PROJECTS,    'Free Ticket')
html = replace_view(html, 'Free Ticket', NEW_FREE_TICKET, 'Paid Ticket')
html = replace_view(html, 'Paid Ticket', NEW_PAID_TICKET, 'Free Pod')
html = replace_view(html, 'Preview',     NEW_PREVIEW,     'Registration')

# Replace JS: Attendees
old_att_js_start = '// ── Attendees ────────────────────────────────────────────────────────────────'
old_att_js_end   = '// ── Registration ────────────────────────────────────────────────────────────────'
si = html.find(old_att_js_start)
ei = html.find(old_att_js_end)
if si != -1 and ei != -1:
    html = html[:si] + NEW_ATTENDEES_JS + '\n' + html[ei:]
else:
    print('WARNING: Could not find Attendees JS block')

# Replace JS: Projects
old_proj_start = '// ── Projects ────────────────────────────────────────────────────────────────────────────────'
old_proj_end   = 'function showPreview()'
si = html.find(old_proj_start)
ei = html.find(old_proj_end)
if si != -1 and ei != -1:
    html = html[:si] + NEW_PROJECTS_JS + '\n' + html[ei:]
else:
    print('WARNING: Could not find Projects JS block')

# Replace JS: showPreview
old_prev_start = 'function showPreview()'
old_prev_end   = 'function showPanelSession()'
si = html.find(old_prev_start)
ei = html.find(old_prev_end)
if si != -1 and ei != -1:
    html = html[:si] + NEW_PREVIEW_JS + '\n' + html[ei:]
else:
    print('WARNING: Could not find showPreview JS block')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. File updated.')
