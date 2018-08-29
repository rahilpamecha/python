import time

q1={"question":"What role did space shuttles play in the making of the international space station?","option":["guidance","fuel","transportation","repair"],"answer":3}
q2={"question":"Which area of transportation has benefited the most from exploration technology?","option":["ships","railroads","auto","aircraft"],"answer":4}
q3={"question":"Who was the first man in space?","option":["yuri gagarin","alan shepard","alan musk","tom hanks"],"answer":1}
q4={"question":"What is one major difference between the space shuttle and earlier spacecraft?","option":["reusability","carriage","solarsystem outreach","interplanetary"],"answer":1}
q5={"question":"Who was the first person to walk on the moon?","option":["Buzz Aldrin","Neil Armstrong","John Glenn","Alan Shepard"],"answer":2}
q6={"question":"Firefighters wear jackets that resist fire. This fabric was orginially designed for?","option":["shuttle seats","shuttle insulation","cargo","suits"],"answer":4}
q7={"question":"Which of the following planets has a revolution time which is shorter than its rotation time?","option":["Jupiter","Venus","Mars","Uranus"],"answer":2}
q=[q1,q2,q3,q4,q5,q6,q7]
Score = 0
for j in range(0,len(q)):
    print(q[j]["question"])
    for i in range(0,4):
        print(q[j]["option"][i])
    choice=eval(input("enter your choice"))
    if choice == q[j]["answer"]:
        Score= Score + 1
    else:
        Score = Score - .25
print("YOUR SCORE : ",Score)         
    
    
