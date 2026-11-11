pkgname = "python-google-auth-httplib2"
pkgver = "0.4.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-google-auth", "python-httplib2"]
pkgdesc = "Python lib for Google auth with httplib2"
license = "Apache-2.0"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth-httplib2"
source = (
    f"$(PYPI_SITE)/g/google-auth-httplib2/google_auth_httplib2-{pkgver}.tar.gz"
)
sha256 = "b931de392c20cfaa351cd789274922bd8cdc001e0e9e96de31b39d71347f8e16"
# requires internet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
