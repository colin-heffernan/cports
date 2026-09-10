pkgname = "zuban"
pkgver = "0.9.3"
pkgrel = 0
build_style = "cargo"
make_dir = f"zuban-{pkgver}"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Python Type Checker / Language Server"
license = "AGPL-3.0-only"
url = "https://zubanls.com"
_typeshed_commit = "bcb5ba6a29b6e1a661b50a3b4476fe7636072e3e"
_mypy_commit = "8236c93d899fa5225eb23644db802cf1e09196a7"
_django_stubs_commit = "5ea1b9977bec281488f0deabd39bfb0f7f2f56a4"
source = [
    f"https://github.com/zubanls/zuban/archive/v{pkgver}.tar.gz",
    f"https://github.com/python/typeshed/archive/{_typeshed_commit}.tar.gz",
    # f"https://github.com/davidhalter/mypy/archive/{_mypy_commit}.tar.gz",
    f"https://github.com/typeddjango/django-stubs/archive/{_django_stubs_commit}.tar.gz",
]
sha256 = [
    "c5dcbadf3ee569c85c8481e785200270f7203d79a6c30617256bd55bb412f983",
    "fd545101d8eb66552f863e3cdb66a395b4e81a564f4ad03b3dafe31638d60cea",
    # "b72ca9451aeced6cfa4897af69902b953e1c88503ad56b6cdeb382f831ee300f",
    "786bd29c94bb000f7be0769954dfcc9ceeedd7542d93b14476447385bda3e2c1",
]


def post_extract(self):
    self.mv(
        f"typeshed-{_typeshed_commit}",
        f"zuban-{pkgver}/third_party/typeshed",
    )
    # self.cp(
    #     f"mypy-{_mypy_commit}",
    #     f"zuban-{pkgver}/crates/zuban_python/tests/mypylike/mypy",
    #     recursive=True,
    # )
    self.mv(
        f"django-stubs-{_django_stubs_commit}",
        f"zuban-{pkgver}/third_party/django-stubs",
    )
    self.cp(f"zuban-{pkgver}/*", "./", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
