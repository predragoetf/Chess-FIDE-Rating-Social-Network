#!/bin/bash

months=( "jan" "feb" "mar" "apr" "may" "jun" "jul" "aug" "sep" "oct" "nov" "dec" )
years=( "18" "17" "16" "15" "14" "13" )
#months=("jan")
#years=("18")
link="http://ratings.fide.com/download/standard_" 
postfix="frl.zip"

for year in ${years[*]}
	do
		for month in ${months[*]}
		do
			tmp_link=$link$month$year$postfix
			wget $tmp_link
			unzip -d $month$year standard_$month$year\frl.zip
		done
	done
