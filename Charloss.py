import os, glob
import random
delpath = (random.choice(glob.glob("C:/Users/Alex/PycharmProjects/colonygame/home/charsheet/*.py")))
delpath2 = delpath
os.remove(delpath2)
smithingskill = int(smithingskill)
combatskill = int(combatskill)
geologyskill = int(geologyskill)
miningskill = int(miningskill)
huntingskill = int(huntingskill)
huntingbonus = huntingbonus - huntingskill
smithingbonus = smithingbonus - smithingskill
combatbonus = combatbonus - combatskill
geologybonus = geologybonus - geologyskill
miningbonus = miningbonus - miningskill
