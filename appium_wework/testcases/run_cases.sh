[ -e /tmp/fifo_3 ] || mkfifo /tmp/fifo_3
exec 3<> /tmp/fifo_3
rm -rf /tmp/fifo_3

adb devices | grep "device$" | awk '{print $1}' >&3

find . -name "test_xueqiu*.py" | {
  while read file; do
    read udid <&3 && {
        echo udid=$udid
        udid=$udid pytest $file
        echo $udid >&3
      } &     # & 放入后台执行

      done
      wait
    }

exec 3<&-
exec 3<&-