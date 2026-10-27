University Scholarship Allocation System

1. Problem Statement

Develop a Python program to allocate scholarships to university students. The system checks aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income. It selects eligible students, ranks them according to predefined rules, resolves ties, and awards scholarships to the top students based on a fixed quota.

 2. Algorithm

1. Start.
2. Read the number of students and scholarship quota.
3. Enter each student's name, aggregate marks, Mathematics marks, Science marks, attendance, and annual family income.
4. Check the eligibility conditions:
   - Aggregate marks ≥ 80.
   - Mathematics marks ≥ 70.
   - Science marks ≥ 70.
   - Attendance ≥ 85%.
   - Annual family income ≤ ₹1,80,000.
5. Store eligible and ineligible students separately.
6. Rank eligible students by:
   - Higher aggregate marks.
   - Higher attendance when aggregate marks are equal.
   - Lower family income when marks and attendance are equal.
7. Select the top students according to the quota.
8. Display winners and other students.
9. Stop.

 3. Flowchart — Mermaid Code

\#chatgpt-mermaid-\_r_fp\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_fp\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_fp\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_fp\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_fp\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_fp\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_fp\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_fp\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_fp\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_fp\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_fp\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_fp\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_fp\_ p{margin:0;}#chatgpt-mermaid-\_r_fp\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_fp\_ .label text,#chatgpt-mermaid-\_r_fp\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .node rect,#chatgpt-mermaid-\_r_fp\_ .node circle,#chatgpt-mermaid-\_r_fp\_ .node ellipse,#chatgpt-mermaid-\_r_fp\_ .node polygon,#chatgpt-mermaid-\_r_fp\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .rough-node .label text,#chatgpt-mermaid-\_r_fp\_ .node .label text,#chatgpt-mermaid-\_r_fp\_ .image-shape .label,#chatgpt-mermaid-\_r_fp\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_fp\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .rough-node .label,#chatgpt-mermaid-\_r_fp\_ .node .label,#chatgpt-mermaid-\_r_fp\_ .image-shape .label,#chatgpt-mermaid-\_r_fp\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_fp\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_fp\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_fp\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_fp\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_fp\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_fp\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_fp\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_fp\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_fp\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_fp\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_fp\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_fp\_ .icon-shape,#chatgpt-mermaid-\_r_fp\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_fp\_ .icon-shape p,#chatgpt-mermaid-\_r_fp\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_fp\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_fp\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_fp\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_fp\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_fp\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_fp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_fp\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_fp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_fp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_fp\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_fp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_fp\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_fp\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_fp\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_fp\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_fp\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .node rect,#chatgpt-mermaid-\_r_fp\_ .node circle,#chatgpt-mermaid-\_r_fp\_ .node ellipse,#chatgpt-mermaid-\_r_fp\_ .node polygon,#chatgpt-mermaid-\_r_fp\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_fp\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_fp\_ .node.mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_fp\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_fp\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_fp\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of students andquotaEnter student detailsAll eligibility conditionssatisfied?Add to eligible listAdd to ineligible listMore students?Sort eligible studentsApply tie-breaking rulesSelect top students withinquotaDisplay winners and otherstudentsStopYesNoYesNo

 4. Python Source Code

```
students = []eligible = []ineligible = []n = int(input("Enter number of students: "))quota = int(input("Enter scholarship quota: "))for i in range(n):    print("\nStudent", i + 1)    name = input("Enter name: ")    marks = float(input("Enter aggregate marks: "))    math = float(input("Enter Mathematics marks: "))    science = float(input("Enter Science marks: "))    attendance = float(input("Enter attendance percentage: "))    income = float(input("Enter annual family income: "))    student = {        "name": name,        "marks": marks,        "math": math,        "science": science,        "attendance": attendance,        "income": income    }    students.append(student)    if (marks >= 80 and math >= 70 and science >= 70            and attendance >= 85 and income <= 180000):        eligible.append(student)    else:        ineligible.append(student)# Rank by marks, attendance, then income
```

5. Sample Input

```
Enter number of students: 4
Enter scholarship quota: 2

Student 1
Enter name: Ravi
Enter aggregate marks: 90
Enter Mathematics marks: 85
Enter Science marks: 80
Enter attendance percentage: 95
Enter annual family income: 150000

Student 2
Enter name: Sita
Enter aggregate marks: 90
Enter Mathematics marks: 85
Enter Science marks: 80
Enter attendance percentage: 98
Enter annual family income: 120000

Student 3
Enter name: Priya
Enter aggregate marks: 88
Enter Mathematics marks: 90
Enter Science marks: 85
Enter attendance percentage: 92
Enter annual family income: 200000

Student 4
Enter name: Ram
Enter aggregate marks: 82
Enter Mathematics marks: 75
Enter Science marks: 72
Enter attendance percentage: 90
Enter annual family income: 100000
```

 6. Sample Output

```
--- Scholarship Winners ---
1 Sita | Marks: 90.0 | Attendance: 98.0 %
2 Ravi | Marks: 90.0 | Attendance: 95.0 %

--- Eligible but Not Selected ---
Ram

--- Ineligible Students ---
Priya
```


