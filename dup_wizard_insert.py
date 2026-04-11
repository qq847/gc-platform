with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

# 1. Replace duplicateEvent function with wizard launcher
old_func = '''function duplicateEvent(idx) {
  const events = loadEvents();
  const copy = { ...events[idx], id: 'ev-' + Date.now(), name: (events[idx].name || 'Untitled') + ' (Copy)', status: 'draft' };
  events.splice(idx + 1, 0, copy);
  saveEvents(events);
  renderEventsList();
  showToast('Event duplicated');
}'''

new_func = '''function duplicateEvent(idx) {
  const events = loadEvents();
  const ev = events[idx] || {};
  window._dupSourceIdx = idx;
  window._dupSourceName = ev.name || 'Untitled';
  const modal = document.getElementById('dup-wizard-modal');
  if (!modal) { showToast('Wizard loading...'); return; }
  const nameInput = document.getElementById('dup-new-name');
  if (nameInput) nameInput.value = (ev.name || 'Untitled') + ' (Copy)';
  showDupStep(1);
  modal.style.display = 'flex';
}
function showDupStep(step) {
  [1,2,3].forEach(s => {
    const el = document.getElementById('dup-step-' + s);
    if (el) el.style.display = s === step ? 'block' : 'none';
    const dot = document.getElementById('dup-dot-' + s);
    if (dot) { dot.style.background = s <= step ? '#2563eb' : '#e5e7eb'; dot.style.color = s <= step ? '#fff' : '#9ca3af'; }
  });
  window._dupCurrentStep = step;
}
function dupNext() {
  const cur = window._dupCurrentStep || 1;
  if (cur === 2) {
    const name = document.getElementById('dup-new-name')?.value || 'Untitled Copy';
    const date = document.getElementById('dup-new-date')?.value || 'Not set';
    const city = document.getElementById('dup-new-city')?.value || 'Not set';
    const mods = [];
    ['dup-mod-tickets','dup-mod-booths','dup-mod-speakers','dup-mod-sponsors','dup-mod-sessions','dup-mod-agenda'].forEach(id => {
      const cb = document.getElementById(id);
      if (cb && cb.checked) mods.push(cb.dataset.label);
    });
    const cn = document.getElementById('dup-confirm-name'); if (cn) cn.textContent = name;
    const cd = document.getElementById('dup-confirm-date'); if (cd) cd.textContent = date;
    const cc = document.getElementById('dup-confirm-city'); if (cc) cc.textContent = city;
    const cm = document.getElementById('dup-confirm-modules'); if (cm) cm.textContent = mods.length ? mods.join(', ') : 'None selected';
  }
  if (cur < 3) showDupStep(cur + 1);
}
function dupBack() {
  const cur = window._dupCurrentStep || 1;
  if (cur > 1) showDupStep(cur - 1);
}
function confirmDuplicate() {
  const events = loadEvents();
  const idx = window._dupSourceIdx;
  const ev = events[idx] || {};
  const newName = document.getElementById('dup-new-name')?.value || (ev.name + ' (Copy)');
  const newDate = document.getElementById('dup-new-date')?.value || '';
  const newCity = document.getElementById('dup-new-city')?.value || '';
  const modules = [];
  ['dup-mod-tickets','dup-mod-booths','dup-mod-speakers','dup-mod-sponsors','dup-mod-sessions','dup-mod-agenda'].forEach(id => {
    const cb = document.getElementById(id);
    if (cb && cb.checked) modules.push(cb.dataset.label);
  });
  const copy = { ...ev, id: 'ev-' + Date.now(), name: newName, status: 'draft', city: newCity || ev.city, startDate: newDate || ev.startDate };
  events.splice(idx + 1, 0, copy);
  saveEvents(events);
  renderEventsList();
  closeDupWizard();
  showToast('\u2705 "' + newName + '" created with ' + modules.length + ' modules');
}
function closeDupWizard() {
  const modal = document.getElementById('dup-wizard-modal');
  if (modal) modal.style.display = 'none';
}'''

if old_func in content:
    content = content.replace(old_func, new_func, 1)
    print("OK: duplicateEvent upgraded")
else:
    print("NOT FOUND: duplicateEvent")

# 2. Add wizard modal before </body>
wizard_html = '''
  <!-- Duplication Wizard Modal -->
  <div id="dup-wizard-modal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:9999;align-items:center;justify-content:center">
    <div style="background:#fff;border-radius:16px;width:520px;max-width:95vw;box-shadow:0 20px 60px rgba(0,0,0,.3);overflow:hidden">
      <div style="background:linear-gradient(135deg,#1e40af,#2563eb);padding:20px 24px;color:#fff;display:flex;justify-content:space-between;align-items:center">
        <div><div style="font-size:16px;font-weight:700">Duplicate Event Wizard</div><div style="font-size:12px;opacity:.8;margin-top:2px">Create a new event from an existing one</div></div>
        <button onclick="closeDupWizard()" style="background:rgba(255,255,255,.2);border:none;border-radius:50%;width:28px;height:28px;color:#fff;cursor:pointer;font-size:16px">x</button>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;gap:0;padding:16px 24px;border-bottom:1px solid #e5e7eb">
        <div id="dup-dot-1" style="width:28px;height:28px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700">1</div>
        <div style="width:60px;height:2px;background:#e5e7eb"></div>
        <div id="dup-dot-2" style="width:28px;height:28px;border-radius:50%;background:#e5e7eb;color:#9ca3af;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700">2</div>
        <div style="width:60px;height:2px;background:#e5e7eb"></div>
        <div id="dup-dot-3" style="width:28px;height:28px;border-radius:50%;background:#e5e7eb;color:#9ca3af;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700">3</div>
      </div>
      <div id="dup-step-1" style="padding:24px">
        <div style="font-size:14px;font-weight:700;margin-bottom:16px">Step 1: Basic Information</div>
        <div style="margin-bottom:14px"><div style="font-size:11px;color:#6b7280;margin-bottom:4px">New Event Name</div><input id="dup-new-name" type="text" style="width:100%;border:1px solid #e5e7eb;border-radius:8px;padding:9px 12px;font-size:13px;box-sizing:border-box" placeholder="e.g. Game Connection 2026"></div>
        <div style="display:flex;gap:12px">
          <div style="flex:1"><div style="font-size:11px;color:#6b7280;margin-bottom:4px">New Start Date</div><input id="dup-new-date" type="date" style="width:100%;border:1px solid #e5e7eb;border-radius:8px;padding:9px 12px;font-size:13px"></div>
          <div style="flex:1"><div style="font-size:11px;color:#6b7280;margin-bottom:4px">New City</div><input id="dup-new-city" type="text" style="width:100%;border:1px solid #e5e7eb;border-radius:8px;padding:9px 12px;font-size:13px" placeholder="e.g. Lyon"></div>
        </div>
        <div style="display:flex;justify-content:flex-end;margin-top:20px"><button onclick="dupNext()" class="btn-primary" style="font-size:13px;padding:9px 20px">Next</button></div>
      </div>
      <div id="dup-step-2" style="display:none;padding:24px">
        <div style="font-size:14px;font-weight:700;margin-bottom:4px">Step 2: Select Modules to Copy</div>
        <div style="font-size:12px;color:#6b7280;margin-bottom:16px">Choose which content to carry over</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-tickets" type="checkbox" checked data-label="Tickets" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Tickets</div><div style="font-size:11px;color:#9ca3af">Types and pricing</div></div></label>
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-booths" type="checkbox" checked data-label="Booths and Pods" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Booths and Pods</div><div style="font-size:11px;color:#9ca3af">Layout and pricing</div></div></label>
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-speakers" type="checkbox" data-label="Speakers" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Speakers</div><div style="font-size:11px;color:#9ca3af">Bios and topics</div></div></label>
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-sponsors" type="checkbox" data-label="Sponsors" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Sponsors</div><div style="font-size:11px;color:#9ca3af">Tiers and contacts</div></div></label>
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-sessions" type="checkbox" data-label="Sessions" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Sessions</div><div style="font-size:11px;color:#9ca3af">Panel and track structure</div></div></label>
          <label style="display:flex;align-items:center;gap:10px;padding:12px;border:1px solid #e5e7eb;border-radius:8px;cursor:pointer"><input id="dup-mod-agenda" type="checkbox" data-label="Agenda" style="width:16px;height:16px;accent-color:#2563eb"><div><div style="font-size:13px;font-weight:600">Agenda</div><div style="font-size:11px;color:#9ca3af">Schedule and timeslots</div></div></label>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:20px"><button onclick="dupBack()" class="btn-secondary" style="font-size:13px;padding:9px 20px">Back</button><button onclick="dupNext()" class="btn-primary" style="font-size:13px;padding:9px 20px">Next</button></div>
      </div>
      <div id="dup-step-3" style="display:none;padding:24px">
        <div style="font-size:14px;font-weight:700;margin-bottom:16px">Step 3: Confirm and Create</div>
        <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:16px;margin-bottom:16px">
          <div style="font-size:13px;font-weight:700;color:#16a34a;margin-bottom:10px">Ready to create new event</div>
          <div style="display:flex;flex-direction:column;gap:6px;font-size:12px;color:#374151">
            <div style="display:flex;gap:8px"><span style="color:#9ca3af;min-width:80px">Name:</span><strong id="dup-confirm-name">-</strong></div>
            <div style="display:flex;gap:8px"><span style="color:#9ca3af;min-width:80px">Start Date:</span><strong id="dup-confirm-date">-</strong></div>
            <div style="display:flex;gap:8px"><span style="color:#9ca3af;min-width:80px">City:</span><strong id="dup-confirm-city">-</strong></div>
            <div style="display:flex;gap:8px"><span style="color:#9ca3af;min-width:80px">Modules:</span><strong id="dup-confirm-modules">-</strong></div>
          </div>
        </div>
        <div style="font-size:12px;color:#9ca3af;margin-bottom:16px">The new event will be created as a Draft. All copied content will be reset to pending state.</div>
        <div style="display:flex;justify-content:space-between"><button onclick="dupBack()" class="btn-secondary" style="font-size:13px;padding:9px 20px">Back</button><button onclick="confirmDuplicate()" style="font-size:13px;padding:9px 20px;background:#16a34a;color:#fff;border:none;border-radius:8px;cursor:pointer;font-weight:600">Create Event</button></div>
      </div>
    </div>
  </div>
'''

if '</body>' in content:
    content = content.replace('</body>', wizard_html + '\n</body>', 1)
    print("OK: Wizard modal inserted")
else:
    print("NOT FOUND: </body>")

with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
    f.write(content)
print("File saved")
