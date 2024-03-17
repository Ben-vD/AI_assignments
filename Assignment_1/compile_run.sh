#!/bin/bash

approach=$1
dim=$2
iterations=$3
lowerBound=$4
upperBound=$5
c1=$6
c2=$7
w=$8
evalFunc=$9
lamda=${10}
experiments=${11}


javac Main.java
##java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments

#python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=0
lamda=0.60
c1=2
c2=2
w=0.4
lowerBound=-100
upperBound=100
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=1
lamda=0.55
c1=2.550
c2=0.850
w=0.7
lowerBound=-32
upperBound=32
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=2
lamda=0
c1=2.625
c2=0.875
w=0.7
lowerBound=-10
upperBound=10
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=4
lamda=0.45
c1=1.950
c2=1.950
w=0.4
lowerBound=-100
upperBound=100
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=5
lamda=0.35
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-10
upperBound=10
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=6
lamda=0.05
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-5.12
upperBound=5.12
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=7
lamda=0.2
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-10
upperBound=10
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=8
lamda=0.5
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-100
upperBound=100
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=9
lamda=0.95
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-5
upperBound=5
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc

evalFunc=10
lamda=0.1
c1=1.496180
c2=1.496180
w=0.729844
lowerBound=-1
upperBound=1
#java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc


#evalFunc=0
#lamda=0.00
#c1=2
#c2=2
#w=0.4
#lowerBound=-100
#upperBound=100
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=1
#lamda=0.00
#c1=2.550
#c2=0.850
#w=0.7
#lowerBound=-32
#upperBound=32
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=2
#lamda=0.00
#c1=2.625
#c2=0.875
#w=0.7
#lowerBound=-10
#upperBound=10
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=4
#lamda=0.00
#c1=1.950
#c2=1.950
#w=0.4
#lowerBound=-100
#upperBound=100
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=5
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-10
#upperBound=10
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=6
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-5.12
#upperBound=5.12
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=7
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-10
#upperBound=10
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=8
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-100
#upperBound=100
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=9
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-5
#upperBound=5
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=10
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=-1
#upperBound=1
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done
#
#evalFunc=3
#lamda=0.00
#c1=1.496180
#c2=1.496180
#w=0.729844
#lowerBound=0
#upperBound=10
#while (( $(echo "$lamda <= 1.00" | bc -l) )); do
#
#    javac Main.java
#    #java Main $approach $dim $iterations $lowerBound $upperBound $c1 $c2 $w $evalFunc $lamda $experiments
#
#    #python ./Visualize.py $approach $iterations $lowerBound $upperBound $evalFunc
#    #python ./PositionTimePlots.py ./Data/particleCoordsData.txt $dim $iterations $experiments
#    python DiversityTimePlots.py $dim $iterations $experiments $approach $evalFunc
#
#    lamda=$(echo "$lamda + 0.05" | bc -l)
#done