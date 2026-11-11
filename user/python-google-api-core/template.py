pkgname = "python-google-api-core"
pkgver = "2.44.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-google-auth",
    "python-googleapis-common-protos",
    "python-proto-plus",
    "python-protobuf",
    "python-requests",
]
pkgdesc = "Python lib for the Google API"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-api-core"
source = f"$(PYPI_SITE)/g/google-api-core/google_api_core-{pkgver}.tar.gz"
sha256 = "5ab9a396965c1227d7dea4581e562b7018aa2bca96d2de0be5eb70dc9c8ab3a1"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
