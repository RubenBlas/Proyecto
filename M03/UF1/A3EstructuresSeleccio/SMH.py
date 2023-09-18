HMS = input()
HMSs = HMS.split( )
#
if len(str(HMSs[0])) == 2 and len(str(HMSs[1])) == 2 and len(str(HMSs[2])) == 2:

    HMSs[0] = round(((float(HMSs[0])/24 - round(float(HMSs[0]))//24)*24) + round(float(HMSs[1]))//60)
    HMSs[1] = round(((float(HMSs[1])/60 - round(float(HMSs[1]))//60)*60) + round(float(HMSs[2]))//60)
    HMSs[2] = round((float(HMSs[2])/60 - round(float(HMSs[2]))//60)*60)

    HMSs[0] = round(((float(HMSs[0])/24 - round(float(HMSs[0]))//24)*24) + round(float(HMSs[1]))//60)
    HMSs[1] = round(((float(HMSs[1])/60 - round(float(HMSs[1]))//60)*60) + round(float(HMSs[2]))//60)
    HMSs[2] = round((float(HMSs[2])/60 - round(float(HMSs[2]))//60)*60)

else:
    print("Flipao! Donde vas? Escribelo asi: xx xx xx")

if len(str(HMSs[0])) == 1:
    HMSs[0] = "0"+(str(HMSs[0]))
if len(str(HMSs[1])) == 1:
    HMSs[1] = "0"+(str(HMSs[1]))
if len(str(HMSs[2])) == 1:
    HMSs[2] = "0"+(str(HMSs[2]))

HMS = (str(HMSs[0]) + ":" + str(HMSs[1]) + ":" + str(HMSs[2]))

print(HMS)

if len(str(HMSs[0])) == 2 and len(str(HMSs[1])) == 2 and len(str(HMSs[2])) == 2:
    S = input("Cuantos segundos quieres añadir? ")

    HMSs[0] = round(((float(HMSs[0])/24 - round(float(HMSs[0]))//24)*24) + round(float(HMSs[1]))//60)
    HMSs[1] = round(((float(HMSs[1])/60 - round(float(HMSs[1]))//60)*60) + round(float(HMSs[2]))//60)
    HMSs[2] = round((float(HMSs[2])/60 - round(float(HMSs[2]))//60)*60) + float(S)

    HMSs[0] = round(((float(HMSs[0])/24 - round(float(HMSs[0]))//24)*24) + round(float(HMSs[1]))//60)
    HMSs[1] = round(((float(HMSs[1])/60 - round(float(HMSs[1]))//60)*60) + round(float(HMSs[2]))//60)
    HMSs[2] = round((float(HMSs[2])/60 - round(float(HMSs[2]))//60)*60)

print(HMS)


