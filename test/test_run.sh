while true;do
echo "Select a test to run"
echo "1)test_get_title
2)test_get_fname
3)test_first_name_is_valid
4)test_get_lname
5)test_last_name_is_valid
6)test_get_email
7)test_email_is_valid
8)test_get_phone
9)test_phone_is_valid
10)test_one_radio_button_is_selected
11)test_at_least_one_check_box_is_selected
12)test_clear_button
13)test_send_button
14)test_next_page
15)test_windy
16)test_tera_santa
17)test_java_book
18)test_youtube
19)test_set_text_from_prompt_alert
20)test_get_finish
21)run all
0)exit

"

read input

case "$input" in
1)
pytest test_AutomationProjectPage.py::test_get_title
;;
2)
pytest test_AutomationProjectPage.py::test_get_fname
;;
3)
pytest test_AutomationProjectPage.py::test_first_name_is_valid
;;
4)
pytest test_AutomationProjectPage.py::test_get_lname
;;
5)
pytest test_AutomationProjectPage.py::test_last_name_is_valid
;;
6)
pytest test_AutomationProjectPage.py::test_get_email
;;
7)
pytest test_AutomationProjectPage.py::test_email_is_valid
;;
8)
pytest test_AutomationProjectPage.py::test_get_phone
;;
9)
pytest test_AutomationProjectPage.py::test_phone_is_valid
;;
10)
pytest test_AutomationProjectPage.py::test_one_radio_button_is_selected
;;
11)
pytest test_AutomationProjectPage.py::test_at_least_one_check_box_is_selected
;;
12)
pytest test_AutomationProjectPage.py::test_clear_button
;;
13)
pytest test_AutomationProjectPage.py::test_send_button
;;
14)
pytest test_AutomationProjectPage.py::test_next_page
;;
15)
pytest test_AutomationProjectPage.py::test_windy
;;
16)
pytest test_AutomationProjectPage.py::test_tera_santa
;;
17)
pytest test_AutomationProjectPage.py::test_java_book
;;
18)
pytest test_AutomationProjectPage.py::test_youtube
;;
19)
pytest test_AutomationProjectPage.py::test_set_text_from_prompt_alert
;;
20)
pytest test_AutomationProjectPage.py::test_get_finish
;;
21)
pytest test_AutomationProjectPage.py
;;
0)
break
;;
*)
echo "Invalid input"
;;
esac
done