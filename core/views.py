import subprocess

from django.core.cache import cache
from django.shortcuts import render


def get_visitor_ip(request):
    # Check if the request contains the 'HTTP_X_FORWARDED_FOR' header
    if "HTTP_X_FORWARDED_FOR" in request.META:
        # Multiple IP addresses may be present in the 'HTTP_X_FORWARDED_FOR' header
        ip_addresses = request.META["HTTP_X_FORWARDED_FOR"].split(",")
        # The client's IP address is typically the first address in the list
        visitor_ip = ip_addresses[0].strip()
    else:
        # If the 'HTTP_X_FORWARDED_FOR' header is not present, use 'REMOTE_ADDR'
        visitor_ip = request.META.get("REMOTE_ADDR", "")

    cache.set("hostname", visitor_ip)
    return visitor_ip


def execute_ping(hostname):
    try:
        # Run the ping command with the specified hostname or IP address
        result = subprocess.run(
            ["ping", "-c", "4", hostname], capture_output=True, text=True
        )

        if result.returncode == 0:
            # Ping was successful
            output = result.stdout
            print(output)
            return output
        else:
            # Ping failed
            error = result.stderr
            print(error)
            return error

    except subprocess.CalledProcessError as e:
        # An error occurred while running the ping command
        print(str(e))
        return str(e)


# Create your views here.


def index(request):
    hostname = get_visitor_ip(request)
    # ping_result = execute_ping(hostname)
    return render(
        request,
        "index.html",
        {
            "hostname": hostname,
            # "ping_result": ping_result,
        },
    )
