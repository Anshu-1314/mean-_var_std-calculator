import numpy as np


def calculate(list):

  try:
    a = np.array(list).reshape(3, 3)
    mean_axis1 = np.mean(a, axis=0)
    mean_axis2 = np.mean(a, axis=1)
    mean_flattened = np.mean(a)
    var_axis1 = np.var(a, axis=0)
    var_axis2 = np.var(a, axis=1)
    var_flattened = np.var(a)
    std_axis1 = np.std(a, axis=0)
    std_axis2 = np.std(a, axis=1)
    std_flattened = np.std(a)
    max_axis1 = np.max(a, axis=0)
    max_axis2 = np.max(a, axis=1)
    max_flattened = np.max(a)
    min_axis1 = np.min(a, axis=0)
    min_axis2 = np.min(a, axis=1)
    min_flattened = np.min(a)
    sum_axis1 = np.sum(a, axis=0)
    sum_axis2 = np.sum(a, axis=1)
    sum_flattened = np.sum(a)
    
    calculations = {
      'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean_flattened],
      'variance': [var_axis1.tolist(), var_axis2.tolist(), var_flattened],
      'standard deviation': [std_axis1.tolist(),
                             std_axis2.tolist(), std_flattened],
      'max': [max_axis1.tolist(), max_axis2.tolist(), max_flattened],
      'min': [min_axis1.tolist(), min_axis2.tolist(), min_flattened],
      'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum_flattened]
    }

    return calculations
    
  except ValueError:
    raise ValueError("List must contain nine numbers.")
    
if __name__ == "__main__":
    print("enter 9 numbers")
    list = []
    for i in range (9):
        list.append(int(input()))
    calculate(list)
