with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_panel = '''  <!-- Notification Panel -->
  <div id="notif-panel" style="display:none;position:fixed;top:56px;right:16px;width:340px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.15);z-index:998">
    <div style="padding:14px 16px;border-bottom:1px solid #e5e7eb;display:flex;justify-content:space-between;align-items:center">
      <div style="font-size:14px;font-weight:700">Notifications</div>
      <button onclick="markAllNotifRead()" style="border:none;background:none;cursor:pointer;font-size:12px;color:#2563eb">Mark all read</button>
    </div>
    <div id="notif-list" style="max-height:320px;overflow-y:auto">
      <div style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;background:#eff6ff">
        <span style="font-size:18px;flex-shrink:0">🎟️</span>
        <div>
          <div style="font-size:13px;font-weight:600">New ticket purchase</div>
          <div style="font-size:12px;color:#6b7280">Yuki Tanaka bought 1x Early Bird ticket</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">2 min ago</div>
        </div>
        <span style="width:8px;height:8px;background:#2563eb;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;background:#eff6ff">
        <span style="font-size:18px;flex-shrink:0">🎮</span>
        <div>
          <div style="font-size:13px;font-weight:600">New game submission</div>
          <div style="font-size:12px;color:#6b7280">"Neon Drift" submitted by Indie Studio X</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">15 min ago</div>
        </div>
        <span style="width:8px;height:8px;background:#2563eb;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6">
        <span style="font-size:18px;flex-shrink:0">🤝</span>
        <div>
          <div style="font-size:13px;font-weight:600">Meeting confirmed</div>
          <div style="font-size:12px;color:#6b7280">Ubisoft × Indie Forge confirmed for Day 1 10:30</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">1 hr ago</div>
        </div>
      </div>
      <div style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6">
        <span style="font-size:18px;flex-shrink:0">🏢</span>
        <div>
          <div style="font-size:13px;font-weight:600">Booth payment received</div>
          <div style="font-size:12px;color:#6b7280">EA Games paid €4,500 for Booth A-12</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">3 hr ago</div>
        </div>
      </div>
      <div style="display:flex;gap:10px;padding:12px 16px">
        <span style="font-size:18px;flex-shrink:0">📊</span>
        <div>
          <div style="font-size:13px;font-weight:600">Registration milestone</div>
          <div style="font-size:12px;color:#6b7280">You've reached 100 registrations! 🎉</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">Yesterday</div>
        </div>
      </div>
    </div>
  </div>'''

new_panel = '''  <!-- Notification Panel -->
  <div id="notif-panel" style="display:none;position:fixed;top:56px;right:16px;width:360px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.15);z-index:998">
    <div style="padding:14px 16px;border-bottom:1px solid #e5e7eb">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
        <div style="font-size:14px;font-weight:700">Notifications <span id="notif-unread-count" style="font-size:11px;background:#dc2626;color:#fff;padding:1px 7px;border-radius:10px;margin-left:4px">3</span></div>
        <button onclick="markAllNotifRead()" style="border:none;background:none;cursor:pointer;font-size:12px;color:#2563eb;font-weight:600">Mark all read</button>
      </div>
      <div style="display:flex;gap:4px">
        <button id="nf-all" onclick="filterNotifs('all')" style="font-size:11px;padding:3px 10px;border:none;border-radius:10px;cursor:pointer;background:#2563eb;color:#fff;font-weight:600">All</button>
        <button id="nf-unread" onclick="filterNotifs('unread')" style="font-size:11px;padding:3px 10px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Unread</button>
        <button id="nf-tickets" onclick="filterNotifs('tickets')" style="font-size:11px;padding:3px 10px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Tickets</button>
        <button id="nf-meetings" onclick="filterNotifs('meetings')" style="font-size:11px;padding:3px 10px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Meetings</button>
      </div>
    </div>
    <div id="notif-list" style="max-height:360px;overflow-y:auto">
      <div class="notif-item" data-cat="tickets" data-read="false" style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;background:#eff6ff;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">🎟️</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">New ticket purchase</div>
          <div style="font-size:12px;color:#6b7280">Yuki Tanaka bought 1x Early Bird ticket</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">2 min ago</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:#2563eb;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div class="notif-item" data-cat="games" data-read="false" style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;background:#eff6ff;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">🎮</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">New game submission</div>
          <div style="font-size:12px;color:#6b7280">"Neon Drift" submitted by Indie Studio X</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">15 min ago</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:#2563eb;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div class="notif-item" data-cat="meetings" data-read="false" style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;background:#eff6ff;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">🤝</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">Meeting confirmed</div>
          <div style="font-size:12px;color:#6b7280">Ubisoft × Indie Forge confirmed for Day 1 10:30</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">1 hr ago</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:#2563eb;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div class="notif-item" data-cat="tickets" data-read="true" style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">🏢</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">Booth payment received</div>
          <div style="font-size:12px;color:#6b7280">EA Games paid €4,500 for Booth A-12</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">3 hr ago</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:transparent;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div class="notif-item" data-cat="system" data-read="true" style="display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid #f3f4f6;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">📊</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">Registration milestone</div>
          <div style="font-size:12px;color:#6b7280">You've reached 100 registrations! 🎉</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">Yesterday</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:transparent;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
      <div class="notif-item" data-cat="meetings" data-read="true" style="display:flex;gap:10px;padding:12px 16px;cursor:pointer" onclick="markNotifRead(this)">
        <span style="font-size:18px;flex-shrink:0">📋</span>
        <div style="flex:1">
          <div style="font-size:13px;font-weight:600">Award voting opened</div>
          <div style="font-size:12px;color:#6b7280">Jurors can now submit scores for Best Indie Game</div>
          <div style="font-size:11px;color:#9ca3af;margin-top:2px">2 days ago</div>
        </div>
        <span class="notif-dot" style="width:8px;height:8px;background:transparent;border-radius:50%;flex-shrink:0;margin-top:4px"></span>
      </div>
    </div>
    <div style="padding:10px 16px;border-top:1px solid #e5e7eb;text-align:center">
      <button onclick="showToast('Notification preferences → Settings → Notifications')" style="border:none;background:none;cursor:pointer;font-size:12px;color:#6b7280">Manage notification preferences</button>
    </div>
  </div>'''

if old_panel in content:
    content = content.replace(old_panel, new_panel, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Notification panel upgraded")
else:
    print("NOT FOUND")
