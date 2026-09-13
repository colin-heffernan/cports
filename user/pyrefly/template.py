pkgname = "pyrefly"
pkgver = "1.3.0"
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
sha256 = "f26552aae8957d6924319034eadd69830f2442685fc4e696c97e777c827a4082"


def post_install(self):
    self.install_license("LICENSE")
