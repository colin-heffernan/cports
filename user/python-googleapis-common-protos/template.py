pkgname = "python-googleapis-common-protos"
pkgver = "1.76.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-protobuf", "grpc"]
pkgdesc = "Python lib for common Google API protobufs"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos"
source = f"$(PYPI_SITE)/g/googleapis-common-protos/googleapis_common_protos-{pkgver}.tar.gz"
sha256 = "71db0e44a1d4c2dd024ebad44ca67129cc1e2892e4861df466764749d5ef8642"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
