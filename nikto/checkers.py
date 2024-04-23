import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    if text in out:
        print(True)
    else:
        print(False)


checkout("nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4", "0 error(s)")
