pkgname = "pnpm"
pkgver = "11.5.1"
pkgrel = 0
depends = ["nodejs"]
pkgdesc = "Fast, disk space efficient package manager"
license = "MIT"
url = "https://pnpm.io"
source = f"https://github.com/pnpm/pnpm/releases/download/v{pkgver}/pnpm-linux-x64-musl.tar.gz"
sha256 = "103e77f25422802a89c6206a09466b05042e9f8e40921db177550944abc7882c"


def install(self):
    # self.install_file("lib/v8-compile-cache.js", "usr/lib/yarn")
    # self.install_file("lib/cli.js", "usr/lib/yarn")
    self.install_bin("pnpm")
    # self.install_license("LICENSE")
