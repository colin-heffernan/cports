pkgname = "python-uritemplate"
pkgver = "4.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python lib for URI template parsing"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://uritemplate.readthedocs.io"
source = f"$(PYPI_SITE)/u/uritemplate/uritemplate-{pkgver}.tar.gz"
sha256 = "480c2ed180878955863323eea31b0ede668795de182617fef9c6ca09e6ec9d0e"


def post_install(self):
    self.install_license("LICENSE.APACHE")
    self.install_license("LICENSE.BSD")
