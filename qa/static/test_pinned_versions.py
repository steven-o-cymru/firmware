"""The version strings a release reports and documents follow its pins."""
import re
import subprocess

import pytest

from lib.paths import ROOT

pytestmark = pytest.mark.static


@pytest.fixture(scope="module")
def pins():
    out = subprocess.run(
        ["bash", "-c", 'set -a; . "$1"; env -0', "pins",
         str(ROOT / "versions.env")],
        capture_output=True, check=True).stdout.decode()
    return dict(item.split("=", 1) for item in out.split("\0") if "=" in item)


def test_klipper_describe_names_the_pinned_commit(pins):
    match = re.fullmatch(r"v(\d+\.\d+\.\d+)-\d+-g([0-9a-f]{7,40})",
                         pins["KLIPPER_DESCRIBE"])
    assert match, pins["KLIPPER_DESCRIBE"]
    assert pins["KLIPPER_VERSION"].startswith(match.group(2)), (
        "KLIPPER_DESCRIBE was not bumped with KLIPPER_VERSION")
    conf = (ROOT / "pkgs/klipper/pkg.conf").read_text()
    assert 'PKG_VERSION="%s~' % match.group(1) in conf, (
        "pkgs/klipper/pkg.conf and KLIPPER_DESCRIBE name different releases")

