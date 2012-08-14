
pgrep -f glipper | xargs kill -9 >/dev/null 2>&1
python glipperSnippetsExtend.py $1
echo "python finish"
# cd ~/codes/glipper/glipper-2.3/
# glipper-uninstalled
glipper & >/dev/null 2>&1
