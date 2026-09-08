pkgname = "python-notmuch2"
pkgver = "0.34.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "notmuch-devel",
    "python-build",
    "python-cffi",
    "python-devel",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python", "python-cffi"]
checkdepends = ["python-pytest"]
pkgdesc = "Pythonic bindings for the notmuch mail database using CFFI"
license = "GPL-3.0-only"
url = "https://github.com/weilbith/notmuch2-python-bindings"
source = f"$(PYPI_SITE)/n/notmuch2/notmuch2-{pkgver}.post1.tar.gz"
sha256 = "d9f571a5eb7d503607df584835898714c8f397fe9363caed4133af1384c26cd7"
# temp, requires pytest-cov
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
