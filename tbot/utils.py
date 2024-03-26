import subprocess

def get_ip():
    cmd = """hostname -I"""
    r = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)
    return r.stdout.strip()

