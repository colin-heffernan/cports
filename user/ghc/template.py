pkgname = "ghc"
pkgver = "9.14.1"
pkgrel = 0
depends = ["gmp-devel", "libffi8-devel", "perl", "gcc", "llvm", "clang"]
makedepends = [
    "ghc-bootstrap",
    "autoconf",
    "automake",
    "binutils",
    "libffi8-devel",
    "ncurses-devel",
    "xz",
    "chimerautils",
    "ggrep",
    "python-sphinx",
    "git",
]
hostmakedepends = [
    "linux-headers",
    "musl-devel",
    "zlib-ng-devel",
    "gmp-devel",
    "binutils",
    "libffi-dev",
    "ncurses-devel",
]
checkdepends = ["python", "diffutils", "bash"]
pkgdesc = "Glasgow Haskell Compiler"
license = "BSD-3-Clause"
url = "https://www.haskell.org/ghc"
source = f"{url}/dist/{pkgver}/{pkgname}-{pkgver}-src.tar.xz"
sha256 = "2a83779c9af86554a3289f2787a38d6aa83d00d136aa9f920361dd693c101e77"


def pre_configure(self):
    self.do("./boot.source")


def configure(self):
    self.do('LD="$CC"', "./configure")


def build(self):
    self.do("hadrian/build", "-j")


def install(self):
    raise Exception("todo")


def post_install(self):
    self.install_license("LICENSE")
