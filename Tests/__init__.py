import logging
import sys
from os import makedirs
from os.path import abspath, dirname, isdir, join
from shutil import rmtree

from matplotlib import use
from packaging.version import Version

# check python version for import of pyside2 or pyside6
PYTHON_VERSION = Version(sys.version.split(" ")[0])
if PYTHON_VERSION <= Version("3.9"):
    try:
        from PySide2 import QtCore

        # Use Qt5/Qt6 backend depended on whats installed (PyQt5/PySide2 or PyQt6/PySide6)
        use("qtagg")
    except ImportError:
        use("agg")
elif PYTHON_VERSION > Version("3.9"):
    try:
        from PySide6 import QtCore

        # Use Qt5/Qt6 backend depended on whats installed (PyQt5/PySide2 or PyQt6/PySide6)
        use("qtagg")
    except ImportError:
        use("agg")
else:
    logging.error("Invalid python version %s", sys.version_info)

TEST_DIR = abspath(dirname(__file__))
DATA_DIR = join(TEST_DIR, "Data")
LOG_DIR = join(TEST_DIR, "logtest.txt")
DOC_DIR = abspath(join(TEST_DIR, "..", "Doc"))
# Set logger for test
x = logging.getLogger("logtest")
x.setLevel(logging.DEBUG)
h = logging.FileHandler(LOG_DIR)
f = logging.Formatter("%(message)s")
h.setFormatter(f)
x.addHandler(h)
# Init the result folder for the test
save_path = join(TEST_DIR, "Results")
if isdir(save_path):  # Delete previous test result
    rmtree(save_path)
# To save all the plot geometry results
save_plot_path = join(save_path, "Plot")
makedirs(save_plot_path)
# To save the validation results
save_validation_path = join(save_path, "Validation")
makedirs(save_validation_path)
# To save the Save/Load .json results
save_load_path = join(save_path, "Save_Load")
makedirs(save_load_path)
# To clean all the results at the end of the corresponding test
is_clean_result = False
