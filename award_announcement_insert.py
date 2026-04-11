with open('EventHQ_Dashboard_v3_PC.html', 'r') as f:
    content = f.read()

old_str = '''      </div>

      <!-- ══ VIEW: Buyer Invitation ══ -->'''

new_str = '''        <!-- Award Announcement Generator -->
        <div class="editor-card" style="margin-top:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
            <div style="font-weight:700;font-size:15px">📢 Announcement Generator</div>
            <div style="display:flex;gap:8px">
              <button onclick="generateAwardAnnouncement()" class="btn-secondary" style="font-size:12px;padding:6px 12px">Generate</button>
              <button onclick="copyAnnouncement()" class="btn-primary" style="font-size:12px;padding:6px 12px">Copy Text</button>
            </div>
          </div>
          <!-- Format selector -->
          <div style="display:flex;gap:6px;margin-bottom:14px">
            <button id="ann-fmt-press" onclick="switchAnnFormat('press')" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#2563eb;color:#fff;font-weight:600">Press Release</button>
            <button id="ann-fmt-social" onclick="switchAnnFormat('social')" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Social Media</button>
            <button id="ann-fmt-email" onclick="switchAnnFormat('email')" style="font-size:11px;padding:4px 12px;border:none;border-radius:10px;cursor:pointer;background:#f3f4f6;color:#374151">Email Blast</button>
          </div>
          <!-- Generated text area -->
          <div id="ann-output" style="background:#f8f9fa;border:1px solid #e5e7eb;border-radius:8px;padding:16px;font-size:13px;line-height:1.7;color:#374151;min-height:140px;white-space:pre-wrap;font-family:Georgia,serif">
FOR IMMEDIATE RELEASE

Game Connection 2025 — Award Winners Announced

Game Connection is proud to announce the winners of this year's prestigious awards:

🏆 Best Art Direction — Neon Abyss 2 (Score: 9.6/10)
   Developer: Dark Pixel Studios | 5 juror votes

🥇 Best Indie Game — Stellar Drift (Score: 8.4/10)
   Developer: Orbit Games | 5 juror votes

🥉 Best Narrative — Echo Protocol (Score: 6.2/10)
   Developer: Hollow Depths Studio | 3 juror votes

Voting for Best Mobile Game is still in progress.

For more information, visit: gameconnection.com/awards-2025
          </div>
          <!-- Social share buttons -->
          <div style="display:flex;gap:8px;margin-top:12px">
            <button onclick="showToast('Opening Twitter/X share...')" style="flex:1;font-size:12px;padding:7px;background:#000;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600">𝕏 Share on X</button>
            <button onclick="showToast('Opening LinkedIn share...')" style="flex:1;font-size:12px;padding:7px;background:#0a66c2;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600">in LinkedIn</button>
            <button onclick="showToast('Opening Facebook share...')" style="flex:1;font-size:12px;padding:7px;background:#1877f2;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600">f Facebook</button>
            <button onclick="showToast('Press release PDF generated')" style="flex:1;font-size:12px;padding:7px;background:#dc2626;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:600">📄 PDF</button>
          </div>
        </div>
      </div>

      <!-- ══ VIEW: Buyer Invitation ══ -->'''

if old_str in content:
    content = content.replace(old_str, new_str, 1)
    with open('EventHQ_Dashboard_v3_PC.html', 'w') as f:
        f.write(content)
    print("OK: Award announcement generator inserted")
else:
    # Try to find the exact string
    idx = content.find('<!-- ══ VIEW: Buyer Invitation ══ -->')
    print(f"Buyer Invitation found at index: {idx}")
    print(repr(content[idx-50:idx+50]))
