with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>
      <!-- ══ VIEW: Projects ══ -->'''

new_str = '''        <!-- Attendee Import / Export -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">📂 Import / Export Attendees</div>
          </div>
          <!-- Export section -->
          <div style="margin-bottom:16px">
            <div style="font-size:13px;font-weight:600;margin-bottom:8px">Export</div>
            <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:8px">
              <div style="flex:1;min-width:130px">
                <div style="font-size:11px;color:#6b7280;margin-bottom:3px">Filter by Ticket Type</div>
                <select style="width:100%;border:1px solid #e5e7eb;border-radius:6px;padding:6px 8px;font-size:12px;background:#fff">
                  <option selected>All Tickets</option>
                  <option>VIP Pass</option>
                  <option>Standard</option>
                  <option>Press</option>
                </select>
              </div>
              <div style="flex:1;min-width:130px">
                <div style="font-size:11px;color:#6b7280;margin-bottom:3px">Filter by Check-in</div>
                <select style="width:100%;border:1px solid #e5e7eb;border-radius:6px;padding:6px 8px;font-size:12px;background:#fff">
                  <option selected>All Attendees</option>
                  <option>Checked In</option>
                  <option>Not Checked In</option>
                </select>
              </div>
              <div style="flex:1;min-width:130px">
                <div style="font-size:11px;color:#6b7280;margin-bottom:3px">Format</div>
                <select style="width:100%;border:1px solid #e5e7eb;border-radius:6px;padding:6px 8px;font-size:12px;background:#fff">
                  <option selected>CSV</option>
                  <option>Excel (.xlsx)</option>
                  <option>JSON</option>
                </select>
              </div>
            </div>
            <button onclick="exportAttendeesCSV()" class="btn-primary" style="font-size:12px;padding:7px 16px">⬇ Export Now</button>
          </div>
          <hr style="border:none;border-top:1px solid #e5e7eb;margin-bottom:16px">
          <!-- Import section -->
          <div>
            <div style="font-size:13px;font-weight:600;margin-bottom:8px">Import</div>
            <div style="border:2px dashed #d1d5db;border-radius:8px;padding:20px;text-align:center;background:#f9fafb;margin-bottom:10px" id="att-drop-zone">
              <div style="font-size:24px;margin-bottom:6px">📄</div>
              <div style="font-size:13px;font-weight:600;color:#374151;margin-bottom:2px">Drop CSV file here</div>
              <div style="font-size:11px;color:#9ca3af;margin-bottom:10px">or click to browse — max 5MB</div>
              <button onclick="simulateAttendeeImport()" class="btn-secondary" style="font-size:12px;padding:6px 14px">Browse File</button>
            </div>
            <!-- Import validation result -->
            <div id="att-import-result" style="display:none">
              <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:12px;margin-bottom:8px">
                <div style="font-size:13px;font-weight:700;color:#16a34a;margin-bottom:6px">✓ File validated — ready to import</div>
                <div style="display:flex;gap:16px;font-size:12px;color:#374151">
                  <span>📊 <strong>247</strong> rows detected</span>
                  <span>✅ <strong>241</strong> valid</span>
                  <span>⚠️ <strong>6</strong> warnings</span>
                  <span>❌ <strong>0</strong> errors</span>
                </div>
              </div>
              <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:10px;margin-bottom:10px">
                <div style="font-size:12px;font-weight:600;color:#d97706;margin-bottom:4px">⚠️ 6 Warnings (rows will be imported with defaults)</div>
                <div style="font-size:11px;color:#6b7280">Row 34: Missing phone number — will use blank<br>Row 89: Duplicate email (john.doe@example.com) — will skip<br>Row 112: Invalid ticket type "VVIP" — defaulting to Standard<br>Row 156, 178, 203: Missing company name — will use blank</div>
              </div>
              <div style="display:flex;gap:8px">
                <button onclick="confirmAttendeeImport()" class="btn-primary" style="font-size:12px;padding:7px 14px">Import 241 Attendees</button>
                <button onclick="document.getElementById('att-import-result').style.display='none'" class="btn-secondary" style="font-size:12px;padding:7px 14px">Cancel</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- ══ VIEW: Projects ══ -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Attendee import/export inserted")
else:
    idx = content.find('<!-- ══ VIEW: Projects ══ -->')
    print(f"Projects found at: {idx}")
    print(repr(content[idx-80:idx+20]))
