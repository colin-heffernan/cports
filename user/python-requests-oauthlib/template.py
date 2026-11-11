pkgname = "python-requests-oauthlib"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-oauthlib",
    "python-requests",
]
pkgdesc = "Python library for OAuth support for Requests"
license = "ISC"
url = "https://github.com/requests/requests-oauthlib"
source = f"$(PYPI_SITE)/r/requests-oauthlib/requests-oauthlib-{pkgver}.tar.gz"
sha256 = "b3dffaebd884d8cd778494369603a9e7b58d29111bf6b41bdc2dcd87203af4e9"
# depends on internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
