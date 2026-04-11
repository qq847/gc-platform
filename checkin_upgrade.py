with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''            <div style="flex:1">
              <div style="font-size:13px;font-weight:600;margin-bottom:8px">Simulate Check-in</div>
              <div style="display:flex;gap:8px;margin-bottom:10px">
                <input type="text" id="qr-sim-input" class="form-input" placeholder="Enter attendee name or email" style="flex:1">
                <button class="btn-primary" style="font-size:12px;padding:8px 14px" onclick="simulateCheckin()">Check In</button>
              </div>
              <div id="qr-sim-result" style="font-size:13px;color:#6b7280">Scan or type to check in an attendee</div>
              <div style="margin-top:12px;padding:10px;background:#f0fdf4;border-radius:8px;border:1px solid #bbf7d0">
                <div style="font-size:12px;color:#166534">✅ <strong>Live check-in:</strong> In production, this connects to the mobile scanner app. Attendees scan their QR badge at entry gates for instant check-in.</div>
              </div>
            </div>'''

new_str = '''            <div style="flex:1">
              <div style="font-size:13px;font-weight:600;margin-bottom:8px">Simulate Check-in</div>
              <div style="display:flex;gap:8px;margin-bottom:10px">
                <input type="text" id="qr-sim-input" class="form-input" placeholder="Enter attendee name or email" style="flex:1">
                <button class="btn-primary" style="font-size:12px;padding:8px 14px" onclick="simulateCheckin()">Check In</button>
              </div>
              <div id="qr-sim-result" style="font-size:13px;color:#6b7280;min-height:22px">Scan or type to check in an attendee</div>
              <!-- Live counter -->
              <div style="display:flex;gap:12px;margin-top:12px">
                <div style="flex:1;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:10px;text-align:center">
                  <div id="ci-counter" style="font-size:22px;font-weight:800;color:#16a34a">247</div>
                  <div style="font-size:11px;color:#166534">Checked In</div>
                </div>
                <div style="flex:1;background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:10px;text-align:center">
                  <div id="ci-pending" style="font-size:22px;font-weight:800;color:#d97706">151</div>
                  <div style="font-size:11px;color:#92400e">Pending</div>
                </div>
                <div style="flex:1;background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:10px;text-align:center">
                  <div id="ci-rate" style="font-size:22px;font-weight:800;color:#2563eb">62%</div>
                  <div style="font-size:11px;color:#1e40af">Rate</div>
                </div>
              </div>
              <!-- Batch check-in -->
              <div style="margin-top:12px;display:flex;gap:8px">
                <button onclick="batchCheckin('vip')" class="btn-secondary" style="font-size:11px;padding:5px 12px">Check-in VIPs (12)</button>
                <button onclick="batchCheckin('press')" class="btn-secondary" style="font-size:11px;padding:5px 12px">Check-in Press (8)</button>
                <button onclick="batchCheckin('all')" style="font-size:11px;padding:5px 12px;background:#16a34a;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600">Batch All Pending</button>
              </div>
              <div style="margin-top:10px;padding:10px;background:#f0fdf4;border-radius:8px;border:1px solid #bbf7d0">
                <div style="font-size:12px;color:#166534">✅ <strong>Live check-in:</strong> In production, this connects to the mobile scanner app. Attendees scan their QR badge at entry gates for instant check-in.</div>
              </div>
            </div>'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Check-in simulator upgraded")
else:
    print("NOT FOUND")
