date
ram=false

if [ $ram ]
then
	rm -f RAM/logMem.dat RAM/RAMUsage.png
	here="$(pwd)"
	(crontab -l 2>/dev/null ; echo "* * * * * bash $here/RAM/logMemLoop.sh $here/RAM") | crontab -
fi

np=6

echo "Setting the case..."
rm -rf 0 [0-9]* log.* processor* postProcessing dynamicCode
rm -rf constant/polyMesh constant/extended*
cp -r orig0 0

echo "blockMesh..."
blockMesh -dict system/blockMeshDict_coarse> log.blockMesh

for i in 1 2 3 4 5 6
do
    foamDictionary system/refineMeshDict -entry set -set c${i} > /dev/null

    topoSet > log.topoSet_c${i}
    
    echo "refineMesh c${i}"
    refineMesh -dict system/refineMeshDict -overwrite > log.refineMesh__c${i}
done

echo "surfaceFeature..."
surfaceFeatures > log.surfaceFeatures

echo "decomposePar for snappy..."
decomposePar > log.decomposePar_snappy

echo "snappyHexMesh..."
mpirun -np $np snappyHexMesh -overwrite -parallel > log.snappyHexMesh

echo "reconstructPar..."
reconstructParMesh -constant -fullMatch -mergeTol 1e-10 > log.reconstructPar_snappy

date

touch 470.foam

if [ $ram ]
then
	crontab -r
	python3 RAM/plotRAM.py
fi
