import sys

date = sys.argv[1]

my_file = open('vectorq.exec', "w")

my_file.write("#!/bin/csh" + "\n")

my_file.write("set dir = ./test/"+ "\n")
my_file.write("set dhdir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/Geopotential" + "\n")
my_file.write("set dendir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/Densityfiles"+ "\n")
my_file.write("set auxdir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/aux/"+ "\n")
my_file.write("set outdir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/omega/"+ "\n")
my_file.write("set fileinfo = {$dir}info_pr.dat"+ "\n")
my_file.write("set filedh =  {$dhdir}/geopotential"+ date +".txt"+ "\n")
my_file.write("set filest =  {$dendir}/density"+ date+".txt"+ "\n")
my_file.write("set filestm = {$auxdir}/st0/"+ date+"_st0.dat"+ "\n")
#my_file.write("set filegrv = {$dir}ss1a2grv.txt")
my_file.write("set filequ =  {$outdir}/u/"+ date+"_qu.txt"+ "\n")
my_file.write("set fileqv =  {$outdir}/v/"+ date+"_qv.txt"+ "\n")
my_file.write("set fileqdi = {$auxdir}/qdi/"+ date+"_qdi.txt"+ "\n")
my_file.write("\n")
my_file.write("./vectorq.exe << !"+ "\n")
my_file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:"+ "\n")
my_file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:"+ "\n")
my_file.write("'$filest'	#>>>>>Escribe fichero de densidad:"+ "\n")
my_file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:"+ "\n")
my_file.write("'$filequ'	#>>>>>Escribe fichero Qu:"+ "\n")
my_file.write("'$fileqv'	#>>>>>Escribe fichero Qv:"+ "\n")
my_file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:"+ "\n")

my_file.close()



#omegainv


my_file= open('omegainv.exec', "w")

my_file.write("#!/bin/csh" + "\n")

my_file.write("set dir = ./test/"+ "\n")
my_file.write("set fileinfo = {$dir}info_pr.dat"+ "\n")
my_file.write("set auxdir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/aux/"+ "\n")
my_file.write("set outdir = /Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/omega/"+ "\n")
my_file.write("set filestm = {$auxdir}/st0/"+ date +"_st0.dat"+ "\n")
my_file.write("set fileqdi = {$auxdir}/qdi/"+ date +"_qdi.txt"+ "\n")
my_file.write("set filew =   {$outdir}w/"+ date +"_ww.txt"+ "\n")
my_file.write("\n")
my_file.write("./omegainv.exe << !"+ "\n")
my_file.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:"+ "\n")
my_file.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:"+ "\n")
my_file.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:"+ "\n")
my_file.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):"+ "\n")
my_file.write("'$filew'	#>>>>>Escribe fichero Salida W:"+ "\n")
my_file.write("!")
my_file.close()
