pkgname = "lieer"
pkgver = "1.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-google-api-python-client",
    "python-google-auth-oauthlib",
    "python-notmuch2",
    "python-tqdm",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Email sync between notmuch and GMail"
license = "GPL-3.0-or-later"
url = "https://lieer.gaute.vetsj.com"
source = f"$(PYPI_SITE)/l/lieer/lieer-{pkgver}.tar.gz"
sha256 = "080c35b52dd034333cc1d25ac9f284a9dc8666539ada53f7065b2b783df492a2"


def post_install(self):
    self.install_license("COPYING.GPL-3.0+")
