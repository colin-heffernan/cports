pkgname = "python-google-auth-oauthlib"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-google-auth", "python-requests-oauthlib"]
pkgdesc = "Python lib for Google API authentication via OAuth"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth-oauthlib"
source = (
    f"$(PYPI_SITE)/g/google-auth-oauthlib/google_auth_oauthlib-{pkgver}.tar.gz"
)
sha256 = "b351107c7dd9017f426cbb0272ea1bc04f469020fd18f4443c7d40362e0b1510"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
