pkgname = "python-oauthlib"
pkgver = "4.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-blinker",
    "python-cryptography",
    "python-pytest",
]
pkgdesc = "Python library for OAuth request signing"
license = "BSD-3-Clause"
url = "https://github.com/oauthlib/oauthlib"
source = f"$(PYPI_SITE)/o/oauthlib/oauthlib-{pkgver}.tar.gz"
sha256 = "3d73febdb6faa00f277c81fb04be7b7586fb96fc3b7f0b9c772dada69a25ede7"
# missing checkdep
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
