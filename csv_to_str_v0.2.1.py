import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from os.path import join
from glob import iglob

def convert_files():
    step1 = int(var_step1.get())
    step2 = entry_step2.get()
    step3 = entry_step3.get()
    
    if step1 in (1, 2):
        product_path = step2
        input_files = sorted(list(iglob(join(product_path, '**', '*.csv'), recursive=True)))
        export_path = step3
        
        for i in input_files:
            file_name = os.path.basename(i)
            date = "20" + file_name[0:6]
            df = pd.read_csv(product_path + file_name, header= None, dtype={4 : 'string'})
            dummy_row = df.iloc[0,:]
            dummy_row.loc[4] = 'dummy'
            Dummy_row_T = pd.DataFrame(dummy_row).T
            df = pd.concat([Dummy_row_T, df], ignore_index=True)
            df[5] = date
            df[5] = pd.to_datetime(df[5], format='%Y%m%d').dt.strftime('%d/%m/%Y')
            df[6] = file_name
            if step1 == 1:
                df[7] = "KTC"
            elif step1 == 2:
                df[7] = "TP"
                
            df.columns = range(df.shape[1])
            zeros = pd.DataFrame([[0, 0, 0, 'd:/tp_mine_svy_rb.ssi', 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
            head = pd.DataFrame(zeros)
            data = pd.concat([head, df], ignore_index=True)
            str_data = data[[4, 1, 2, 3, 4, 0, 5, 6, 7]]
            str_data.to_csv(export_path + file_name[0:-4] + " L1.csv", index=False, header=False)
            status_label.config(text=file_name + " successfully converted!")
            
        print("Processing for renumber string codes")
        print("------------------------------------")
        print("------------------------------------")
        Loading_Point = (['1429','1427','1431','1430','1422', '1340', '1346', '1423', '1342', '1345', '1344', '1321', '1320', '1333', '1421', '1424', '1324', '1319', '1419', 'EX1502', '1309', '1432', '1428'])
        BM = (['B31A', 'B31B', 'B21A', 'B21B','UY5','AA1', 'AA2','UY1', 'UY2', 'BM', 'BM1', 'BM.01', 'CEK BTS', 'P1', 'P01', 'P2', 'P02', 'A01', 'A02', 'DN1', 'DN2', 'DN01', 'DN02', 'W3', 'E2', 'W-3', 'E-2', 'E.2', 'SS2.N', 'A-O1', 'SS2', 'W-3', 'A-01', 'P-1', 'P1A', 'P1B', 'AS-01', 'MON1', 'E40.1A', 'SS02', 'C1' , 'C2', 'LS'])
        AIR = (['AIR'])
        DSP = (['DSP'])
        ELV = (['ELV', 'CEK', 'CEK ELV', 'SAM', 'elv'])
        BOR = (['9'])
        OB = (['4'])
        nan = (['nan'])
        CREST = (['2'])
        TOE = (['3'])
        PLAN = (['C140', 'C130', 'C120', 'C110', 'C100', 'C90', 'C80', 'C70', 'C60', 'C50', 'C40', 'T140', 'T130', 'T120', 'T110', 'T100', 'T90', 'T80', 'T70', 'T60', 'T50', 'T40', 'PL', 'c140', 'c130', 'c120', 'c110', 'c100', 'c90', 'c80', 'c70', 'c60', 'c50', 'c40', 't140', 't130', 't120', 't110', 't100', 't90', 't80', 't70', 't60', 't50', 't40', 'pl']) #Plan stakeout Crest / Toe
        SAM = (['SAM'])
        LONGSOR = (['LONGSOR'])
        
        dict_tp = ([nan, Loading_Point, BM, AIR, DSP, ELV, LONGSOR, PLAN]) #dictionary kode TP
        Dict_tp = pd.DataFrame(dict_tp)
        str_tp = (['1', '1000', '500', '400', '19', '400', '1600', '300'])
        
        dict_ktc = ([nan, Loading_Point, BM, AIR, DSP, BOR, OB, ELV, CREST, TOE, SAM, LONGSOR, PLAN]) #dictionary kode KTC
        Dict_ktc = pd.DataFrame(dict_ktc)
        str_ktc = (['1', '1000', '500', '400', '19', '1500', '16', '400', '17', '18', '400', '1600', '300'])
        
        seam = (['20', '25', '25U', '25L', '29', '30', '40', '40L', '60', '70', '80',
                 '100','105', '105U', '105L', '109', '109U', '109L', '115', '116', '120' ,'120U', '120L', '122', '124','124U', '124L', '128', '130', '135', '140', '145',
                 '150', '151', '155', '155U', '155L', '165', '170', '175', '175U','175L', '175-U','175-L'])
        
        seam_dict = pd.DataFrame(seam)
        
        seam_str_ = ([
                ['612', '613', '312', '313'], #20
                ['622', '623', '322', '323'], #25
                ['622', '623', '322', '323'], ['212', '213', '112', '113'], #25U & L
                ['262', '263', '162', '163'], ['632', '633', '332', '333'], #29 & 30
                ['642', '643', '342', '343'], ['652', '653', '352', '353'], #40 & 40L
                ['162', '163', '262', '263'], ['172', '173', '272', '273'], #60 & 70
                ['182', '183', '282', '283'], #80
                
                ['652', '653', '352', '343'], #100
                ['662', '663', '362', '363'], #105
                ['662', '663', '362', '363'], ['672', '673', '372', '373'], #105 U & 105L
                ['682', '683', '382', '383'], #109
                ['682', '683', '382', '383'], ['692', '693', '392', '393'], #109 U & 109L
                ['712', '713', '412', '413'], ['722', '723', '422', '423'], #115 & 116
                ['732', '733', '432', '433'], #120
                ['732', '733', '432', '433'], ['742', '743', '442', '443'], #120 U & 120L
                ['752', '753', '452', '453'], #122
                ['762', '763', '462', '463'], #124
                ['762', '763', '462', '463'], ['772', '773', '472', '473'], #124 U & 124L
                ['782', '783', '482', '483'], ['792', '793', '492', '493'], #128 & 130 
                ['812', '813', '512', '513'], ['822', '823', '522', '523'], #135 & 140
                ['832', '833', '532', '533'], #145
                
                ['132', '133', '232', '233'], ['142', '143', '242', '243'], #151 & 153 > rev 150 & 151
                ['152', '153', '252', '253'], ['152', '153', '252', '253'], ['152', '153', '252', '253'], #155 & 155L
                ['162', '263', '262', '263'], ['172', '173', '272', '273'], #165 & 170
                ['182', '183', '282', '283'], ['182', '183', '282', '283'], ['192', '193', '292', '293'], #175, 175U & 175L
                ['182', '183', '282', '283'], ['192', '193', '292', '293'] #175U & 175L
                ])
        
        seam_str = pd.DataFrame(seam_str_)
        #20_Crf = (['S20', '20R', '20CR'])
        #20_Trf = (['20TR'])
        #20_Cfl = (['20F', '20CF'])
        #20_Tfl = (['20TF'])
        
        Crf_ = ([])
        Trf_ = ([])
        Cfl_ = ([])
        Tfl_ = ([])
            
        
        for s in seam_dict.index:
            Crf_.append([seam[s], 'S'+seam[s], 'S-'+seam[s], seam[s]+'R', seam[s]+'-R', 'S'+seam[s]+'R', 'S-'+seam[s]+'R', 'S'+seam[s]+'-R', 'S-'+seam[s]+'-R', seam[s]+'CR', seam[s]+'-CR', 'S'+seam[s]+'CR', 'S-'+seam[s]+'CR', 'S'+seam[s]+'-CR', 'S-'+seam[s]+'-CR', seam[s]+'C'])
            Trf_.append([seam[s]+'TR', seam[s]+'-TR', 'S'+seam[s]+'TR', 'S'+seam[s]+'-TR', 'S-'+seam[s]+'TR', 'S-'+seam[s]+'-TR', seam[s]+'T'])
            Cfl_.append([seam[s]+'F', seam[s]+'-F', 'S'+seam[s]+'F', 'S-'+seam[s]+'F', 'S'+seam[s]+'-F', 'S-'+seam[s]+'-F', seam[s]+'CF', seam[s]+'-CF', 'S'+seam[s]+'CF', 'S-'+seam[s]+'CF', 'S'+seam[s]+'-CF', 'S-'+seam[s]+'-CF'])
            Tfl_.append([seam[s]+'TF', seam[s]+'-TF', 'S'+seam[s]+'TF', 'S'+seam[s]+'-TF','S-'+seam[s]+'TF', 'S-'+seam[s]+'-TF'])
        
        Crf = pd.DataFrame(Crf_)
        Trf = pd.DataFrame(Trf_)
        Cfl = pd.DataFrame(Cfl_)
        Tfl = pd.DataFrame(Tfl_)
            
        raw_converted = sorted(list(iglob(join(export_path, '**', '* L1.csv'),recursive=True)))
        
        for j in raw_converted:
            file_name = os.path.basename(j)
            df = pd.read_csv(export_path + file_name, header=None)
            df[0] = df[0].astype("string")
            df[0].fillna('400', inplace=True)
            df.loc[df[0].str.contains("dummy", regex=False), 0] = "400"
            df.loc[df[0].str.contains('DSP', regex=False), 0] = "19"
            df.loc[df[0].str.contains('OB', regex=False), 0] = "19"
            df.loc[df[0].str.contains("AIR", regex=False), 0] = "400"
            df.loc[df[0].str.contains("SUMP", regex=False), 0] = "400"
            df.loc[df[0].str.contains("SOIL", regex=False), 0] = "25"
            if step1 == 1:
                for k in Dict_ktc.index:
                    df.loc[df[0].isin(dict_ktc[k]), 0] = str_ktc[k]
            else:
                for k in Dict_tp.index:
                    df.loc[df[0].isin(dict_tp[k]), 0] = str_tp[k]
            for l in Crf.index: #tiddies seam string
                df.loc[df[0].isin(Crf.iloc[l]), 0] = seam_str.iloc[l,0] #crest roof
                df.loc[df[0].isin(Trf.iloc[l]), 0] = seam_str.iloc[l,1] #toe roof
                df.loc[df[0].isin(Cfl.iloc[l]), 0] = seam_str.iloc[l,2] #crest floor
                df.loc[df[0].isin(Tfl.iloc[l]), 0] = seam_str.iloc[l,3] #toe floor
            df.to_csv(export_path + file_name, index=False, header=False)
            print(file_name + " sucessfully renumber string!")

        print("Processing for generate str and validation")
        print("------------------------------------")
        print("------------------------------------")
            
        csv_restring_files = sorted(list(iglob(join(export_path, '**', '* L1.csv'),recursive=True)))
        
        for m in csv_restring_files:
            file_name = os.path.basename(m)
            df = pd.read_csv(export_path + file_name, header=None)
            asd = df[0].dtype.kind in 'iu'
                
            if asd is True:
                df.to_csv(export_path + file_name[0:-7] + ".str", index=False, header=False)            
                print(file_name + " Generated Sucessfully!")
                os.remove(m)
            else:
                print('\x1b[6;30;42m' + file_name + " Not Valid String Number!!" + '\x1b[0m')    
    else:
        print("Error")

root = tk.Tk()
root.title("CSV to STR Converter")

# Step 1: Select Source Data
label_step1 = tk.Label(root, text="Pilih Sumber Data dengan format (PNEZS): \n1. KTC, 2. TP")
label_step1.grid(row=0, column=0)
var_step1 = tk.StringVar(root)
var_step1.set("1")
dropdown_step1 = tk.OptionMenu(root, var_step1, "1", "2")
dropdown_step1.grid(row=0, column=1)

# Step 2: Input Folder Raw Data
label_step2 = tk.Label(root, text="Input Folder Raw Data:")
label_step2.grid(row=1, column=0)
entry_step2 = tk.Entry(root)
entry_step2.grid(row=1, column=1)
button_browse_step2 = tk.Button(root, text="Browse", command=lambda: browse_folder(entry_step2))
button_browse_step2.grid(row=1, column=2)

# Step 3: Tentukan Folder untuk Export
label_step3 = tk.Label(root, text="Tentukan Folder untuk Export:")
label_step3.grid(row=2, column=0)
entry_step3 = tk.Entry(root)
entry_step3.grid(row=2, column=1)
button_browse_step3 = tk.Button(root, text="Browse", command=lambda: browse_folder(entry_step3))
button_browse_step3.grid(row=2, column=2)

# Function to browse folder and append "/" at the end
def browse_folder(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path + "/")
        
# Button to start conversion
button_convert = tk.Button(root, text="Convert Files", command=convert_files)
button_convert.grid(row=3, columnspan=3)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=4, columnspan=3)

root.mainloop()
