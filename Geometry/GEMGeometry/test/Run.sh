#!/bin/bash

:<<'END'
start right now
END

echo "Start!!!! it ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rock and Roll"

sign="true"
runComparison=true
gogo=true
next=true

for ((i=0;i<6;i++));do

	if [ "$gogo" = true ];then
		cd ../../..
		scram b -j8

	fi

	if [ "$next" = true ];then
		cd Geometry/GEMGeometry/test/
	fi
#################################diffglobal####################3
	if [ "$i" = 0 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END diffglobal"
		fi

		cp -r GEMGeometryAnalyzer1.cc  GEMGeometryAnalyzer.cc
		echo "END diffglobal now go to difflocal~~~~~"
	fi



##############################difflocal##########################

	if [ "$i" = 1 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END difflocal"
		fi

		cp -r GEMGeometryAnalyzer2.cc  GEMGeometryAnalyzer.cc
		echo "END difflocal now go to anlocal~~~~~"
	fi
############################anlocal#################################

	if [ "$i" = 2 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END anlocal"
		fi

		cp -r GEMGeometryAnalyzer3.cc  GEMGeometryAnalyzer.cc
		echo "END anlocal now go to anglobal~~~~~"
	fi

###########################anglobal########################

	if [ "$i" = 3 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END anglobal"
		fi

		cp -r GEMGeometryAnalyzer4.cc  GEMGeometryAnalyzer.cc
		echo "Finsh everthing~~~~~~~~~~~~~"
	fi
##########################xxxxxxxx################3

	if [ "$i" = 4 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END anglobal"
		fi

		cp -r GEMGeometryAnalyzer5.cc  GEMGeometryAnalyzer.cc
		echo "Finsh everthing~~~~~~~~~~~~~"
	fi
#####################dxdxdxdxdxdxdxdx#########################

	if [ "$i" = 5 ];then
		if [ "$runComparison" = true -a "$sign" = true ];then
			cmsRun testGEMGeometry_cfg.py
			echo "END anglobal"
		fi

		cp -r GEMGeometryAnalyzer0.cc  GEMGeometryAnalyzer.cc
		echo "Finsh everthing~~~~~~~~~~~~~"
	fi
	done

cp -r GEMtestOutputanglobal.out /xrootd_user/seungjun/test/
cp -r GEMtestOutputanlocal.out /xrootd_user/seungjun/test/
cp -r GEMtestOutputdiffgl.out /xrootd_user/seungjun/test/
cp -r GEMtestOutputdifflo.out /xrootd_user/seungjun/test/
cp -r GEMxx.out /xrootd_user/seungjun/test/
cp -r GEMdxdx.out /xrootd_user/seungjun/test/


echo "Finsh everything~~~~~~~~~~~~~~~~"
