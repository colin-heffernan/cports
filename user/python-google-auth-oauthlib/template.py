pkgname = "python-google-auth-oauthlib"
pkgver = "1.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
pkgdesc = "Google Authentication Library"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python"
source = (
    f"$(PYPI_SITE)/g/google_auth_oauthlib/google_auth_oauthlib-{pkgver}.tar.gz"
)
sha256 = "1a83f5f2a8421dedadaa3caf25b3a710dddf85a33a63144be41c2fc79174b106"
# A number of checks fail, seemingly because of lack of network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
