while true;do
echo "Select a test to run"
echo "1)test_add
2)test_sub
3)test_sum_of_digits
4)test_sum_of_digits_flag_exceptin
5)test_ispl
6)test_compress
7)test_exceptin_add
8)test_exceptin_sub
9)test_exceptin_value_sumofdigit
10)test_exceptin_value_ispl
11)run all
0)exit

"

read input

case "$input" in
1)
pytest test_zip.py::test_add
;;
2)
pytest test_zip.py::test_sub
;;
3)
pytest test_zip.py::test_sum_of_digits
;;
4)
pytest test_zip.py::test_sum_of_digits_flag_exceptin
;;
5)
pytest test_zip.py::test_ispl
;;
6)
pytest test_zip.py::test_compress
;;
7)
pytest test_zip.py::test_exceptin_add
;;
8)
pytest test_zip.py::test_exceptin_sub
;;
9)
pytest test_zip.py::test_exceptin_value_sumofdigit
;;
10)
pytest test_zip.py::test_exceptin_value_ispl
;;
11)
pytest test_zip.py
;;
0)
break
;;
*)
echo "Invalid input"
;;
esac
done