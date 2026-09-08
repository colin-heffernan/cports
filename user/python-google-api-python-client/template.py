pkgname = "python-google-api-python-client"
pkgver = "2.200.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python"]
pkgdesc = "Google API Client Library for Python"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-api-python-client"
source = f"$(PYPI_SITE)/g/google_api_python_client/google_api_python_client-{pkgver}.tar.gz"
sha256 = "82aa18b851328ea04867fd51c5a0c8da2e1b86ec45ce08487e902e7726d4ee50"
# Since the library is for accessing a cloud API, most tests require network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
