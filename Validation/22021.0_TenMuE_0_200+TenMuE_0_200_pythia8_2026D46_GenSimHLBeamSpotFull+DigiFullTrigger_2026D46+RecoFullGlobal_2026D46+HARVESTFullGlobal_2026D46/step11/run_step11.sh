#!/bin/bash
if [ $# != 1 ]; then
    echo "JOB SECTION NUMBER IS MISSING!!!"
    exit 1
fi
SECTION=${@: -1}
FSECTION=`printf %03d $SECTION`

if [ _$CMS_PATH == _ ]; then
  export CMS_PATH=/cvmfs/cms.cern.ch
fi
source $CMS_PATH/cmsset_default.sh

hostname
whoami
tar xzf job.tar.gz
cd CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46
cd -
cd CMSSW_11_1_0_pre3/src
scram build ProjectRename
eval `scram runtime -sh`


scram build -j
cd -
cd CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46
eval `scram runtime -sh`
if [ -f $CMSSW_BASE/proxy.x509 ]; then
    export X509_USER_PROXY=$CMSSW_BASE/proxy.x509
fi


echo BEGIN `date` cmsRun job_${FSECTION}_cfg.py  #>> /cms/ldap_home/seungjun/CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46/step11/submit.log
echo cmsRun job_${FSECTION}_cfg.py 
touch ___started___job___
time cmsRun job_${FSECTION}_cfg.py 
EXITCODE=$?
if [ $EXITCODE == 0 ]; then
    echo ENDED `date` cmsRun job_${FSECTION}_cfg.py  #>> /cms/ldap_home/seungjun/CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46/step11/submit.log


else
    rm -f core.*
    echo TERMINATED_$EXITCODE `date` cmsRun job_${FSECTION}_cfg.py  #>> /cms/ldap_home/seungjun/CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46/step11/submit.log
    exit 1
fi

for FILE in step1.root; do
    EXT=${FILE##*.}
    PREFIX=${FILE%.${EXT}}
    TRANSFERCMD=(xrdcp -d 1 -f)
    DESTDIR=root://cms-xrdr.private.lo:2094//xrd/store/user/seungjun/NEW_DIRAA
    ${TRANSFERCMD[@]} ${FILE} ${DESTDIR}/${PREFIX}_${FSECTION}.${EXT}
    if [ $? -ne 0 ]; then
        echo "Failed to copy file.. retry in 5 seconds"
        sleep 5
        echo "trying: " ${TRANSFERCMD[@]} ${FILE} ${DESTDIR}/${PREFIX}_${FSECTION}.${EXT}
        ${TRANSFERCMD[@]} ${FILE} ${DESTDIR}/${PREFIX}_${FSECTION}.${EXT}
    fi
    if [ $? -ne 0 ]; then
        echo "Failed to copy file.. (trial2) retry in 30 seconds"
        sleep 30
        ${TRANSFERCMD[@]} ${FILE} ${DESTDIR}/${PREFIX}_${FSECTION}.${EXT}
    fi
done
echo FINISHED `date` # >> /cms/ldap_home/seungjun/CMSSW_11_1_0_pre3/src/Validation/22021.0_TenMuE_0_200+TenMuE_0_200_pythia8_2026D46_GenSimHLBeamSpotFull+DigiFullTrigger_2026D46+RecoFullGlobal_2026D46+HARVESTFullGlobal_2026D46/step11/submit.log
