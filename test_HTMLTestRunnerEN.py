import HTMLTestReportCN

if __name__ == '__main__':
    filePath ='F:\\Report.html'
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerEN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='',
        #tester="Findyou"
        )
    runner.run(Suite())