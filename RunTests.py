import unittest
import HTMLTestRunner
import Tests


suite = unittest.TestLoader().loadTestsFromTestCase(Tests.Tests)

# Please input path to your Report.html directory
outfile = open("C:\Users\User\Desktop\Report.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    verbosity=2,
    title='Test Report',
    description='This report is created by Kate.Syroed')

runner.run(suite)


