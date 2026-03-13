import re
from urllib.parse import urlparse

def extract_features_from_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    path = parsed.path
    query = parsed.query

    return {
        'url_length': len(url),
        'domain_length': len(domain),
        'path_length': len(path),
        'query_length': len(query),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_slashes': url.count('/'),
        'num_subdomains': len(domain.split('.')) - 1,
        'has_at': int('@' in url),
        'has_ip': int(bool(re.match(r'(http[s]?://)?(\d{1,3}\.){3}\d{1,3}', url))),
        'https': int(url.lower().startswith('https')),
        'has_port_in_url': int(':' in parsed.netloc),
        'has_double_slash_redirect': int('//' in path.strip('/')),
        'has_suspicious_words': int(any(word in url.lower() for word in ['login','verify','bank','update','secure']))
    }