pkgname = "ghc-devel"
pkgver = "9.8.4"
pkgrel = 0
pkgdesc = "Glasgow Haskell Compiler, precompiled binary"
license = "BSD-3-Clause"
url = "https://www.haskell.org/ghc"
source = f"https://downloads.haskell.org/ghc/{pkgver}/ghc-{pkgver}-x86_64-alpine3_12-linux-static.tar.xz"
sha256 = "02535eaef4f57aef8b7b272ef6f48d386d186ebd07fa47e227b46b93fa7eb0ab"


def configure(self):
    self.do("./configure", "--prefix=/usr")


def install(self):
    self.do("make", "install", f"DESTDIR=../..{self.chroot_destdir}")


def post_install(self):
    self.install_license("share/doc/x86_64-linux-ghc-9.8.4/ghc-9.8.4/LICENSE")
