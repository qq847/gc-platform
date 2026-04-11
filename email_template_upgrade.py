with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''        <!-- Tab: Attendees -->
        <div id="reg-tab-attendees" style="display:none">'''

new_str = '''          <!-- Email Template Selector + Scheduled Send -->
          <div class="editor-card" style="margin-bottom:16px">
            <div style="font-weight:700;font-size:15px;margin-bottom:14px">📨 Email Templates & Scheduled Send</div>
            <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px">
              <div onclick="loadEmailTemplate('confirmation')" style="border:2px solid #2563eb;border-radius:8px;padding:12px;cursor:pointer;background:#eff6ff">
                <div style="font-size:16px;margin-bottom:4px">🎉</div>
                <div style="font-size:12px;font-weight:700;color:#2563eb">Registration Confirmation</div>
                <div style="font-size:10px;color:#6b7280;margin-top:2px">Sent on registration</div>
              </div>
              <div onclick="loadEmailTemplate('reminder')" style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;cursor:pointer">
                <div style="font-size:16px;margin-bottom:4px">⏰</div>
                <div style="font-size:12px;font-weight:700">Event Reminder</div>
                <div style="font-size:10px;color:#6b7280;margin-top:2px">24h before event</div>
              </div>
              <div onclick="loadEmailTemplate('checkin')" style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;cursor:pointer">
                <div style="font-size:16px;margin-bottom:4px">📍</div>
                <div style="font-size:12px;font-weight:700">Check-in Instructions</div>
                <div style="font-size:10px;color:#6b7280;margin-top:2px">Day before event</div>
              </div>
              <div onclick="loadEmailTemplate('thankyou')" style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;cursor:pointer">
                <div style="font-size:16px;margin-bottom:4px">💌</div>
                <div style="font-size:12px;font-weight:700">Thank You</div>
                <div style="font-size:10px;color:#6b7280;margin-top:2px">After event ends</div>
              </div>
              <div onclick="loadEmailTemplate('survey')" style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;cursor:pointer">
                <div style="font-size:16px;margin-bottom:4px">📋</div>
                <div style="font-size:12px;font-weight:700">Post-Event Survey</div>
                <div style="font-size:10px;color:#6b7280;margin-top:2px">2 days after event</div>
              </div>
              <div onclick="loadEmailTemplate('custom')" style="border:1px dashed #d1d5db;border-radius:8px;padding:12px;cursor:pointer;text-align:center">
                <div style="font-size:16px;margin-bottom:4px">✏️</div>
                <div style="font-size:12px;font-weight:700;color:#6b7280">Custom Template</div>
                <div style="font-size:10px;color:#9ca3af;margin-top:2px">Start from scratch</div>
              </div>
            </div>
            <!-- Scheduled Send -->
            <div style="border-top:1px solid #e5e7eb;padding-top:14px">
              <div style="font-size:13px;font-weight:600;margin-bottom:10px">Scheduled Send</div>
              <div style="display:flex;gap:10px;align-items:flex-end">
                <div style="flex:1">
                  <div style="font-size:12px;color:#6b7280;margin-bottom:4px">Send Date</div>
                  <input type="date" class="form-input" id="email-sched-date" onchange="markDirty()">
                </div>
                <div style="flex:1">
                  <div style="font-size:12px;color:#6b7280;margin-bottom:4px">Send Time</div>
                  <input type="time" class="form-input" id="email-sched-time" value="09:00" onchange="markDirty()">
                </div>
                <div style="flex:1">
                  <div style="font-size:12px;color:#6b7280;margin-bottom:4px">Recipients</div>
                  <select class="form-input" onchange="markDirty()">
                    <option>All Registered (398)</option>
                    <option>Confirmed Only (247)</option>
                    <option>Not Checked In (151)</option>
                    <option>VIP Group (12)</option>
                  </select>
                </div>
                <div style="display:flex;gap:6px">
                  <button onclick="showToast('Test email sent to events@game-connection.com')" class="btn-secondary" style="font-size:12px;padding:8px 12px;white-space:nowrap">Send Test</button>
                  <button onclick="scheduleEmailSend()" class="btn-primary" style="font-size:12px;padding:8px 12px;white-space:nowrap">Schedule</button>
                </div>
              </div>
              <div id="email-sched-status" style="margin-top:8px;font-size:12px;color:#6b7280"></div>
            </div>
          </div>

        <!-- Tab: Attendees -->
        <div id="reg-tab-attendees" style="display:none">'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Email template selector inserted")
else:
    print("NOT FOUND")
