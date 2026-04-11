with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''        <!-- FAQ Accordion -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="font-weight:700;font-size:15px;margin-bottom:14px">💬 Frequently Asked Questions</div>'''

new_str = '''        <!-- Video Tutorials -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="font-weight:700;font-size:15px;margin-bottom:14px">🎬 Video Tutorials</div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: Getting Started with EventHQ')">
              <div style="background:linear-gradient(135deg,#1e3a8a,#2563eb);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #2563eb;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">3:42</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">Getting Started</div>
                <div style="font-size:11px;color:#6b7280">Create your first event in 5 minutes</div>
              </div>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: Setting Up Modules')">
              <div style="background:linear-gradient(135deg,#7c3aed,#9333ea);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #7c3aed;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">5:18</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">Setting Up Modules</div>
                <div style="font-size:11px;color:#6b7280">Enable Game Showcase, Awards & more</div>
              </div>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: Managing Registrations')">
              <div style="background:linear-gradient(135deg,#065f46,#16a34a);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #065f46;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">4:55</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">Managing Registrations</div>
                <div style="font-size:11px;color:#6b7280">Import, invite & check in attendees</div>
              </div>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: Sponsorship & Revenue')">
              <div style="background:linear-gradient(135deg,#92400e,#d97706);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #92400e;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">6:10</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">Sponsorship & Revenue</div>
                <div style="font-size:11px;color:#6b7280">Track payments and deliver benefits</div>
              </div>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: Analytics Deep Dive')">
              <div style="background:linear-gradient(135deg,#1e3a5f,#0ea5e9);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #1e3a5f;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">7:02</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">Analytics Deep Dive</div>
                <div style="font-size:11px;color:#6b7280">Read your data and export reports</div>
              </div>
            </div>
            <div style="border:1px solid #e5e7eb;border-radius:10px;overflow:hidden;cursor:pointer" onclick="showToast('Playing: API & Webhooks')">
              <div style="background:linear-gradient(135deg,#4c1d95,#7c3aed);height:90px;display:flex;align-items:center;justify-content:center;position:relative">
                <div style="width:40px;height:40px;background:rgba(255,255,255,0.9);border-radius:50%;display:flex;align-items:center;justify-content:center">
                  <div style="width:0;height:0;border-style:solid;border-width:8px 0 8px 16px;border-color:transparent transparent transparent #4c1d95;margin-left:3px"></div>
                </div>
                <span style="position:absolute;bottom:6px;right:8px;font-size:10px;color:rgba(255,255,255,0.8);background:rgba(0,0,0,0.4);padding:1px 5px;border-radius:3px">8:30</span>
              </div>
              <div style="padding:10px">
                <div style="font-size:12px;font-weight:700;margin-bottom:3px">API & Webhooks</div>
                <div style="font-size:11px;color:#6b7280">Connect EventHQ to your stack</div>
              </div>
            </div>
          </div>
        </div>

        <!-- FAQ Accordion -->
        <div class="editor-card" style="margin-bottom:16px">
          <div style="font-weight:700;font-size:15px;margin-bottom:14px">💬 Frequently Asked Questions</div>'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Video tutorials card inserted")
else:
    print("NOT FOUND")
