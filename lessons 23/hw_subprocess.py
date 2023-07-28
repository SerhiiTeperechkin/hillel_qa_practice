import platform
import subprocess


def ping_websites(websites, count):
    operating_system = platform.system().lower()

    if operating_system == 'windows':
        command = ['ping', '-n', str(count)]
    elif operating_system == 'linux':
        command = ['ping', '-c', str(count)]
    else:
        raise OSError("Unsupported operating system. The function supports Windows and Linux only.")

    for website in websites:
        print(f"Pinging {website}...")
        command.append(website)
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(result.stdout.encode('windows-1251').decode('ibm866'))
        except subprocess.CalledProcessError as e:
            print(f"Error pinging {website}: {e}")
        command.pop()


websites_to_ping = ['www.google.com', 'www.youtube.com', 'www.github.com']
ping_count = 3

ping_websites(websites_to_ping, ping_count)
