with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
            <div style="font-weight:700;font-size:14px">📋 Pre-publish Checklist</div>
            <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="runPublishChecklist()">Run Check</button>
          </div>
          <div id="checklist-items" style="display:flex;flex-direction:column;gap:6px">
            <div id="chk-name" style="display:flex;align-items:center;gap:8px;font-size:12px">
              <span id="chk-name-icon" style="font-size:14px">⏳</span>
              <span>Event name filled in</span>
            </div>
            <div id="chk-date" style="display:flex;align-items:center;gap:8px;font-size:12px">
              <span id="chk-date-icon" style="font-size:14px">⏳</span>
              <span>Start date set</span>
            </div>
            <div id="chk-city" style="display:flex;align-items:center;gap:8px;font-size:12px">
              <span id="chk-city-icon" style="font-size:14px">⏳</span>
              <span>City / Location specified</span>
            </div>
            <div id="chk-cover" style="display:flex;align-items:center;gap:8px;font-size:12px">
              <span id="chk-cover-icon" style="font-size:14px">⏳</span>
              <span>Cover image uploaded</span>
            </div>
            <div id="chk-module" style="display:flex;align-items:center;gap:8px;font-size:12px">
              <span id="chk-module-icon" style="font-size:14px">⏳</span>
              <span>At least 1 module enabled</span>
            </div>
          </div>
          <div id="checklist-summary" style="margin-top:10px;font-size:12px;color:#6b7280">Click "Run Check" to validate before publishing.</div>'''

new_str = '''          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
            <div style="font-weight:700;font-size:14px">📋 Pre-publish Checklist</div>
            <div style="display:flex;gap:6px">
              <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="autoFixChecklist()">Auto-fix</button>
              <button class="btn-secondary" style="font-size:11px;padding:4px 10px" onclick="runPublishChecklist()">Run Check</button>
            </div>
          </div>
          <div id="checklist-items" style="display:flex;flex-direction:column;gap:6px">
            <div id="chk-name" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-name-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">Event name filled in</span>
              <span id="chk-name-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
            <div id="chk-date" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-date-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">Start date set</span>
              <span id="chk-date-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
            <div id="chk-city" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-city-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">City / Location specified</span>
              <span id="chk-city-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
            <div id="chk-cover" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-cover-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">Cover image uploaded</span>
              <span id="chk-cover-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#fef3c7;color:#92400e">Warning</span>
            </div>
            <div id="chk-module" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-module-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">At least 1 module enabled</span>
              <span id="chk-module-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
            <div id="chk-desc" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-desc-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">Event description added</span>
              <span id="chk-desc-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
            <div id="chk-reg" style="display:flex;align-items:center;gap:8px;font-size:12px;padding:6px 8px;border-radius:6px;background:#f9fafb">
              <span id="chk-reg-icon" style="font-size:14px">⏳</span>
              <span style="flex:1">Registration module configured</span>
              <span id="chk-reg-badge" style="font-size:10px;padding:1px 7px;border-radius:10px;background:#e5e7eb;color:#6b7280">Pending</span>
            </div>
          </div>
          <div id="checklist-summary" style="margin-top:10px;font-size:12px;color:#6b7280">Click "Run Check" to validate before publishing.</div>'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Checklist upgraded")
else:
    print("NOT FOUND")
