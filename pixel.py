
#sudo pip install Pillow

#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import math
from array import *
import json
import os

class PixelData(object):
    R=0
    G=0
    B=0
    Key=""
    number=0

        

def make_regalur_image(img, size = (50, 50)):
    return img.resize(size).convert('RGBA')

def greyColor(color):
    R=color[0]
    G=color[1]
    B=color[2]
    A=color[3]

    if(A<255):
        A=0
        R=0
        G=0
        B=0
    else:
        A=255
    #value=int(R*0.3+G*0.59+B*0.11)
    #R=value
    #G=value
    #B=value



    return R,G,B,A


def compare(dict,R,G,B):
    minDis=255
    targetKey=None
    for key in dict:
        pixelData=dict[key]
        disR=pixelData.R-R
        disG=pixelData.G-G
        disB=pixelData.B-B
        value=math.sqrt(disR*disR+disG*disG+disB*disB)
        if value<minDis:
            minDis=value
            targetKey=key
    if minDis<20:
        return targetKey
    return None

def pixelSort(pixelData1,pixelData2):
    if pixelData1.number>pixelData2.number:
        return -1
    elif pixelData1.number<pixelData2.number:
        return 1
    else:
        return 0

def getColorDict(pixL,w,h):
    colorsDict={}
    for j in xrange(0,h):
        for i in xrange(0,w):
            R=pixL[i,j][0]
            G=pixL[i,j][1]
            B=pixL[i,j][2]
            A=pixL[i,j][3]
            if A==255:
                targetKey=compare(colorsDict,R,G,B)
                if targetKey==None:
                    key=str(R)+"_"+str(G)+"_"+str(B)
                    pixelData=PixelData()
                    pixelData.key=key
                    pixelData.R=R
                    pixelData.G=G
                    pixelData.B=B
                    pixelData.number=1
                    colorsDict[key]=pixelData
                else:
                    pixelData=colorsDict[targetKey]
                    pixelData.number=pixelData.number+1
                    colorsDict[targetKey]=pixelData

    return colorsDict

def getSortValues(colorsDict):
    values=[]
    for key in colorsDict:
        values.append(colorsDict[key])
    values.sort(pixelSort)
    return values

def getIndexAndDistance(sortValues):
    index=len(sortValues)
    targetNumber=20
    distance=30

    while index>targetNumber:
        for pixelData in sortValues:
            if pixelData.number<distance:
                index=sortValues.index(pixelData)
                break
        if index>targetNumber:
            distance=distance+5
    if index<=5:
        distance=20
        index=len(sortValues)
        while index>targetNumber:
            for pixelData in sortValues:
                if pixelData.number<distance:
                    index=sortValues.index(pixelData)
                    break
                if index>targetNumber:
                    distance=distance+5
    if index<=5:
        distance=10
        index=len(sortValues)
        while index>targetNumber:
            for pixelData in sortValues:
                if pixelData.number<distance:
                    index=sortValues.index(pixelData)
                    break
                if index>targetNumber:
                    distance=distance+5
    return index,distance

def getColorimeterWithList(mList,R,G,B):
    minDis=255
    mIndex=-1
    for value in mList:
        lR=value[0]
        lG=value[1]
        lB=value[2]

        disR=lR-R
        disG=lG-G
        disB=lB-B

        sqrtValue=math.sqrt(disR*disR+disG*disG+disB*disB)
        if sqrtValue<minDis:
            minDis=sqrtValue
            mIndex=mList.index(value)

    if(minDis<64):
        return mIndex
    else:
        return -1


def cleanDir(name):

    print("--------cleanDir")

    #remove zip file
    zip_path = "./" + name + ".zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)
    else:
        print("The file does not exist: " + zip_path)

    for i in range(5):
        image_name = name + "_" + str(i+1) + "_gray.png"
        image_path = "./" + name + "/" + image_name
        json_path = "./" + name + "/" + name + "_" + str(i+1) + ".json"
        other_file_path = "./" + name + "/" + "Thumbs.db"

        #remove image file
        if os.access(image_path, os.F_OK):
            os.remove(image_path)
        else:
            print("The file does not exist: " + image_path)

        #remove json file
        if os.path.exists(json_path):
            os.remove(json_path)
        else:
            print("The file does not exist: " + json_path)

        #remove other file
        if os.path.exists(other_file_path):
            os.remove(other_file_path)
        else:
            print("The file does not exist: " + other_file_path)




def handleImage(folder, path, filename, difficulty):

    print("-----handleImage")

    name=os.path.splitext(filename)[0]

    print(">>>>>>>name: " + name)
    print(">>>>>>>path: " + path)

    size = (50, 50)
    if difficulty == 'normal':
        size = (70,70)
    elif difficulty == 'hard':
        size = (100,100)

    img=make_regalur_image(Image.open(path), size)
    pixL=img.load()
    #print type(pixL)

    w,h=img.size
    for j in xrange(0,h):
        for i in xrange(0,w):
            pixL[i,j]=greyColor(pixL[i,j])

    colorsDict=getColorDict(pixL,w,h)
    #print type(colorsDict)
    
    sortValues=[]
    for key in colorsDict:
        sortValues.append(colorsDict[key])
    sortValues.sort(pixelSort)
    
    index,distance=getIndexAndDistance(sortValues)
    #print index,distance

    numberDict={}
    colorsValueList=[]
    if len(sortValues)>=index:
        for pixelData in sortValues:
            R=pixelData.R
            G=pixelData.G
            B=pixelData.B
            mList=[R,G,B]
            xindex=sortValues.index(pixelData)
            if xindex<=index:
                colorsValueList.append(mList)
                mkey=str(xindex)
                numberDict[mkey]=mList
    else:
        for pixelData in sortValues:
            xindex=len(colorsValueList)
            R=pixelData.R
            G=pixelData.G
            B=pixelData.B
            mList=[R,G,B]
            colorsValueList.append(mList)
            numberDict[str(xindex)]=mList

    numberList=[]
    for j in xrange(0,h):
        rowList=[]
        for i in xrange(0,w):
            R=pixL[i,j][0]
            G=pixL[i,j][1]
            B=pixL[i,j][2]
            A=pixL[i,j][3]
            if A<255:
                R=0
                G=0
                B=0
                A=0
                rowList.append(-1)
            else:
                rate=A/255.0
                R=int(R*rate)
                G=int(G*rate)
                B=int(B*rate)
                A=255
                mIndex=getColorimeterWithList(colorsValueList,R,G,B)
                if mIndex>=0:
                    rowList.append(mIndex)
                else:
                    mIndex=len(colorsValueList)
                    rowList.append(mIndex)
                    mList=[R,G,B]
                    colorsValueList.append(mList)
                    mKey=str(mIndex)
                    numberDict[mKey]=mList

            greyValue=int(R*0.3+G*0.59+B*0.11)
            # pixL[i,j]=(R,G,B,A)
            pixL[i,j]=(greyValue,greyValue,greyValue,A)

        numberList.append(rowList)

    jsonDict={}
    jsonDict["palette"]=numberDict
    jsonDict["pixel_map"]=numberList

    jsonFile= folder + name + ".json"
    #print jsonFile
    with open(jsonFile,"w") as f:
        f.write(json.dumps(jsonDict))
        f.close()


    newImg=Image.new("RGBA",(w*2,h*2))
    pixNew=newImg.load()
    newW,newH=newImg.size
    for j in xrange(0,newH):
        for i in xrange(0,newW):
            x=int(i/2)
            y=int(j/2)
            pixNew[i,j]=pixL[x,y]

    savePath = folder + name + "_gray.png"
    newImg.save(savePath)
            



# g = os.walk(r"./")  
# for path,dir_list,file_list in g:  
#     for file_name in file_list:  
#         #print(os.path.join(path, file_name) )
#         #print(os.path.splitext(file_name)[-1])
#         if(os.path.splitext(file_name)[-1] == '.png'):
#             #print(file_name)
#             operationImage(os.path.splitext(file_name)[0])
            


# read json file
def readConfig(filename):
    with open(filename) as configFile:

        data = json.load(configFile)
        items = data['all']

        index = 0
        for item in items:
            name = item["name"]
            difficulty = item["difficulty"]

            if len(name) > 0:
                #clean files
                for i in range(5):
                    folder = "./" + name + "/"

                    if os.access(folder, os.F_OK) == False:
                        print("Folder is not exist: " + folder + "\n")
                        continue

                    cleanDir(name)


                #handle images
                for i in range(5):
                    image_name = name + "_" + str(i+1) + ".png"
                    image_path = "./" + name + "/" + image_name
                    folder = "./" + name + "/"

                    if os.access(image_path, os.F_OK) == False:
                        print("image path is not exist: " + image_path + "\n")
                        continue

                    handleImage(folder,image_path,image_name,difficulty)
                    os.system("zip -r " + name + ".zip " + name)


            index = index + 1

            if index >= 5:
                break


readConfig("items.json")





