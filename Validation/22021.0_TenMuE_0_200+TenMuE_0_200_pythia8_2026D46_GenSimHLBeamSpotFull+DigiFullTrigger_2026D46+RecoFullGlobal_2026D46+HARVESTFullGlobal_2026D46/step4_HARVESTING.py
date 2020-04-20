# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase2_realistic_T15 -s HARVESTING:@phase2Validation+@phase2+@miniAODValidation+@miniAODDQM --scenario pp --filetype DQM --geometry Extended2026D46 --era Phase2C9 --mc -n 100 --filein file:step3_inDQM.root --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('HARVESTING',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D46Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
'''
# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring('file:step3_inDQM.root')
)
'''
from FWCore.ParameterSet import VarParsing
import os
import glob

options = VarParsing.VarParsing('analysis')
options.register(
    "inPath",
    "./step3_inDQM.root",
    VarParsing.VarParsing.multiplicity.singleton,
    VarParsing.VarParsing.varType.string,
    "a Path to a inDQM file or a directory having such files")
options.parseArguments()

if os.path.isdir(options.inPath):
    pathname = os.path.join(options.inPath, '*inDQM*.root')
    fileNames = ['file:' + each for each in glob.glob(pathname)]
    fileNames = cms.untracked.vstring(*fileNames)
else:
    fileNames = cms.untracked.vstring('file:' + options.inPath)

process.source = cms.Source("DQMRootSource",
    fileNames = fileNames
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.genHarvesting = cms.Path(process.postValidation_gen)
process.dqmHarvestingFakeHLT = cms.Path(process.DQMOffline_SecondStep_FakeHLT+process.DQMOffline_Certification)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.dqmHarvestingExtraHLT = cms.Path(process.DQMOffline_SecondStep_ExtraHLT+process.DQMOffline_Certification)
process.alcaHarvesting = cms.Path()
process.validationHarvestingNoHLT = cms.Path(process.postValidation+process.postValidation_gen)
process.validationHarvestingFS = cms.Path(process.recoMuonPostProcessors+process.postValidationTracking+process.MuIsoValPostProcessor+process.calotowersPostProcessor+process.hcalSimHitsPostProcessor+process.hcaldigisPostProcessor+process.hcalrechitsPostProcessor+process.electronPostValidationSequence+process.photonPostProcessor+process.pfJetClient+process.pfMETClient+process.pfJetResClient+process.pfElectronClient+process.rpcRecHitPostValidation_step+process.makeBetterPlots+process.bTagCollectorSequenceMCbcl+process.METPostProcessor+process.L1GenPostProcessor+process.bdHadronTrackPostProcessor+process.MuonGEMHitsPostProcessors+process.MuonGEMDigisPostProcessors+process.MuonGEMRecHitsPostProcessors+process.hgcalPostProcessor+process.MuonME0DigisPostProcessors+process.MuonME0SegPostProcessors+process.trackerphase2ValidationHarvesting+process.postValidation_gen)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationHarvesting = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.validationpreprodHarvestingNoHLT = cms.Path(process.postValidation_preprod+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.dqmHarvesting = cms.Path(process.DQMOffline_SecondStep+process.DQMOffline_Certification)
process.postValidation_common_step = cms.Path(process.postValidation_common)
process.postValidationTracking_step = cms.Path(process.postValidationTracking)
process.postValidation_muons_step = cms.Path(process.postValidation_muons)
process.postValidation_JetMET_step = cms.Path(process.postValidation_JetMET)
process.electronPostValidationSequence_step = cms.Path(process.electronPostValidationSequence)
process.photonPostProcessor_step = cms.Path(process.photonPostProcessor)
process.bTagCollectorSequenceMCbcl_step = cms.Path(process.bTagCollectorSequenceMCbcl)
process.runTauEff_step = cms.Path(process.runTauEff)
process.postValidation_HCAL_step = cms.Path(process.postValidation_HCAL)
process.hgcalValidatorPostProcessor_step = cms.Path(process.hgcalValidatorPostProcessor)
process.mtdValidationPostProcessor_step = cms.Path(process.mtdValidationPostProcessor)
process.postValidationOuterTracker_step = cms.Path(process.postValidationOuterTracker)
process.trackerphase2ValidationHarvesting_step = cms.Path(process.trackerphase2ValidationHarvesting)
process.DQMHarvestTracking_step = cms.Path(process.DQMHarvestTracking)
process.DQMHarvestOuterTracker_step = cms.Path(process.DQMHarvestOuterTracker)
process.DQMHarvestTrackerPhase2_step = cms.Path(process.DQMHarvestTrackerPhase2)
process.DQMHarvestMuon_step = cms.Path(process.DQMHarvestMuon)
process.DQMCertMuon_step = cms.Path(process.DQMCertMuon)
process.DQMHarvestHcal_step = cms.Path(process.DQMHarvestHcal)
process.DQMHarvestHcal2_step = cms.Path(process.DQMHarvestHcal2)
process.DQMHarvestEGamma_step = cms.Path(process.DQMHarvestEGamma)
process.DQMCertEGamma_step = cms.Path(process.DQMCertEGamma)
process.DQMHarvestMiniAOD_step = cms.Path(process.DQMHarvestMiniAOD)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.postValidation_common_step,process.postValidationTracking_step,process.postValidation_muons_step,process.postValidation_JetMET_step,process.electronPostValidationSequence_step,process.photonPostProcessor_step,process.bTagCollectorSequenceMCbcl_step,process.runTauEff_step,process.postValidation_HCAL_step,process.hgcalValidatorPostProcessor_step,process.mtdValidationPostProcessor_step,process.postValidationOuterTracker_step,process.trackerphase2ValidationHarvesting_step,process.DQMHarvestTracking_step,process.DQMHarvestOuterTracker_step,process.DQMHarvestTrackerPhase2_step,process.DQMHarvestMuon_step,process.DQMCertMuon_step,process.DQMHarvestHcal_step,process.DQMHarvestHcal2_step,process.DQMHarvestEGamma_step,process.DQMCertEGamma_step,process.validationHarvestingMiniAOD,process.DQMHarvestMiniAOD_step,process.dqmsave_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
