pkgname = "pizauth"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera", "rust-std", "turnstile"]
pkgdesc = "Command-line OAuth2 authentication daemon"
license = "MIT OR Apache-2.0"
url = "https://tratt.net/laurie/src/pizauth"
source = f"{url}/releases/{pkgname}-{pkgver}.tgz"
sha256 = "a1917ac6c953ce236f82cbf05bf2f3866cd99e5635ec37780570c4f6a422285d"


def post_install(self):
    # Licenses
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
    self.install_license("COPYRIGHT")

    # Service
    self.install_service(self.files_path / "pizauth.user")

    # Manpages
    self.install_man("pizauth.1")
    self.install_man("pizauth.conf.5")

    # Completions
    # Bash, Fish, Zsh
