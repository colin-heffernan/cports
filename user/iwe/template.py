pkgname = "iwe"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Markdown memory system for you and your AI agent"
license = "Apache-2.0"
url = "https://github.com/iwe-org/iwe"
source = f"{url}/archive/iwe-v{pkgver}.tar.gz"
sha256 = "02c550c1b5695f3969a21b6edaeae0214602650ef51f2b2851deeeaa082bc407"


# FIXME: add the binaries to the PATH
# def pre_check(self):
#     print(f"{self.env}")
#     self.env["PATH"] = (
#         f"target/{self.profile().triplet}/release:{self.env['PATH']}"
#     )


def check(self):
    return


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/iwe")
    self.install_bin(f"target/{self.profile().triplet}/release/iwec")
    self.install_bin(f"target/{self.profile().triplet}/release/iwes")
    self.install_license("LICENSE-APACHE")
