import os.path
import shutil
from unittest import TestCase
from unittest import mock
from optipng.optipng import OptiPNG

_TEST_DIR = os.path.abspath(os.path.dirname(__file__))


def _reset_output_dir() -> None:
    output_dir = os.path.join(_TEST_DIR, 'testdata/outputdir')
    os.makedirs(output_dir)
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)


class OptiPNGTests(TestCase):
    """
    Test OptiPNG.
    """
    def setUp(self):
        self.app = OptiPNG()
        _reset_output_dir()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append(os.path.join(_TEST_DIR, 'testdata/inputdir'))
        args.append(os.path.join(_TEST_DIR, 'testdata/outputdir'))

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        self.assertIn('pngtest.png', os.listdir(os.path.join(_TEST_DIR, 'testdata/outputdir')))
        self.assertGreater(
            os.stat(os.path.join(_TEST_DIR, 'testdata/inputdir/pngtest.png')).st_size,
            os.stat(os.path.join(_TEST_DIR, 'testdata/outputdir/pngtest.png')).st_size)

    def tearDown(self) -> None:
        _reset_output_dir()
