Step 1: Download IMD-20 Real Life Manipulated Images from [Link](http://staff.utia.cas.cz/novozada/db/).

set the dataset path in  
 ``` config.py - base_dir ``` 
for example, if you have downloaded and unzipped the IMD2020 dataset in the following directory:'/home/forgery/' then put '/home/forgery/' as the base_dir. (DO NOT put '/home/forgery/IMD2020/)

run   
  ```shell
  python python trainer.py
  ```

To evaluate the model after training, run

  ```shell
  python python evaluate.py --pretrained_model  imd_2020_best_model.pth
  ```