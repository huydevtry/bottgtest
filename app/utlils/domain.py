from urllib.parse import urlparse

def analyze_domain(url: str) -> dict:
    parsed = urlparse(url)

    if not parsed.scheme or not parsed.hostname:
        raise ValueError("Invalid URL")

    host_parts = parsed.hostname.split(".")

    if len(host_parts) < 2:
        domain = parsed.hostname
        subdomain = None
    else:
        domain = ".".join(host_parts[-2:])
        subdomain = ".".join(host_parts[:-2]) or None

    return {
        "scheme": parsed.scheme,
        "domain": domain,
        "subdomain": subdomain,
        "port": parsed.port,
        "path": parsed.path,
        "query": parsed.query,
    }