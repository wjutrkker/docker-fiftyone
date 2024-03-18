FROM voxel51/fiftyone:latest



#sudo docker build -t fiftyone:latest .
#sudo docker run -it --gpus 2 --ipc=host -p 5151:5151 -v /data3/backups/ceder:/data voxel51/fiftyone:latest:latest 
# sudo docker run -it --gpus 2 --ipc=host -p 5151:5151 --entrypoint bash -v /data3/backups/ceder:/data pol-fiftyone:latest ipython3 /data/fiftyoneTrain.py