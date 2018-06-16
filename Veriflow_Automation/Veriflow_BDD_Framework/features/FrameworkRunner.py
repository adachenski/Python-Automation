#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    # run Behave + BDD + Python code
    tagList = ' --tags=-dontRun '  # any scenario except tagged with this tag
    # featureFilePath = ' feature_files '
    # featureFilePath = ' feature_files//Veriflow_Smoke_Test.feature '
    featureFilePath = ' feature_files//Advanced_Searches_Sanity_Test.feature '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + commonRunnerOptions + tagList
    runner_with_options.main(fullRunnerOptions)
