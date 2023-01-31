# 2_2_3-4.py
# feedback = input("напишите впечатления")
feedback = "Было весело, увлекательно. Хорошие развлечения"

low_feedback = feedback.lower()
split_feedback = low_feedback.split()

if "весело" in split_feedback or "увлекательно" in split_feedback or "развлечения" in split_feedback:
    print("ok")
else:
    print("no")