pkgname = "python-google-api-python-client"
pkgver = "2.202.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-google-api-core",
    "python-google-auth",
    "python-google-auth-httplib2",
    "python-httplib2",
    "python-uritemplate",
]
pkgdesc = "Python client for the Google API"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-api-python-client"
source = f"$(PYPI_SITE)/g/google-api-python-client/google_api_python_client-{pkgver}.tar.gz"
sha256 = "ae126c8e91f43c331e23dbd83bc4a8075699dd48089cebc7295f6ab2f5850fc5"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
