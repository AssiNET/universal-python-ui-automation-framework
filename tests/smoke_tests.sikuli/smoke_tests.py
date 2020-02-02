import unittest
from _lib import *
import HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner

import os

class SmokeTests(unittest.TestCase):
    # Execute BEFORE each Test
    def setUp(self):
        # Write test name into the Textbox file
        test_name = '.'.join(self._testMethodName.split('.')[-2:])
        f = open(os.path.join(os.getcwd(), 'tools', 'textbox', 'textbox.txt'), 'wb')
        f.write(test_name)
        f.close()

    # Execute AFTER each test
    def tearDown(self):
        pass

    def test_100_Start_Browser(self):
        Reporting.TestLog("This function print info into console/jenkins-output and Report.html as well")
        print("print info only in Report.html")

        # Run SampleWebpage_for_demos_125dpi.html in CMD which start Chrome Automatically
        sample_web_page_path = os.path.join(os.getcwd(), 'content', 'SampleWebpage_for_demos_125dpi.html')
        os.system(sample_web_page_path)
        #Browser.Start(r"google.com")
        wait(Browser_UI.button_Refresh, 5)
        Browser.Maximize()

    def test_200_Check_Stop_Button(self):
        Reporting.TestLog("XXXXXXXXX Test 222 started XXXXXXXXX")
        click(SamplePage_UI.button_Reload)
        click(SamplePage_UI.button_Test)
        clipboard = UIActions.CopyAllClipboard()
        assert "Clicked" in clipboard

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    # #Use it to add manually test cases - handy when debugging a specific part of the set
	# suite = unittest.TestSuite() -
    # suite.addTest(SmokeTests('test_100_Start_Browser'))
    # suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

    outfile = open("Report.html", "w")
    runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Some descr")
    runner.run(suite)
    outfile.close()
