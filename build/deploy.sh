#/bin/bash
# credits to seva zaikov. This script are an modified version from: 
# https://blog.bloomca.me/2017/12/15/how-to-push-folder-to-github-pages.html 

cd build
git add .
git commit -m "deployed at $(date -I)"
git push --force origin master:gh-pages

