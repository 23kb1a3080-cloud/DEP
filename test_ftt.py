import sys
sys.stdout.reconfigure(encoding='utf-8')
from rag_chatbot import (get_response, load_timetable_data, load_faculty_data,
                         initialize_nlp, train_ml_classifier, load_knowledge_base,
                         classify_query_module, analyse_query)

load_timetable_data()
load_faculty_data()
initialize_nlp()
train_ml_classifier()
load_knowledge_base()

tests = [
    'faculty timetable',
    'faculty time table',
    'timetable of Dr Narayana Rao',
    'show timetable of SD',
    'teacher timetable',
    'schedule of Dr Rao',
    'faculty schedule',
]

for q in tests:
    qa = analyse_query(q)
    module = classify_query_module(q, qa)
    resp = get_response(q)
    nl = chr(10)
    snippet = resp[:200].replace(nl, ' ')
    status = "OK" if "I don" not in resp else "FAIL"
    print(f"  {status}  module={module:25s}  {q!r:40s}")
    print(f"       -> {snippet}")
    print()
