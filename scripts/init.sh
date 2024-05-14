# !/bin/bash
mv startwith "$1"
cd $1
sed -i '' "s/dev-startwith/$1-dev/" environment.yml
sed -i '' "s/dev-startwith/$1-dev/" README.md
git remote remove origin
rm -rf .git --yes
mv .vscode/startwith.code-workspace ".vscode/$1.code-workspace"
code .vscode/startwith.code-workspace