import subprocess

from django.shortcuts import render


def execute_ping(hostname):
    try:
        # Run the ping command with the specified hostname or IP address
        result = subprocess.run(
            ["ping", "-c", "4", hostname], capture_output=True, text=True
        )

        if result.returncode == 0:
            # Ping was successful
            output = result.stdout
            return output
        else:
            # Ping failed
            error = result.stderr
            return error

    except subprocess.CalledProcessError as e:
        # An error occurred while running the ping command
        return str(e)


# Create your views here.


def index(request):
    hostname = "example.com"
    ping_result = execute_ping(hostname)
    print(ping_result)
    return render(request, "index.html", {"ping_result": ping_result})
