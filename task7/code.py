import math

def calculate_attendance_recovery(total_classes, attended_classes, target_pct):
    """Calculates current attendance and required consecutive classes to reach target."""
    current_pct = (attended_classes / total_classes) * 100 if total_classes > 0 else 0.0
    
    if current_pct >= target_pct:
        required_classes = 0
        status = "Eligible (Target Met)"
    else:
        # Formula: X = ceil( (target * total - 100 * attended) / (100 - target) )
        numerator = (target_pct * total_classes) - (100 * attended_classes)
        denominator = 100 - target_pct
        required_classes = math.ceil(numerator / denominator)
        status = "Shortage (Recovery Needed)"
        
    return {
        "total": total_classes,
        "attended": attended_classes,
        "current_pct": round(current_pct, 2),
        "target_pct": target_pct,
        "required": required_classes,
        "status": status
    }

def analyze_student_attendance(student_records, target_pct):
    """Generates a formatted attendance recovery report for multiple students."""
    print("=" * 75)
    print(f"{'ATTENDANCE RECOVERY & ELIGIBILITY REPORT (Target: ' + str(target_pct) + '%)':^75}")
    print("=" * 75)
    print(f"{'Student Name':<15} | {'Total':<6} | {'Attended':<8} | {'Current %':<10} | {'Required Classes':<16} | {'Status'}")
    print("-" * 75)
    
    for name, data in student_records.items():
        res = calculate_attendance_recovery(data["total"], data["attended"], target_pct)
        print(f"{name:<15} | {res['total']:<6} | {res['attended']:<8} | {res['current_pct']:<9.2f}% | {res['required']:<16} | {res['status']}")
        
    print("=" * 75)

# --- Sample Execution ---
if __name__ == "__main__":
    target_threshold = 75.0  # 75% minimum attendance required
    
    students = {
        "Alice Smith": {"total": 40, "attended": 32},   # 80.00% (Above target)
        "Bob Jones": {"total": 40, "attended": 26},     # 65.00% (Below target)
        "Charlie Brown": {"total": 50, "attended": 30}, # 60.00% (Below target)
        "Diana Prince": {"total": 45, "attended": 40}   # 88.89% (Above target)
    }
    
    analyze_student_attendance(students, target_threshold)
