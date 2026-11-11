pkgname = "python-google-auth"
pkgver = "2.62.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-cryptography"]
pkgdesc = "Python lib for Google API authentication"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth"
source = f"$(PYPI_SITE)/g/google-auth/google_auth-{pkgver}.tar.gz"
sha256 = "046c61a72d3a847d6df6417a7f0d5cf054e3b82bbcb54fb1e69d47880964049c"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
