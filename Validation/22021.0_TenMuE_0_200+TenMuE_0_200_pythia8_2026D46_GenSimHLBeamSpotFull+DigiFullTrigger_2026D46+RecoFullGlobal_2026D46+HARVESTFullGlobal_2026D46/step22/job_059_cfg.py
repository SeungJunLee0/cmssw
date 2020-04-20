#!/usr/bin/env python
import cPickle
process = cPickle.load(open("job_cfg.pkl")) 
process.source.fileNames = ['root://cms-xrdr.private.lo:2094//xrd//store/user/seungjun/NEW_DIRAA/step1_059.root'] 
