#Bemaßungsfunktion für Grafiken
def annotate_dim(ax,xyfrom,xyto,angle=0,versatz=False,text=None):
    import numpy as np

    #Bemaßungstext runden und ohne Dezimalstellen ausgeben
    if text is None:
        text = str(np.round(np.sqrt( (xyfrom[0]-xyto[0])**2 + (xyfrom[1]-xyto[1])**2 ),decimals=0).astype(int))

    #Bemaßungslinie
    ax.annotate("",xyfrom,xyto,arrowprops=dict(arrowstyle='|-|, widthA=0.3, widthB=0.3',shrinkA=0,shrinkB=0))
    
    #Horizontale Bemaßung bis 45° als horizontalen Text ausgeben
    if angle <=45:
        if versatz:
            #Versatz des Texts im Falle von kleinen Zahlen. Versatz geht in umgekehrte Richtung (dH right -> text rückt nach links)
            ha="right"
        else:
            ha="center"
        ax.text((xyto[0]+xyfrom[0])/2,(xyto[1]+xyfrom[1])/2,text,fontsize=18,rotation=angle, 
                        fontstretch="ultra-condensed", fontweight="bold",horizontalalignment=ha,
                        verticalalignment="bottom")
    
    #Vertikale Bemaßung als vertikalen Text ausgeben
    elif angle == 90:
        if versatz:
            #Versatz des Texts im Falle von kleinen Zahlen. Versatz geht in umgekehrte Richtung
            va="top"
        else:
            va="center"
        ax.text((xyto[0]+xyfrom[0])/2,(xyto[1]+xyfrom[1])/2,text,fontsize=18,rotation=angle, 
                            fontstretch="ultra-condensed", fontweight="bold",horizontalalignment="right",  
                            verticalalignment=va)

#---------------------------------------------------------------------------


#CreateFigures-Funktion erzeugt Grafik und Beschriftungen
def createFigures(filename,folder):

    import os
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib import font_manager
    from matplotlib import rc
    import xml.etree.ElementTree as et
    from .variables import profilausnahme,fontsdir

    ospath=os.path.dirname(os.path.realpath(__name__))
    fonts=os.path.join(ospath,str(fontsdir))

    for font in font_manager.findSystemFonts(fonts):
        font_manager.fontManager.addfont(font)

    foldername=str(folder)+"/"+str(os.path.basename(str(filename)))+"_figures"
    ############################################
    #Anpassen für Verwendung spezifischer XML-Dateien
    ################################################
    #XML-Datei finden (relative Pfadangabe)
    tree = et.parse(str(filename))
    #################################################

    #Einlesen Abschnitt PositionList in XML
    root=tree.getroot()
    root.findall('./PositionList')


    ######################################################
    #Anpassen - Ausgabe in Ordner mit Bestellnummer
    ######################################################
    #Unterverzeichnis figures anlegen, falls noch nicht existent
    if not os.path.isdir(foldername):
        os.mkdir(foldername)
    ###########################################################
    #Array für Erstellung eines Pandas Dataframe aus XML-Inhalt
    data=[]

    #Durch XML-Datei iterieren zur Ausgabe der Grafik als Einzellinien
    for child in root.findall('./PositionList/Position'):

        

        for OrderPosNo in child.findall('./OrderPosNo'):

            #->Ausgabe der Positionsnummer. Für Debugzwecke kommentarmarke entfernen
            #print("Pos: ",OrderPosNo.text)
            #Bestehende Figures schließen
            plt.close('all')
            #Neues Figure ausgeben

    #############################################################################
    #Sicherstellen dass Helvetica-Schriftart im richtigen Ordner installiert ist!!
    #Ansonsten wird automatisch auf eine andere Schriftart umgestellt
    ##Ordnerpfad für Schriftart ermitteln und cache-Datei löschen.
    #Zur Ermittlung der Ordnerpfade:
    #
    #import matplotlib
    #from matplotlib import get_cachedir
    #print(matplotlib.matplotlib_fname())
    #print(get_cachedir())
    #################################################################################
            #Schriftart Helvetica für Textstellen verwenden
            rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
            
            #Grafik mit Fensterrahmen wird in einen 1x4 Subplott geplottet, wobei 3/4
            #von der Fenstergrafik verwendet werden. 1/4 wird weiter unten für die
            #Tabelle herangezogen
    #        ax=fig.add_subplot(1,4,(1,3))

            #Frames entsprechen Fensterabschnitten
            #Vollständige Rahmen und Flügel werden werden aus XML-Abschnitt Frames entnommen
            for Frame in child.findall('./FrameList/Frame'):
                framedim=[]
                #->Für Debugzwecke Kommentarmarke entfernen
                #print("-->Frame:", Frame[1].text)

                #Parts entsprechen Rahmen- und Flügelelementen
                #Rahmen oben, unten, Flügelelement links, rechts, ... werden aus XML-Abschnitt Parts entnommen
                for Part in Frame.findall("./PartList/Part"):
                    #->Für Debugzwecke Kommentarmarke entfernen
                    #print("   -->Part:", Part[1].text)
                    
                    if Part.find("Profile").text in profilausnahme:
                        continue
                    else:
                        
                        
                        for Edge in Part.findall("./EdgeList/Edge"):
                            #Linien Zeichnen
                            #x=[round(float(Edge.find("X1").text)), round(float(Edge.find("X2").text))]
                            #y=[round(float(Edge.find("Y1").text)), round(float(Edge.find("Y2").text))]
                            #plt.plot(x, y, color='black')

                            #Daten für Pandas Dataframe, zur Bemaßung
                            data.append([OrderPosNo.text,Frame.find("FrameIndex").text,Frame.find("Width").text,Frame.find("Height").text,Part.find("PartShort").text,str(Edge.find("EdgePos").text),
                                float(Part.find("Width").text),float(Edge.find("X1").text), float(Edge.find("X2").text),float(Edge.find("Y1").text), float(Edge.find("Y2").text)])
    ####################################################################################################
    ################Vermutliche Performanceeinbußen in diesem Abschnitt durch übergeordnete For-Schleife
    ####################################################################################################
        #Pandas Dataframe für Bemaßung der Hauptabschnitte des Fensters + Rahmen
    df=pd.DataFrame(data, columns=["Pos","Frame","FWidth","FHeight","PartShort","EdgePos","Width","X1","X2","Y1","Y2"])
    plt.close('all')
    for Pos in df["Pos"].drop_duplicates():
        plt.close('all')
        fig = plt.figure()

        ax=fig.add_subplot(1,5,(1,3))
        #df[df["Pos"].isin([str(Pos)])].sort_values(by=['Y1'])["Y1"].drop_duplicates()
        #x=[round(float(Edge.find("X1").text)), round(float(Edge.find("X2").text))]
        #y=[round(float(Edge.find("Y1").text)), round(float(Edge.find("Y2").text))]
        df1=df[df["Pos"].isin([str(Pos)])]
        x=[df1[df1["Pos"].isin([str(Pos)])]["X1"].to_numpy(),df1[df1["Pos"].isin([str(Pos)])]["X2"].to_numpy()]
        y=[df1[df1["Pos"].isin([str(Pos)])]["Y1"].to_numpy(),df1[df1["Pos"].isin([str(Pos)])]["Y2"].to_numpy()]
        plt.plot(x, y, color='black')
        
        
        #Filtern X-Achsenabschnitte für Rahmenbauteile und Setzholz-Elemente und überschreiben in schnelleres Numpy-Array
        x_data=df1[df1["PartShort"].isin(["RA L", "RA R", "SE", "RA OL", "RA OR", "RVi U", "RVi O"])&df1["EdgePos"].isin(["IN","OUT"])].sort_values(by=['X1'])["X1"].drop_duplicates().to_numpy()

        #Filtern Y-Achsenabschnitte für horizontale und schräge Rahmenbauteile
        ##y_data1=df[df["PartShort"].isin(["RA R", "RA L","RA OL", "RA OR"])&df["EdgePos"].isin(["IN","OUT"])].sort_values(by=['Y1']).drop_duplicates()
        #Ergänzung der Y-Achsenabschnitte um Kämpfer-Elemente
        ##y_data2=df[df["PartShort"].isin(["RA U", "RA O", "KÄ", "RVi U", "RVi O"])&df["EdgePos"].isin(["IN","OUT"])].sort_values(by=['Y1']).drop_duplicates()
        #Zusammenfügen der beiden Filteranwendungen
        ##y_data=pd.concat([y_data1, y_data2])
        #Doppelte
        ##y_data=y_data.sort_values(by=['Y1'])["Y1"].drop_duplicates().to_numpy()
        
        #Filtern Y-Achsenabschnitte für horizontale schräge Rahmenbauteile, Kämpfer- und Rahmenverbreiterungselemente und überschreiben in schnelleres Numpy-Array
        y_data=df1[df1["PartShort"].isin(["RA R", "RA L","RA OL", "RA OR","RA U", "RA O", "KÄ", "RVi U", "RVi O"])&df1["EdgePos"].isin(["IN","OUT"])].sort_values(by=['Y1'])["Y1"].drop_duplicates().to_numpy()

        #Filtern X- und Y-Achsenabschnitte für Flügelelemente und überschreiben in schnelleres Numpy-Array, Elementaußen- und Innenmaße extra bearbeiten
        x_FLdataIN=df1[df1["PartShort"].isin(["FL L", "FL R"])&df1["EdgePos"].isin(["IN"])].sort_values(by=['X1'])["X1"].drop_duplicates().to_numpy()
        y_FLdataIN=df1[df1["PartShort"].isin(["FL U", "FL O"])&df1["EdgePos"].isin(["IN"])].sort_values(by=['Y1'])["Y1"].drop_duplicates().to_numpy()
        x_FLdataOUT=df1[df1["PartShort"].isin(["FL L", "FL R"])&df1["EdgePos"].isin(["OUT"])].sort_values(by=['X1'])["X1"].drop_duplicates().to_numpy()
        y_FLdataOUT=df1[df1["PartShort"].isin(["FL U", "FL O"])&df1["EdgePos"].isin(["OUT"])].sort_values(by=['Y1'])["Y1"].drop_duplicates().to_numpy()
        
        #Rahmendaten für Ermittlung der Text-Tabelle Außenmaße Rahmen
        ra_data=df1[df1["PartShort"].isin(["RA L", "RA R","RA U", "RA O", "SE", "KÄ", "RVi U","RVi O","RA OL", "RA OR", "RA UL", "RA UR"])&df1["EdgePos"].isin(["OUT"])]


        #Bemaßungen einführen    
        
        #Maximale X- und Y-Position für Bemaßungsposition in Plot. Initialisieren der Variablen
        x_max=x_data[-1]
        x_maxmax=x_max
        y_max=y_data[-1]
        y_maxmax=y_max
        x_minmin=0
        y_minmin=0
    #    y_max=np.amax(y_rahmen)
        clr="black"
        #arsz=20
        #tsz=16
        #Zeilenabstand
        dist=120


    #----------------------------------------------------------------------
        #horizontale Rahmenelemente unten bemaßen
        #j für Distanz zw. Bemaßungspfeilen
        j=0
        #last_element für Nebeneinander od. Untereinandersetzen der Bemaßungspfeile
        last_element=0
        x_rahmen1=[0]
        x_rahmen2=[0]
        #k für zurücksetzen des Bemaßungsabstands
        k=False
        last_laenge=0
        #Bemaßung Gesamtrahmen
        x_rahmen1=np.append(x_rahmen1,x_data[0])
        x_rahmen2=np.append(x_rahmen2,x_data[-1])
        #Bemaßung Maßkette
        x_rahmen1=np.append(x_rahmen1,x_data[:-1])
        x_rahmen2=np.append(x_rahmen2,x_data[1:])
        #rahmen_masskette_x="Rahmen Maßkette H: |"
        

        for x1,x2 in zip(x_rahmen1,x_rahmen2):
            if x1!=x2:

                #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungshöhe dargestellt werden

                if last_element <= x1:
                    #if last_laenge > 200:
                    #    if k and j>2:
                    #        j=j-1
                    #        k=False
                    #    else:
                    #        j=j
                    if k and j >2 and last_laenge >=100:
                        #Erst ab zweitem Durchlauf - Rücksetzen auf vorige Bemaßungszeile
                        j=j-1
                        k=False        
                    else:
                        j=j+1
                        k=True
                else:
                    j=j+1
                    #k=True


                #Abstände der Bemaßungen, relativ zur Objektgröße
                y=np.round(0-j*dist)
                if y_minmin > y:
                    y_minmin=y
                laenge=int(np.round(abs(x2-x1),0))
                if abs(x2-x1)<10:
                    versatz=True
                else:
                    versatz=False

                #print("Trial: x1, x2, y "+ str(x1)+" "+str(x2)+" " +str(y))
                if x1 != 0 or x2 !=0:
                    annotate_dim(ax,[x1,y],[x2,y],0,versatz)
                last_element=x2
                last_laenge=laenge


    #-----------------------------------------------------------------------
        #vertikale Rahmenelemente rechts bemaßen
        #j für Distanz zw. Bemaßungspfeilen
        last_element=0
        j=0
        y_rahmen1=[]
        y_rahmen2=[]
        k=False
        last_laenge=0

        #Bemaßung Gesamtrahmen
        y_rahmen1=np.append(y_rahmen1,y_data[0])
        y_rahmen2=np.append(y_rahmen2,y_data[-1])
        #Bemaßung Maßkette
        y_rahmen1=np.append(y_rahmen1,y_data[:-1])
        y_rahmen2=np.append(y_rahmen2,y_data[1:])
        
        for y1,y2 in zip(y_rahmen1,y_rahmen2):
            #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungshöhe dargestellt werden
            if y1!=y2:

                #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungshöhe dargestellt werden

                if last_element <= y1:
                    #if last_laenge > 200:
                    #    if k and j>2:
                    #        j=j-1
                    #        k=False
                    #    else:
                    #        j=j
                    if k and j >2 and last_laenge >=100:
                        #Erst ab zweitem Durchlauf - Rücksetzen auf vorige Bemaßungszeile
                        j=j-1
                        k=False        
                    else:
                        j=j+1
                        k=True
                else:
                    j=j+1
                    #k=True
            
            #Abstände der Bemaßungen, relativ zur Objektgröße
            #x=np.round(x_max+dist+j*dist)
            x=np.round(x_max+j*dist)
            if x_minmin > x:
                x_minmin=x
            if x_maxmax < x:
                x_maxmax=x

            #Versatz des Zahlenwerts in Bemaßung bei sehr kleinem Maß
            if abs(y2-y1)<10:
                versatz=True
            else:
                versatz=False

            if y1 != 0 or y2 !=0:
                annotate_dim(ax,[x,y1],[x,y2],90,versatz)
            laenge=int(np.round(abs(y2-y1),0))
            last_laenge=laenge
            last_element=y2


    #-----------------------------------------------------------------------------------        
        #horizontale Flügelelemente oben bemaßen
        #n für Distanz zw. Bemaßungspfeilen

        last_element=0
        j=0
        k=False
        x_FLrahmen1=[]
        x_FLrahmen2=[]
        last_laenge=0

        x_FLrahmen1=np.append(x_FLrahmen1,x_FLdataIN[:-1])
        x_FLrahmen2=np.append(x_FLrahmen2,x_FLdataIN[1:])
        x_FLrahmen1=np.append(x_FLrahmen1,x_FLdataOUT[:-1])
        x_FLrahmen2=np.append(x_FLrahmen2,x_FLdataOUT[1:])
        
        
        for x1,x2 in zip(x_FLrahmen1,x_FLrahmen2):

            #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungslinie dargestellt werden
            if x1!=x2:

                #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungshöhe dargestellt werden

                if last_element <= x1:
                    #if last_laenge > 200:
                    #    if k and j >2:
                    #        j=j-1
                    #        k=False
                    #    else:
                    #        j=j
                    if k and j >2 and last_laenge >=100:
                        #Erst ab zweitem Durchlauf - Rücksetzen auf vorige Bemaßungszeile
                        j=j-1
                        k=False        
                    else:
                        j=j+1
                        k=True
                else:
                    j=j+1
                    #k=True


            #Abstände der Bemaßungen, relativ zur Objektgröße
            y=y_max+j*dist
            
            if y_maxmax < y:
                y_maxmax=y
            laenge=int(np.round(abs(x2-x1),0))
            if abs(x2-x1)<10:
                versatz=True
            else:
                versatz=False

            if x1 != 0 or x2 !=0:
                annotate_dim(ax,[x1,y],[x2,y],0,versatz)
            
            last_element=x2
            last_laenge=laenge

    #---------------------------------------------------------------------------
        #vertikale Flügelelemente links bemaßen
        #n für Distanz zw. Bemaßungspfeilen    
        j=0
        last_element=0
        y_FLrahmen1=[]
        y_FLrahmen2=[]
        k=False
        last_laenge=0

        y_FLrahmen1=np.append(y_FLrahmen1,y_FLdataIN[:-1])
        y_FLrahmen2=np.append(y_FLrahmen2,y_FLdataIN[1:])
        y_FLrahmen1=np.append(y_FLrahmen1,y_FLdataOUT[:-1])
        y_FLrahmen2=np.append(y_FLrahmen2,y_FLdataOUT[1:])

        for y1,y2 in zip(y_FLrahmen1, y_FLrahmen2):


            #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungslinie dargestellt werden
            if y1!=y2:

                #zwei Bemaßungslinien die nebeneinander gesetzt werden können, sollen in der gleichen Bemaßungshöhe dargestellt werden

                if last_element <= y1:
                    #if last_laenge > 200:
                    #    if k and j>2:
                    #        j=j-1
                    #        k=False
                    #    else:
                    #        j=j
                    if k and j >2 and last_laenge >=100:
                        #Erst ab zweitem Durchlauf - Rücksetzen auf vorige Bemaßungszeile
                        j=j-1
                        k=False        
                    else:
                        j=j+1
                        k=True
                else:
                    j=j+1
                    #k=True
            #Abstände der Bemaßungen, relativ zur Objektgröße
            x=0-j*dist
            laenge=int(np.round(abs(y2-y1),0))
            if x_minmin > x:
                x_minmin = x
            if abs(y2-y1)<10:
                versatz=True
            else:
                versatz=False

            if y1 != 0 or y2 !=0:
                annotate_dim(ax,[x,y1],[x,y2],90,versatz)
            last_element=y2
            last_laenge=laenge


    #Bemaßungshinweise-----------------------------------------------------------------------------------        

                

        #Tabelle generieren mit Außenmaße Rahmenteile
        row_labels=[]
        table_vals=[]
        
        #Außenmaße von Rahmenframe filtern
        for idx, row in df1[df1["PartShort"].isin(["RA U", "RA O"])&df1["EdgePos"].isin(["IN"])].sort_values(by=['X1'])[["Frame","FWidth","FHeight"]].drop_duplicates().iterrows():
            w=(row["FWidth"])
            v=(row["FHeight"])
            row_labels.append("Rahmen Nr." + str(row["Frame"])+"\nAußen:")
            col_labels=['Länge /\nHöhe /mm','Breite /mm']
            table_vals.append([round(float(v),1),round(float(w),1)])
            #print(table_vals)
            
        for idx,row in ra_data.iterrows():
            x_length=(row["X2"]-row["X1"])
            y_length=(row["Y2"]-row["Y1"])
            w=(row["Width"])
            v_length=round((x_length**2+y_length**2)**(1/2),1)
            row_labels.append(str(row["PartShort"])+" Außen:")
            #col_labels=['Länge \n/mm','Breite /\nHöhe /mm']
            table_vals.append([round(float(v_length),1),round(float(w),1)])
        

    #Beschriftungsfeld - Frame-ID
        for frame in df1[df1["PartShort"].isin(["FL L", "FL R", "FL O", "FL U"])&df1["EdgePos"].isin(["IN"])].sort_values(by=['Frame'])["Frame"].drop_duplicates():
            x_pos=df1[df1["Frame"].isin([frame])&df1["EdgePos"].isin(["IN"])].sort_values(by=['Frame'])[["X1","X2"]].mean().mean()
            y_pos=df1[df1["Frame"].isin([frame])&df1["EdgePos"].isin(["IN"])].sort_values(by=['Frame'])[["Y1","Y2"]].mean().mean()
            ax.text(x_pos,y_pos,str(frame),fontsize=18, 
                        fontstretch="ultra-condensed", fontweight="bold",horizontalalignment="center",
                        verticalalignment="center")
            
            
            #Tabelleneintrag Flügel Außen pro Frame
            h=df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL O"])&df1["EdgePos"].isin(["OUT"])][["Y1","Y2"]].to_numpy()-df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL U"])&df1["EdgePos"].isin(["OUT"])][["Y2","Y1"]].to_numpy()
            w=df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL R"])&df1["EdgePos"].isin(["OUT"])][["X1","X2"]].to_numpy()-df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL L"])&df1["EdgePos"].isin(["OUT"])][["X2","X1"]].to_numpy()
            row_labels.append("FL"+str(frame)+" Außen: ")
            if h[0][0]==h[0][1] and w[0][0]==w[0][1]:
                h=h[0][0]
                w=w[0][0]
                table_vals.append([round(float(h),1),round(float(w),1)])
            else:
                table_vals.append([str(round(float(h[0][0]),1))+"\n"+str(round(float(h[0][1]),1)),str(round(float(w[0][0]),1))+"\n"+str(round(float(w[0][1]),1))])

            #Tabelleneintrag Flügel Innen pro Frame
            h=df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL O"])&df1["EdgePos"].isin(["IN"])][["Y1","Y2"]].to_numpy()-df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL U"])&df1["EdgePos"].isin(["IN"])][["Y2","Y1"]].to_numpy()
            w=df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL R"])&df1["EdgePos"].isin(["IN"])][["X1","X2"]].to_numpy()-df1[df1["Frame"].isin([frame])&df1["PartShort"].isin(["FL L"])&df1["EdgePos"].isin(["IN"])][["X2","X1"]].to_numpy()
            row_labels.append("FL"+str(frame)+" Innen: ")
            if h[0][0]==h[0][1] and w[0][0]==w[0][1]:
                h=h[0][0]
                w=w[0][0]
                table_vals.append([round(float(h),1),round(float(w),1)])
            else:
                table_vals.append([str(round(float(h[0][0]),1))+"\n"+str(round(float(h[0][1]),1)),str(round(float(w[0][0]),1))+"\n"+str(round(float(w[0][1]),1))])

                
                
            
        #Tabelle erstellen
        #4x1 Figure, Tabelle ist in vierter Figure-Spalte
        ax2=fig.add_subplot(1,5,(5,5))
        the_table = ax2.table(cellText=table_vals,colWidths = [0.2]*4,rowLabels=row_labels,colLabels=col_labels,loc='center')
        the_table.auto_set_font_size(False)
        the_table.set
        the_table.scale(3,1.5)
        plt.rcParams.update({'font.size': 16})
        for (row, col), cell in the_table.get_celld().items():
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))
        
        
        
        #Infotext für Bemaßungshinweis
        x_text="Hinweis: Rahmenmaße rechts und unten /\nFlügelmaße links und oben"
        ax.text(0,y_minmin-2*dist,x_text,fontsize=16, fontstretch="ultra-condensed",
                 fontweight="bold",ha="center", rotation=0,ma="left", verticalalignment="bottom")

        
        ax.set_aspect('equal')
        #fig.set_size_inches(19.5,10.5,forward=True)
        ax.set_ylim([y_minmin,y_maxmax])
        ax.set_xlim([x_minmin,x_maxmax])
        ax.set_title('Kd.Pos.: '+Pos+"\n\n",fontsize=18)
        plt.axis('off')
        
        ax.axis("off")
        ax2.axis("off")
        #fig.set_size_inches(w,h,forward=true/false)
        fig.set_size_inches(20.5,10.5,forward=True)
        
        plt.ylim([y_minmin,y_maxmax])
        plt.xlim([x_minmin,x_maxmax])
        #print(x_maxmax)
        
        #print(x_maxmax)

        
        #plt.tight_layout()

        fig.savefig(str(foldername)+"/"+"Pos "+str(Pos),bbox_inches="tight",dpi=150)
        
        #Debugging-Option - nur begrenzte Anzahl Bilder erzeugen und anzeigen
        #if int(OrderPosNo.text) == 1:
        #    break
        #plt.show()

        #plt.close()


