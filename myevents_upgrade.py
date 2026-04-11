with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

# Upgrade the event row template in renderEventsList
old_row = '''    return `<div class="event-row" onclick="openEvent(${idx})">
      ${thumb}
      <div class="event-info">
        <div class="event-name">${ev.name || 'Untitled Event'}</div>
        <div class="event-meta">${meta || 'No date set'}</div>
        <div style="display:flex;gap:10px;margin-top:4px">
          <span style="font-size:11px;color:#6b7280">👥 ${attCount} attendees</span>
          <span style="font-size:11px;color:#6b7280">🎮 ${projCount} projects</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-right:8px">${miniChart}<span style="font-size:11px;color:#6b7280">Revenue</span></div>
      <div class="event-badges">${statusBadge}</div>
      <div class="event-actions" onclick="event.stopPropagation()">
        <button class="action-btn primary" onclick="openEvent(${idx})">Edit</button>
        <button class="action-btn" onclick="previewEventFromList(${idx})">👁</button>
        <button class="action-btn" onclick="duplicateEvent(${idx})">📋</button>
        <button class="action-btn" onclick="deleteEvent(${idx})">🗑</button>
      </div>
    </div>`;'''

new_row = '''    const revenue = ev.revenue ? 'EUR ' + ev.revenue.toLocaleString() : 'EUR 0';
    const modules = ev.modules ? ev.modules.filter(m => m.enabled).length : 0;
    return `<div class="event-row" onclick="openEvent(${idx})">
      ${thumb}
      <div class="event-info">
        <div class="event-name">${ev.name || 'Untitled Event'}</div>
        <div class="event-meta">${meta || 'No date set'}</div>
        <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
          <span style="font-size:10px;background:#eff6ff;color:#2563eb;padding:2px 8px;border-radius:10px;font-weight:600">👥 ${attCount} reg</span>
          <span style="font-size:10px;background:#f0fdf4;color:#166534;padding:2px 8px;border-radius:10px;font-weight:600">💰 ${revenue}</span>
          <span style="font-size:10px;background:#faf5ff;color:#7c3aed;padding:2px 8px;border-radius:10px;font-weight:600">🧩 ${modules} modules</span>
          <span style="font-size:10px;background:#fff7ed;color:#c2410c;padding:2px 8px;border-radius:10px;font-weight:600">🎮 ${projCount} projects</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-right:8px">${miniChart}<span style="font-size:11px;color:#6b7280">Trend</span></div>
      <div class="event-badges">${statusBadge}</div>
      <div class="event-actions" onclick="event.stopPropagation()">
        <button class="action-btn primary" onclick="openEvent(${idx})">Edit</button>
        <button class="action-btn" onclick="previewEventFromList(${idx})" title="Preview">👁</button>
        <button class="action-btn" onclick="duplicateEvent(${idx})" title="Duplicate">📋</button>
        <button class="action-btn" onclick="archiveEvent(${idx})" title="Archive">📦</button>
        <button class="action-btn" onclick="deleteEvent(${idx})" title="Delete">🗑</button>
      </div>
    </div>`;'''

if old_row in content:
    content = content.replace(old_row, new_row, 1)
    print("OK: renderEventsList row upgraded")
else:
    print("NOT FOUND: renderEventsList row")

# Upgrade the filtered list row template too
old_row2 = '''    return `<div class="event-row" onclick="openEvent(${origIdx})">
      ${thumb}
      <div class="event-info">
        <div class="event-name">${ev.name || 'Untitled Event'}</div>
        <div class="event-meta">${meta || 'No date set'}</div>
        <div style="display:flex;gap:10px;margin-top:4px">
          <span style="font-size:11px;color:#6b7280">👥 ${attCount} attendees</span>
          <span style="font-size:11px;color:#6b7280">🎮 ${projCount} projects</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-right:8px">${miniChart}<span style="font-size:11px;color:#6b7280">Revenue</span></div>
      <div class="event-badges">${statusBadge}</div>
      <div class="event-actions" onclick="event.stopPropagation()">
        <button class="action-btn primary" onclick="openEvent(${origIdx})">Edit</button>
        <button class="action-btn" onclick="previewEventFromList(${origIdx})">👁</button>
        <button class="action-btn" onclick="duplicateEvent(${origIdx})">📋</button>
        <button class="action-btn" onclick="deleteEvent(${origIdx})">🗑</button>
      </div>
    </div>`;'''

new_row2 = '''    const revenue2 = ev.revenue ? 'EUR ' + ev.revenue.toLocaleString() : 'EUR 0';
    const modules2 = ev.modules ? ev.modules.filter(m => m.enabled).length : 0;
    return `<div class="event-row" onclick="openEvent(${origIdx})">
      ${thumb}
      <div class="event-info">
        <div class="event-name">${ev.name || 'Untitled Event'}</div>
        <div class="event-meta">${meta || 'No date set'}</div>
        <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
          <span style="font-size:10px;background:#eff6ff;color:#2563eb;padding:2px 8px;border-radius:10px;font-weight:600">👥 ${attCount} reg</span>
          <span style="font-size:10px;background:#f0fdf4;color:#166534;padding:2px 8px;border-radius:10px;font-weight:600">💰 ${revenue2}</span>
          <span style="font-size:10px;background:#faf5ff;color:#7c3aed;padding:2px 8px;border-radius:10px;font-weight:600">🧩 ${modules2} modules</span>
          <span style="font-size:10px;background:#fff7ed;color:#c2410c;padding:2px 8px;border-radius:10px;font-weight:600">🎮 ${projCount} projects</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-right:8px">${miniChart}<span style="font-size:11px;color:#6b7280">Trend</span></div>
      <div class="event-badges">${statusBadge}</div>
      <div class="event-actions" onclick="event.stopPropagation()">
        <button class="action-btn primary" onclick="openEvent(${origIdx})">Edit</button>
        <button class="action-btn" onclick="previewEventFromList(${origIdx})" title="Preview">👁</button>
        <button class="action-btn" onclick="duplicateEvent(${origIdx})" title="Duplicate">📋</button>
        <button class="action-btn" onclick="archiveEvent(${origIdx})" title="Archive">📦</button>
        <button class="action-btn" onclick="deleteEvent(${origIdx})" title="Delete">🗑</button>
      </div>
    </div>`;'''

if old_row2 in content:
    content = content.replace(old_row2, new_row2, 1)
    print("OK: filterEventsByStatus row upgraded")
else:
    print("NOT FOUND: filterEventsByStatus row")

with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
    f.write(content)
