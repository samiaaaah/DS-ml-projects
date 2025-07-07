{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "49ccd63f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[19.53125    17.64705882 16.04938272 14.95844875]\n",
      "1.75\n",
      "1.75\n",
      "54\n",
      "50\n",
      "51.75\n"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "import numpy as np\n",
    "np_height_m=[1.6,1.7,1.8,1.9]\n",
    "np_weight_k=[50,51,52,54]\n",
    "np_weight_kg=np.array(np_weight_k)\n",
    "np_height_mtrs=np.array(np_height_m)\n",
    "bmi = np_weight_kg/np_height_mtrs**2\n",
    "# Print out bmi\n",
    "print(bmi)\n",
    "#printmeanmedian\n",
    "from statistics import mean\n",
    "print(mean(np_height_mtrs))\n",
    "from statistics import median\n",
    "print(median(np_height_mtrs))\n",
    "#printmax,min\n",
    "print(max(np_weight_kg))\n",
    "print(min(np_weight_kg))\n",
    "average = sum(np_weight_kg)/len(np_weight_kg)\n",
    "print(average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b3f68209",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 0,  1,  2,  3,  5],\n",
       "       [ 1,  3,  6, 10, 15]])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array=[[ 1,  2,  3,  4,  5,  6],\n",
    "       [ 0,  1,  2,  3,  5,  8],\n",
    "       [ 1,  3,  6, 10, 15, 21]]\n",
    "\n",
    "np_array=np.array(array)\n",
    "np_array[:,0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "edf6aa1e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1028023756.py, line 4)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[66], line 4\u001b[0;36m\u001b[0m\n\u001b[0;31m    info[:,0:1:2:3:4]\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "info=np.array([[ 1,  2,  3,  4,  5,  6],[ 0,  1,  2,  3,  5,  8],[ 1,  3,  6, 10, 15, 21]]) \n",
    "print(info)\n",
    "info[:,0:1:2:3:4]\n",
    "print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "b118c151",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12]\n",
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "info= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) \n",
    "print(info)\n",
    "print(info.reshape(3,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fd70206",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
