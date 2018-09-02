import hashlib
import urllib.request


def hash_jar(version):
    request = urllib.request.urlopen(f'https://cdn.runemate.com/builds/{version}/standalone/RuneMate.jar')
    m = hashlib.md5()
    m.update(request.read())
    return m.hexdigest()


def get_latest_version():
    request = urllib.request.urlopen('https://www.runemate.com/client/runemate_version.php')
    return request.read().decode('UTF-8')
