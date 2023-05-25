call sphinx-build doc _build
call sphinx-build doc -W -b linkcheck -d _build/doctrees _build/html