
date

np=5

echo "Setting the case..."
rm -rf 0 [0-9]* log.* processor* postProcessing dynamicCode
cp -r orig0 0

echo "blockMesh..."
blockMesh -dict system/blockMeshDict_nuovo> log.blockMesh

echo "decomposePar for snappy..."
decomposePar > log.decomposePar_snappy

echo "snappyHexMesh..."
mpirun -np $np snappyHexMesh -parallel > log.snappyHexMesh

echo "reconstructPar..."
reconstructPar > log.reconstructPar_snappy

date
return

echo "renumberMesh..."
renumberMesh -noFields -overwrite > log.renumberMesh

echo "setFields..."
setFields > log.setFields

echo "decomposePar..."
decomposePar > log.decomposePar

echo "interFoam..."
mpirun -np $np interFoam -parallel > log.interFoam

echo "reconstructPar..."
reconstructPar -latestTime > log.reconstructPar

date



