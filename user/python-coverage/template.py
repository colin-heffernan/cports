pkgname = "python-coverage"
pkgver = "7.16.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python", "python-flaky", "python-hypothesis"]
checkdepends = ["python-pytest", "python-pytest-xdist", *depends]
pkgdesc = "Code coverage measurement for Python"
license = "Apache-2.0"
url = "https://github.com/coveragepy/coveragepy"
source = f"$(PYPI_SITE)/c/coverage/coverage-{pkgver}.tar.gz"
sha256 = "f83981779bcf9dfa06fa0a8d4cb43e0faec1706328ce07aa3e7b665b4ac0f210"


def post_install(self):
    self.install_license("LICENSE.txt")
