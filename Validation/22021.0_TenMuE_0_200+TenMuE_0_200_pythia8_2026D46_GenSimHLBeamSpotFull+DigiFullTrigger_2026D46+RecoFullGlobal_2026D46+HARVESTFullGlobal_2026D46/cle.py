import os
import glob
for each in glob.glob('xrootd_user/seungjun/xrootd/NEW_DIRAA/'):
  root_file = ROOT.TFile(each)
  if root_file.IsZombie():
    print(each)
    os.remove(each)

for each in glob.glob('xrootd_user/seungjun/xrootd/NEW_DIRBB/'):
  root_file = ROOT.TFile(each)
  if root_file.IsZombie():
    print(each)
    os.remove(each)

for each in glob.glob('xrootd_user/seungjun/xrootd/NEW_DIRCC/'):
  root_file = ROOT.TFile(each)
  if root_file.IsZombie():
    print(each)
    os.remove(each)

