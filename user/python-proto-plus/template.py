pkgname = "python-proto-plus"
pkgver = "1.29.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
depends = ["python-protobuf"]
pkgdesc = "Python wrapper for protobuf"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/proto-plus"
source = f"$(PYPI_SITE)/p/proto-plus/proto_plus-{pkgver}.tar.gz"
sha256 = "cfb4e62ad7e13dd18f346cabbda00cab39930d36a05791fd81ddb074d6ee884f"
# doesnt wanna work?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
