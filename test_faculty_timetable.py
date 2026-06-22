import sys
sys.stdout.reconfigure(encoding='utf-8')
from rag_chatbot import (get_response, load_timetable_data, load_faculty_data,
                         initialize_nlp, train_ml_classifier, load_knowledge_base)

load_timetable_data()
load_faculty_data()
initialize_nlp()
train_ml_classifier()
load_knowledge_base()

print("=" * 80)
print("TESTING FACULTY TIMETABLE FUNCTIONALITY")
print("=" * 80)

tests = [
    'faculty timetable',
    'faculty time table',
    'timetable of Dr Narayana Rao',
    'show timetable of Mahendra',
    'teacher timetable',
    'schedule of Dr Rao',
    'faculty schedule',
    'Venkateswarlu timetable',
    'timetable of Sivapratap',
]

for q in tests:
    print(f"\n{'='*80}")
    print(f"Query: {q}")
    print(f"{'='*80}")
    resp = get_response(q)
    
    # Check if response contains timetable HTML
    if "timetable-card-container" in resp or "timetable-table" in resp:
        print("✅ SUCCESS: Faculty timetable HTML found in response")
        # Show first 300 chars
        print(f"Response preview: {resp[:300]}...")
    elif "I don" in resp:
        print("❌ FAIL: Got 'I don't know' response")
    else:
        print("⚠️  UNKNOWN: Response doesn't contain expected timetable HTML")
        print(f"Response preview: {resp[:300]}...")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
