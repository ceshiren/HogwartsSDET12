for i in `adb devices|grep 'device$'|awk '{print $1}'`
do
  echo $i
  udid=$i pytest test_xueqiu1.py --alluredir ./result_$i &
done