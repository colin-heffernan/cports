pkgname = "pyrefly"
pkgver = "1.3.1"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--", "--skip", "test_get_source_db_always_configures_paths"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["pkgconf", "rust-std", "zstd-devel"]
checkdepends = ["bash"]
pkgdesc = "Fast type checker and language server for Python"
license = "MIT"
url = "https://pyrefly.org"
source = f"https://github.com/facebook/pyrefly/archive/{pkgver}.tar.gz"
sha256 = "00777ca516a4bd6740c2f5b2c70a5ead3349bb565e5f86ba8ae59810b5ea3f45"


def post_install(self):
    self.install_license("LICENSE")
