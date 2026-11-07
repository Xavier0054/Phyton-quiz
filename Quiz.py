import csv
from csv import reader,writer


def read_file (filename ):
    f = open(filename, "r")
    r= reader(f)
    user = list(r)
    f.close()
    return user






#def check (username, pw, users):
    
    
users = read_file("user.csv ")
Name = input ("what is you name: ")
Age= input ("what is your age: ")
Year_group= input ("what is your year group: ")
password= input("what password would you like: ")
name_bit =(Name[0:3])
Username = (name_bit + Age)
print ("Your username is " + Username)
score = 0
B=0
data = [["Username"],[ Username], ["password"], [password] ,["name"], [Name] ,["age"], [Age], ["year group"], [Year_group]]

print (data)
yes = ("yes")
#with open('user', 'w',newline="") as my_csv:
 #   csv_object =writer(my_csv)
  #  csv_object.writerows(data)
   # my_csv.close()
f = open("user.csv", "w", newline="")
w = csv.writer(f)
w.writerows(data)
f.close()

print (Name + " what topic would you like to do")
topic_pick= input("• history • music • computer science: ")

if topic_pick == "history":
    rating = input("easy, medium or hard:")
    if rating == "easy":
        B = 5
        eh1 = input("""Who was the first President of the United States?   :
                       A- Thomas Jefferson
                       B- George Washington
                       """)
        if eh1 == "B":
            print(yes)
            score = score + 1
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(1))
        else:
            print("no it was: B")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        eh2 = input("""Which ancient civilization built the Great Pyramids of Giza?   :
                       A-The Ancient Egyptians
                       b-The Ancient Greeks
                       """)
        if eh2 == "A":
            print(yes)
            score = score + 1
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(1))
        else:
            print("no it was:A ")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        eh3 = input("""In which century did Christopher Columbus first reach the Americas (1492)?   :
                    A-15th Century
                    B-14th Century
                    """)
        if eh3 == "A":
            print(yes)
            score = score + 1
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(1))
        else:
            print("no it was:15th Century ")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        eh4 = input("""Which country gifted the Statue of Liberty to the United States?   :
                    A-France
                    B-United Kingdom
                    """)
        if eh4 == "A":
            print(yes)
            score = score + 1
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(1))
        else:
            print("no it was: France  ")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        eh5 = input("""Which major world war lasted from 1939 to 1945?   :
                    A- World War I
                    B- World War II
                    """)
        if eh5 == "B":
            print(yes)
            score = score + 1
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(1))
        else:
            print("no it was: World War II   ")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
    
                

    if rating == "medium":
        B = 10
        mh1 = input("""Which treaty officially ended World War I in 1919?   :
                    A-Treaty of Paris
                    B-The Treaty of Versailles
                    C-Treaty of Utrecht
                    """)
        if mh1 == "B":
            print("yes")
            score = score + 2
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(2))
        else:
            print("no it was:The Treaty of Versailles")
            
            
        mh2 = input("""Which English monarch broke away from the Roman Catholic Church to establish the Church of England?   :
                    A-Henry VIII
                    B-Henry IIV
                    C-henry IX
                    """)
        if mh2 == "A":
            print("yes")
            score = score + 2
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(2))
        else:
            print("no it was: Henry VIII  ")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        mh3 = input("""In what year did the French Revolution begin with the Storming of the Bastille?   :
                    A-1796
                    B-1798
                    C-1789
                    """)
        if mh3 == "C":
            print("yes")
            score = score + 2
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(2))
        else:
            print("no it was: 1789  ")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        mh4 = input("""Which ancient trade route connected China to the Mediterranean world for centuries?   :
                    A-The Amber Road
                    B-The Incense Route
                    C-The Silk Road
                    """)
        if mh4 == "C":
            print("yes")
            score = score + 2
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(2))
        else:
            print("no it was: The Silk Road  ")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        mh5 = input("""In which battle was Napoleon Bonaparte final defeated in 1815?   :
                    A-Battle of Waterloo
                    B-Battle of Austerlitz
                    C-Battle of Leipzig
                    """)
        if mh5 == "A":
            print("yes")
            score = score + 2
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(2))
        else:
            print("no it was: Battle of Waterloo  ")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(0))



    if rating == "hard":
        B = 20
        hh1 = input("""Which ancient empire was ruled by King Ashoka during the 3rd century BCE following the conquest of Kalinga?   :
                    A-The Gupta Empire
                    B-The Maurya Empire
                    C-The Mughal Empire
                    """)
        #Answer: The Maurya Empire
        if hh1 == "B":
            print("yes")
            score = score + 4
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(4))
        else:
            print("no it was:The Maurya Empire")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(0))
        
        hh2 = input("""Which ancient mesoamerican civilization built the city of Tikal, one of its primary urban centers during the Classic Period?   :
                    A-The Maya Civilization
                    B-The Inca Civilization
                    c-The Aztec Civilization
                    """)
        if hh2 == "A":
            print("yes")
            score = score + 4
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(4))
        else:
            print("no it was:The Maya Civilization ")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        hh3 = input("""In 1215, which English king was forced by his rebel barons to sign the Magna Carta at Runnymede?   :
                    A-King Henry II
                    B-King Richard I
                    C-King Jonhn
                    """)
        if hh3 == "C":
            print("yes")
            score = score + 4
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(4))
        else:
            print("no it was: King John")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(0))
            
        hh4 = input("""Which ancient city-state's defeat in the Sicilian Expedition (415–413 BCE) marked a major turning point in the Peloponnesian War?   :
                    A-Corinth
                    B-Sparta
                    C-Athens
                    """)
        if hh4 == "C":
            print("yes")
            score = score + 4
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(4))
        else:
            print("no it was:Athens")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(0)) 
        
        hh5 = input("""Which ancient Mesopotamian ruler is best known for issuing one of the earliest and most complete written legal codes around 1750 BCE?   :
                    A-Hammurabi
                    B-Sargon of Akkad
                    C-Ashurbanipal
                    """)
        if hh5 == "A":
            print("yes")
            score = score + 4
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(4))
        else:
            print("no it was:Hammurabi")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(0)) 
        
        
        
        
        
elif topic_pick == "music":
    rating = input("""easy, medium or hard:""")
    if rating == "easy":
        B = 5
        em1 = input("""How many strings does a standard acoustic guitar have?   :
                    A-3
                    B-6
                    C-5""")
        if em1 == "B":
            print("yes")
            score = score + 1
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        em2 = input("""Which instrument has black and white keys that you press to make sound?   :
                   A) Piano
                   B) Flut
                   C) Drums """)
        if em2 == "A":
            print("yes")
            score = score + 1
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:A")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        em3 = input("""Which member of a band typically keeps the rhythm using sticks?  :
                    A) Guitarist
                    B) Singer
                    C) Drummer""")
        if em3 == "C":
            print("yes")
            score = score + 1
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:C")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        em4 = input("""How many lines make up a standard musical staff?   :
                    A) 4
                    B) 5
                    C) 6 """)
        if em4 == "B":
            print("yes")
            score = score + 1
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))

        em5 = input("""Which family of instruments does the trumpet belong to?   :
                    A) Woodwind
                    B) Brass
                    C) Percussion""")
        if em5 == "B":
            print("yes")
            score = score + 1
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")        
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
    elif rating == "medium":
        B = 10
        mm1 = input("Which musical term directs a performer to play gradually louder?   : ")
        #Answer: Crescendo (often abbreviated as cresc.)
        if mm1 == "crescendo":
            print("yes")
            score = score + 2
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:Crescendo")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mm2 = input("""What term refers to the speed or pace at which a piece of music is played?   :
                    A) Tempo
                    B) Dynamics
                    C) Pitch""")
        if mm2 == "A":
            print("yes")
            score = score + 2
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:A")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mm3 = input("""Which woodwind instrument uses a single reed attached to a mouthpiece?   :
                    A) Flute
                    B) Oboe
                    C) Clarinet""")
        if mm3 == "C":
            print("yes")
            score = score + 2
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:C")    
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mm4 = input("""In music theory, what is the distance in pitch between two notes called?   :
                    A) Octave
                    B) Interval
                    C) Scale""")
        if mm4 == "B":
            print("yes")
            score = score + 2
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mm5 = input("""Which classical composer wrote the famous orchestral work "The Four Seasons"?   :
                    A) Antonio Vivaldi
                    B) Johann Sebastian Bach
                    C) Wolfgang Amadeus Mozart """)
        if mm5 == "A":
            print("yes")
            score = score + 2
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:A")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
               
    elif rating == "hard":
        B = 20
        hm1 = input("In music theory, what is the specific name for a chord built using the 1st, 3rd, 5th, and 7th degrees of a major scale?   : ")
        #Answer: Major seventh chord (e.g., C–E–G–B)
        if hm1 == "major seventh chord":
            print("yes")
            score = score + 4
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:Major seventh chord")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hm2 = input("""Which form of musical composition features a recurring main theme (A) alternating with contrasting sections (e.g., A–B–A–C–A)?   :
                    A) Rondo form
                    B) Sonata form
                    C) Ternary form""") 
        if hm2 == "A":
            print("yes")
            score = score + 4
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:A")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hm3 = input("""Which mode is built on the 5th degree of the major scale and is commonly used in jazz and blues for its dominant sound?   :
                    A) Dorian
                    B) Mixolydian
                    C) Phrygian """) 
        if hm3 == "B":
            print("yes")
            score = score + 4
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B") 
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        hm4 = input("""What is the name of the contrapuntal technique where a musical phrase is repeated by another voice in exact reverse (backwards)?   :
                    A) Inversion
                    B) Retrograde
                    C) Augmentation """) 
        if hm4 == "B":
            print("yes")
            score = score + 4
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")    
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hm5 = input("""Which late-19th-century musical movement, associated with composers likeClaude Debussy, emphasized atmosphere and subtle tone color over traditional harmonic structure?"   :
                    A) Expressionism
                    B) Serialism
                    C) Impressionism""") 
        if hm5 == "C":
            print("yes")
            score = score + 4
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:C")    
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
            

elif topic_pick == "computer science":
    rating = input("easy, medium or hard:")
    if rating == "easy":
        B=5
        ec1 = input("What does \"HTML\" stand for in web development?   : ")
        if ec1 == "hypertext markup language":
            print("yes")
            score = score + 1
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:HyperText Markup Language")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        ec2 = input("""Which part of a computer is often referred to as its "brain"?   :
                    A) Hard Drive
                    B) CPU (Central Processing Unit)
                    C) RAM (Random Access Memory) """)
        if ec2 == "B":
            print("yes")
            score = score + 1
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        ec3 = input("""What is the main function of computer RAM?   :
                    A) Permanent long-term storage of files
                    B) Temporary short-term memory for active tasks
                    C) Cooling down the processor components """)
        if ec3 == "B":
            print("yes")
            score = score + 1
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:B ")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        ec4 = input("""What binary digits are used in base-2 computer code?   :
                    A) 0 and 1
                    B) 1 and 2
                    C) 0 and 10 """)
        if ec4 == "A":
            print("yes")
            score = score + 1
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:A ")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score)) 
            
        ec5 = input("""Which software program manages computer hardware and allows applications to run?   :
                    A) Web Browser
                    B) Operating System
                    C) Text Editor""")
        if ec5 == "B":
            print("yes")
            score = score + 1
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was B")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))     
            
            
        
    elif rating == "medium":
        B=10
        mc1 = input("""What is the average time complexity of searching for an element in a balanced Binary Search Tree (BST)?   :
                    A)O(\log n)
                    B)O(log\n)
                    C)0 log n""")
        if mc1 == "A":
            print("yes")
            score = score + 2
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:O(\log n)")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mc2 = input("""Which data structure operates on a Last-In, First-Out (LIFO) basis?   :
                    A) Stack
                    B) Queue
                    C) Array""")
        if mc2 == "A":
            print("yes")
            score = score + 2
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was: Stack")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))   
            
        mc3 = input("""What is the primary function of a compiler in programming?   :
                    A) Execute code line-by-line in real time
                    B) Translate source code into machine code all at once
                    C) Manage database queries and storage """)
        if mc3 == "B":
            print("yes")
            score = score + 2
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:Translate source code into machine code all at once")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        mc4 = input("""In object-oriented programming, what is the process of hiding internal implementation details and exposing only necessary interfaces called?   :
                    A) Polymorphism
                    B) Inheritance
                    C) Encapsulation """)
        if mc4 == "C":
            print("yes")
            score = score + 2
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:Encapsulation")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        
        mc5 = input("""Which layer of the OSI model is responsible for routing data packets across different networks using IP addresses?   :
                    A) Transport Layer
                    B) Network Layer
                    C) Data Link Layer""")
        if mc5 == "B":
            print("yes")
            score = score + 2
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print("no it was:Network Layer")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score)) 
            
            
            
        
    elif rating == "hard":
        B= 20
        hc1 = input("In operating systems, what are the four necessary conditions required for a deadlock to occur (known as the Coffman conditions)?   : ")
        if hc1 == "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait":
            print ("yes")
            score = score + 4
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print ("no it was: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait")
            s1 = (topic_pick + " - "+rating +" -  score: "+ str(score))
               
        hc2 = input("""In relational database design, a table is in 3rd Normal Form (3NF) if it is in 2NF and has no...   :
                    A) Partial dependencies
                    B) Transitive dependencies
                    C) Multi-valued dependencies""")
        if hc2 == "B":
            print ("yes")
            score = score + 4
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print ("no it was:Transitive dependencies ")
            s2 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hc3 = input("""Which protocol in distributed systems ensures atomic commit across multiple node transactions despite network partitions or failures?   :
                    A) Two-Phase Commit (2PC)
                    B) Domain Name System (DNS)
                    C) Address Resolution Protocol (ARP)""")
        if hc3 == "A":
            print ("yes")
            score = score + 4
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print ("no it was:Two-Phase Commit (2PC)")
            s3 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hc4 = input("""In compiler design, which parsing technique processes input from left to right to produce a Rightmost derivation in Reverse?   :
                    A) LL(1) Parser
                    B) LALR Parser
                    C) Recursive Descent Parser""")
        if hc4 == "B":
            print ("yes")
            score = score + 4
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print ("no it was :LALR Parser ")
            s4 = (topic_pick + " - "+rating +" -  score: "+ str(score))
            
        hc5 = input("""In computational complexity theory, which class consists of decision problems solvable by a deterministic Turing machine in polynomial time?   :
                    A) NP
                    B) P
                    C) PSPACE""")
        if hc5 == "A":
            print ("yes")
            score = score + 4
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score))
        else:
            print ("no it was: P ")
            s5 = (topic_pick + " - "+rating +" -  score: "+ str(score)) 
            
            
            
            
            
            
            
print("""_____________________________________________________________________
#####################################################################
---------------------------------------------------------------------""")
print (Username) 
print ( "your score is: ",score," out of ",str(B))
string_score = str(score)
data2 = [["Username"], [Username],["score"], [string_score], [s1], [s2],[s3],[s4],[s5]]

with open('score', 'w',newline="") as my_csv:
    csv_object =writer(my_csv)
    csv_object.writerows(data2)
    my_csv.close()

