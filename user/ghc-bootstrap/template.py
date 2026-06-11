pkgname = "ghc-bootstrap"
pkgver = "9.14.1"
pkgrel = 0
pkgdesc = "Bootstrap version of ghc"
license = "BSD-3-Clause"
url = "https://www.haskell.org/ghc"
options = ["!lintstatic"]

match self.profile().arch:
    case "x86_64":
        source = f"https://downloads.haskell.org/ghc/{pkgver}/ghc-{pkgver}-x86_64-alpine3_12-linux-static.tar.xz"
        sha256 = (
            "238ff218098949b9c6be2315b4a288fbdd2edd4cd29a1b6e27117b784c23802f"
        )
    case "aarch64":
        source = f"https://downloads.haskell.org/ghc/{pkgver}/ghc-{pkgver}-aarch64-alpine3_22-linux.tar.xz"
        sha256 = ""
    case _:
        broken = (
            f"No distfiles available for this target: {self.profile().arch}"
        )


def configure(self):
    self.do("./configure", "--prefix=/usr")


def install(self):
    self.do("make", "install", f"DESTDIR=../..{self.chroot_destdir}")


def post_install(self):
    self.install_license(
        f"share/doc/x86_64-linux-ghc-{pkgver}-05ec/ghc-{pkgver}/LICENSE"
    )
