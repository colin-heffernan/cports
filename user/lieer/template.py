pkgname = "lieer"
pkgver = "1.6"
pkgrel = 0
build_style = "python_pep517"
# make_check_args = [
#     # pytest fixture client not found
#     "--ignore=test/plugins/test_aura.py",
#     # requests_oauthlib
#     "--ignore=test/plugins/test_beatport.py",
#     # discogs_client
#     "--ignore=test/plugins/test_discogs.py",
#     # pylast
#     "--ignore=test/plugins/test_lastgenre.py",
#     # mpd
#     "--ignore=test/plugins/test_mpdstats.py",
#     # flakes
#     "--ignore=test/test_importer.py",
#     "--ignore=test/test_ui.py",
# ]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-google-api-python-client",
    "python-google-auth-oauthlib",
    "python-notmuch2",
    "python-tqdm",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Sync between notmuch and GMail"
license = "GPL-3.0-or-later"
url = "https://lieer.gaute.vetsj.com"
source = f"$(PYPI_SITE)/l/lieer/lieer-{pkgver}.tar.gz"
sha256 = "080c35b52dd034333cc1d25ac9f284a9dc8666539ada53f7065b2b783df492a2"


# def init_check(self):
#     self.make_check_args += [
#         f"--numprocesses={self.make_jobs}",
#         "--dist=worksteal",
#     ]


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_license("COPYING.GPL-3.0+")
    # self.install_man("man/beet.1")
    # self.install_man("man/beetsconfig.5")
