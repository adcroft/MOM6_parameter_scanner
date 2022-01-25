import os
import shutil
import tarfile
import tempfile
import pkg_resources as pkgr
import pytest
import mom6_parameter_scanner


def test_import():
    """tests if package can be imported"""
    import mom6_parameter_scanner


# set up temporary directories
cwd = os.getcwd()
tempdir = tempfile.mkdtemp()

# figure out where the sample data reside
resource_dir = pkgr.resource_filename("mom6_parameter_scanner", "resources")
shutil.copytree(resource_dir,f"{tempdir}/resources")

os.makedirs(f"{tempdir}/piControl/coupled")
os.makedirs(f"{tempdir}/piControl/oceanonly")
os.makedirs(f"{tempdir}/historical/coupled")
os.makedirs(f"{tempdir}/historical/oceanonly")

# make sample tar files
os.chdir(f"{tempdir}/resources/piControl")
with tarfile.open(
    f"{tempdir}/piControl/coupled/00010101.ascii_out.tar", mode="w"
) as archive:
    archive.add("./", recursive=True)

os.chdir(f"{tempdir}/resources/historical")
with tarfile.open(
    f"{tempdir}/historical/coupled/18500101.ascii_out.tar", mode="w"
) as archive:
    archive.add("./", recursive=True)

os.chdir(f"{tempdir}/resources/ocean_only_a")
with tarfile.open(
    f"{tempdir}/piControl/oceanonly/00010101.ascii_out.tar", mode="w", dereference=True
) as archive:
    archive.add("./", recursive=True)

os.chdir(f"{tempdir}/resources/ocean_only_b")
with tarfile.open(
    f"{tempdir}/historical/oceanonly/18500101.ascii_out.tar", mode="w", dereference=True
) as archive:
    archive.add("./", recursive=True)

os.chdir(cwd)

test_dirs = [
    f"{tempdir}/piControl/coupled/",
    f"{tempdir}/historical/coupled/",
    f"{tempdir}/piControl/oceanonly/",
    f"{tempdir}/historical/oceanonly/",
]


@pytest.mark.parametrize("dir", test_dirs)
def test_mom_parameters(dir):
    mom6_parameter_scanner.Parameters(dir)


@pytest.mark.parametrize("dir", test_dirs)
def test_sis_parameters(dir):
    mom6_parameter_scanner.Parameters(
        dir, parameter_files=["*SIS_parameter_doc.all", "*SIS_parameter_doc.short"]
    )


@pytest.mark.parametrize("dir", test_dirs)
def test_log0_parameters(dir):
    mom6_parameter_scanner.Log(dir, parameter_files=["*logfile.000000.out"])


@pytest.mark.parametrize("dir", test_dirs)
def test_log1_parameters(dir):
    mom6_parameter_scanner.Log(dir, ignore_files=["*logfile.000000.out"])


@pytest.mark.parametrize("dir", test_dirs)
def test_namelist0_parameters(dir):
    mom6_parameter_scanner.Namelists(dir, parameter_files=["*logfile.000000.out"])


@pytest.mark.parametrize("dir", test_dirs)
def test_namelist1_parameters(dir):
    mom6_parameter_scanner.Namelists(dir, ignore_files=["*logfile.000000.out"])


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def remove_test_dir():
        shutil.rmtree(tempdir)

    request.addfinalizer(remove_test_dir)
