with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''        <!-- Speaker Management -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">🎤 Speaker Management</div>'''

new_str = '''        <!-- Conflict Detection -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">⚠️ Schedule Conflict Detector</div>
            <button class="btn-secondary" style="font-size:12px;padding:6px 12px" onclick="runConflictCheck()">🔍 Run Check</button>
          </div>
          <div id="conflict-results">
            <!-- Conflict 1: Speaker double-booked -->
            <div style="background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:12px;margin-bottom:10px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px">🔴</span>
                  <div>
                    <div style="font-size:13px;font-weight:700;color:#dc2626">Speaker Double-Booking</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">Sarah Kim is scheduled in <strong>Business Track 10:00</strong> and <strong>Indie Track 10:00</strong> simultaneously</div>
                    <div style="font-size:11px;color:#9ca3af;margin-top:4px">Day 1 · 10:00–10:45</div>
                  </div>
                </div>
                <button onclick="resolveConflict(this,'sk-double')" class="btn-secondary" style="font-size:11px;padding:4px 10px;white-space:nowrap;color:#dc2626;border-color:#fecaca">Resolve</button>
              </div>
              <div style="margin-top:8px;padding:8px;background:#fff;border-radius:6px;border:1px solid #fecaca">
                <div style="font-size:11px;font-weight:600;color:#6b7280;margin-bottom:4px">Suggested Fix:</div>
                <div style="font-size:11px;color:#374151">Move "Funding Your Indie Game" to 11:00 in Indie Track (currently free)</div>
              </div>
            </div>
            <!-- Conflict 2: Room capacity -->
            <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px;margin-bottom:10px">
              <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div style="display:flex;gap:10px;align-items:flex-start">
                  <span style="font-size:16px">🟡</span>
                  <div>
                    <div style="font-size:13px;font-weight:700;color:#d97706">Room Capacity Warning</div>
                    <div style="font-size:12px;color:#6b7280;margin-top:2px">"Opening Keynote" in Hall A (cap: 200) has 312 RSVPs — 56% over capacity</div>
                    <div style="font-size:11px;color:#9ca3af;margin-top:4px">Day 1 · 09:00–09:45</div>
                  </div>
                </div>
                <button onclick="resolveConflict(this,'cap-keynote')" class="btn-secondary" style="font-size:11px;padding:4px 10px;white-space:nowrap;color:#d97706;border-color:#fde68a">Resolve</button>
              </div>
              <div style="margin-top:8px;padding:8px;background:#fff;border-radius:6px;border:1px solid #fde68a">
                <div style="font-size:11px;font-weight:600;color:#6b7280;margin-bottom:4px">Suggested Fix:</div>
                <div style="font-size:11px;color:#374151">Move to Main Stage (cap: 800) or add overflow room with live stream</div>
              </div>
            </div>
            <!-- No more conflicts -->
            <div id="conflict-clear" style="display:none;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:12px;text-align:center">
              <span style="font-size:16px">✅</span>
              <span style="font-size:13px;font-weight:600;color:#16a34a;margin-left:8px">No schedule conflicts detected</span>
            </div>
          </div>
          <div style="margin-top:10px;display:flex;gap:8px">
            <div style="flex:1;background:#fef2f2;border-radius:6px;padding:8px;text-align:center">
              <div style="font-size:18px;font-weight:800;color:#dc2626">1</div>
              <div style="font-size:10px;color:#6b7280">Critical</div>
            </div>
            <div style="flex:1;background:#fffbeb;border-radius:6px;padding:8px;text-align:center">
              <div style="font-size:18px;font-weight:800;color:#d97706">1</div>
              <div style="font-size:10px;color:#6b7280">Warnings</div>
            </div>
            <div style="flex:1;background:#f0fdf4;border-radius:6px;padding:8px;text-align:center">
              <div style="font-size:18px;font-weight:800;color:#16a34a">18</div>
              <div style="font-size:10px;color:#6b7280">OK</div>
            </div>
          </div>
        </div>

        <!-- Speaker Management -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">🎤 Speaker Management</div>'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Conflict detector inserted")
else:
    print("NOT FOUND")
