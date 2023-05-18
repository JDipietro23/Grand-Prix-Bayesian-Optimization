from bayes_opt import BayesianOptimization
import pandas
import subprocess

columnNames = ['Front Camber',
               'Rear Camber',
               'Front Wing Relative Angle',
               'Back Wing Relative Angle',
               'Front Suspension Stiffness',
               'Rear Suspension Stiffness' ,
               'Front Ride Height',
               'Rear Ride Height',
               'Tire Compound',
               'Engine Mode',
               'Fuel Remaining',
               'Total Tire Usage',
               'Top Speed',
               'Lap Time']

finalResults = pandas.DataFrame(columns=columnNames)

def blackBoxfunc(frontCam,rearCam,frontWing,rearWing,frontStiff,rearStiff,frontHeight,rearHeight):

    global finalResults

    #make df and initialize with vals
    initVals = {'frontCam':[frontCam],
                'rearCam':[rearCam],
                'frontWing':[frontWing],
                'rearWing':[rearWing],
                'frontStiff':[frontStiff],
                'rearStiff':[rearStiff],
                'frontHeight':[frontHeight],
                'rearHeight':[rearHeight],
                'Tire Compound':['H'],
                'Engine Mode':[3],
                'Starting Fuel':[5],
                'Laps':[1]
                }
    
    myDf = pandas.DataFrame.from_dict(initVals)
    #export as csv to current run position
    CRfilePath = "currentrun.csv"
    programFilePath = "C:\\Users\\JobiW\\Desktop\\Design, Search,Optimization\\Joe_Kasia\\Marianapolis_Grand_Prix_Run.exe"
    LRfilePath = "latestrun.csv"

    myDf.to_csv(CRfilePath, header=False, index=False)
    #run exe
    subprocess.run([programFilePath])

    #open results csv
    resultsDf = pandas.read_csv(LRfilePath)

    finalResults.loc[len(finalResults.index)] = resultsDf.columns

    return float(resultsDf.columns[-1])*-1

pbounds = {'frontCam':(0,5),
            'rearCam':(0,3),
            'frontWing':(0,10),
            'rearWing':(0,10),
            'frontStiff':(0,10),
            'rearStiff':(0,10),
            'frontHeight':(25,75),
            'rearHeight':(25,75)
            }

optimizer = BayesianOptimization(f=blackBoxfunc, pbounds=pbounds, random_state=1)

optimizer.maximize(init_points=20, n_iter=480)

finalFilePath = "finalResults.csv"

finalResults.to_csv(finalFilePath)