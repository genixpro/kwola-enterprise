#
#     Kwola is an AI algorithm that learns how to use other programs
#     automatically so that it can find bugs in them.
#
#     Copyright (C) 2020 Kwola Software Testing Inc.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from kwola.config.config import Configuration
from kwola.components.agents.DeepLearningAgent import DeepLearningAgent
import torch
import torch.distributed
import traceback


def runNeuralNetworkTestOnGPU(gpu, config, verbose=True):
    try:
        branchSize = 50

        agent = DeepLearningAgent(config=config, whichGpu=gpu)

        agent.initialize(branchSize, enableTraining=True)

        if verbose:
            print("Saving and loading the network to disk")
        agent.save()
        agent.load()

        if verbose:
            print("Running a test training iteration")

        batches = [agent.prepareEmptyBatch()]
        agent.learnFromBatches(batches)

        return True
    except Exception:
        traceback.print_exc()
        return False


def testNeuralNetworkAllGPUs(verbose=True):
    """
        This method is used to test whether or not the pytorch and the neural network is installed.
        If GPU's are detected, it will try to train using them, ensuring that everything is working
        there.
    """

    for batchSize in range(2, 64):
        configDir = Configuration.createNewLocalKwolaConfigDir("testing",
                                                               url="http://demo.kwolatesting.com/",
                                                               email="",
                                                               password="",
                                                               name="",
                                                               paragraph="",
                                                               enableRandomNumberCommand=False,
                                                               enableRandomBracketCommand=False,
                                                               enableRandomMathCommand=False,
                                                               enableRandomOtherSymbolCommand=False,
                                                               enableDoubleClickCommand=False,
                                                               enableRightClickCommand=False,
                                                               batch_size=batchSize
                                                               )

        config = Configuration(configDir)


        torch.distributed.init_process_group(backend="gloo",
                                             world_size=1,
                                             rank=0,
                                             init_method="file:///tmp/kwola_distributed_coordinator", )

        success = runNeuralNetworkTestOnGPU(gpu=0, config=config, verbose=verbose)

