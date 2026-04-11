with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>

      <!-- ══ VIEW: Panel / Session ══ -->'''

new_str = '''        <!-- Contract Signing Tracker -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">✍️ Contract Signing Tracker</div>
            <button onclick="showToast('Contract status report sent to all sponsors')" class="btn-secondary" style="font-size:12px;padding:6px 12px">Send All Status</button>
          </div>
          <!-- Contract rows -->
          <div style="display:flex;flex-direction:column;gap:10px">
            <!-- Sony - Signed -->
            <div style="border:1px solid #bbf7d0;border-radius:10px;padding:14px;background:#f0fdf4">
              <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div>
                  <div style="font-size:13px;font-weight:700">Sony Interactive Entertainment</div>
                  <div style="font-size:11px;color:#6b7280;margin-top:1px">Platinum · EUR 30,000</div>
                </div>
                <span style="font-size:11px;background:#dcfce7;color:#16a34a;padding:3px 10px;border-radius:10px;font-weight:700">✓ Signed</span>
              </div>
              <!-- Timeline steps -->
              <div style="display:flex;align-items:center;gap:0;margin-top:12px;overflow-x:auto">
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Draft Sent</div>
                  <div style="font-size:9px;color:#9ca3af">Mar 1</div>
                </div>
                <div style="flex:1;height:2px;background:#16a34a;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Reviewed</div>
                  <div style="font-size:9px;color:#9ca3af">Mar 5</div>
                </div>
                <div style="flex:1;height:2px;background:#16a34a;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Signed</div>
                  <div style="font-size:9px;color:#9ca3af">Mar 8</div>
                </div>
                <div style="flex:1;height:2px;background:#16a34a;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Paid</div>
                  <div style="font-size:9px;color:#9ca3af">Mar 15</div>
                </div>
              </div>
            </div>
            <!-- Tencent - Awaiting Signature -->
            <div style="border:1px solid #fde68a;border-radius:10px;padding:14px;background:#fffbeb">
              <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div>
                  <div style="font-size:13px;font-weight:700">Tencent Games</div>
                  <div style="font-size:11px;color:#6b7280;margin-top:1px">Gold · EUR 25,000</div>
                </div>
                <span style="font-size:11px;background:#fef3c7;color:#d97706;padding:3px 10px;border-radius:10px;font-weight:700">⏳ Awaiting Signature</span>
              </div>
              <div style="display:flex;align-items:center;gap:0;margin-top:12px;overflow-x:auto">
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Draft Sent</div>
                  <div style="font-size:9px;color:#9ca3af">Apr 1</div>
                </div>
                <div style="flex:1;height:2px;background:#16a34a;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#16a34a;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px">✓</div>
                  <div style="font-size:9px;color:#16a34a;font-weight:600;margin-top:3px;text-align:center">Reviewed</div>
                  <div style="font-size:9px;color:#9ca3af">Apr 5</div>
                </div>
                <div style="flex:1;height:2px;background:#fde68a;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#fde68a;border:2px solid #d97706;display:flex;align-items:center;justify-content:center;color:#d97706;font-size:14px;font-weight:700">?</div>
                  <div style="font-size:9px;color:#d97706;font-weight:600;margin-top:3px;text-align:center">Pending Sign</div>
                  <div style="font-size:9px;color:#9ca3af">Due Apr 15</div>
                </div>
                <div style="flex:1;height:2px;background:#e5e7eb;min-width:20px"></div>
                <div style="display:flex;flex-direction:column;align-items:center;min-width:70px">
                  <div style="width:28px;height:28px;border-radius:50%;background:#e5e7eb;display:flex;align-items:center;justify-content:center;color:#9ca3af;font-size:12px">—</div>
                  <div style="font-size:9px;color:#9ca3af;font-weight:600;margin-top:3px;text-align:center">Payment</div>
                  <div style="font-size:9px;color:#9ca3af">TBD</div>
                </div>
              </div>
              <div style="margin-top:10px;display:flex;gap:6px">
                <button onclick="showToast('Reminder email sent to Tencent Games')" class="btn-secondary" style="font-size:11px;padding:5px 12px">Send Reminder</button>
                <button onclick="showToast('Contract link copied to clipboard')" style="font-size:11px;padding:5px 12px;border:1px solid #e5e7eb;background:#fff;border-radius:6px;cursor:pointer">Copy Link</button>
              </div>
            </div>
            <!-- New prospect - Not sent yet -->
            <div style="border:1px solid #e5e7eb;border-radius:10px;padding:14px;background:#f8f9fa">
              <div style="display:flex;justify-content:space-between;align-items:flex-start">
                <div>
                  <div style="font-size:13px;font-weight:700">Bandai Namco Entertainment</div>
                  <div style="font-size:11px;color:#6b7280;margin-top:1px">Silver · EUR 10,000</div>
                </div>
                <span style="font-size:11px;background:#f3f4f6;color:#6b7280;padding:3px 10px;border-radius:10px;font-weight:700">📋 Draft Ready</span>
              </div>
              <div style="font-size:12px;color:#9ca3af;margin-top:8px;margin-bottom:8px">Contract prepared — not yet sent to sponsor</div>
              <button onclick="showToast('Contract sent to Bandai Namco')" class="btn-primary" style="font-size:11px;padding:5px 14px">Send Contract</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ══ VIEW: Panel / Session ══ -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Contract signing tracker inserted")
else:
    idx = content.find('<!-- ══ VIEW: Panel / Session ══ -->')
    print(f"Panel/Session found at: {idx}")
    print(repr(content[idx-80:idx+20]))
