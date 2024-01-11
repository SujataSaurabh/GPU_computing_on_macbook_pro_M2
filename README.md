On Apple Macbook Pro M2, running a python program which would use in-built GPU is not so straightforward. 
So, I jot down the steps to enable GPU based computations on M2 Macbook Pro. 
1. Install tensorflow-metal library on macbook. OR you can install it in your Python virtual environment.

   ```
      pip3 install tensorflow-metal
   ```
2. Then try to run the python program `matrix_multiplication_using_gpu.py`. This should work.  The program also checks if GPU is available and accessible to it.  
