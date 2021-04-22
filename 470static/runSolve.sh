
date

np=5

echo "Setting the case..."
rm -rf [0-9]* processor* postProcessing dynamicCode
cp -r orig0 0

echo "setFields..."
setFields > log.setFields

echo "decomposePar..."
decomposePar > log.decomposePar_solve

echo "renumberMesh..."
renumberMesh -noFields -overwrite > log.renumberMesh

echo "interFoam..."
mpirun -np $np interFoam -parallel > log.interFoam

echo "reconstructPar..."
reconstructPar -latestTime > log.reconstructPar_solve

date
