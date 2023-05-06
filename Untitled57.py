#!/usr/bin/env python
# coding: utf-8

# Question 1
# Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
# 

# In[1]:


def is_symmetrical(num):
    num_str = str(num)
    num_str_reversed = num_str[::-1]
    if num_str == num_str_reversed:
        return True
    else:
        return False


# In[2]:


is_symmetrical(7227)


# In[3]:


is_symmetrical(12567)


# In[4]:


is_symmetrical(44444444)


# In[5]:


is_symmetrical(9939)


# In[6]:


is_symmetrical(1112111)


# Given a string of numbers separated by a comma and space, return the product of the numbers.

# In[16]:


def multiply_nums(nums_str):
    nums_list = nums_str.split(', ')
    nums_int = [int(num) for num in nums_list]
    product = 1
    for num in nums_int:
        product *= num
    return product
        
    


# In[17]:


multiply_nums("2, 3")


# In[18]:


multiply_nums("1, 2, 3, 4")


# In[19]:


multiply_nums("54, 75, 453, 0")


# In[20]:


multiply_nums("10, -2")


# Create a function that squares every digit of a number.
# 

# In[24]:


def square_digits(num):
    digits = [int(digit) for digit in str(num)]
    squared_digits = [digit**2 for digit in digits]
    result = int(''.join(map(str, squared_digits)))
    return result


# In[25]:


square_digits(9119) 


# In[26]:



square_digits(2483)


# In[27]:


square_digits(3212)


# Create a function that sorts a list and removes all duplicate items from it.
# 

# In[28]:


def setify(lst):
    return sorted(list(set(lst)))


# In[29]:


setify([1, 3, 3, 5, 5])


# In[30]:


setify([4, 4, 4, 4])


# In[31]:


setify([5, 7, 8, 9, 10, 15])


# In[32]:


setify([3, 3, 3, 2, 1])


# Create a function that returns the mean of all digits.

# In[36]:


def mean(num):
    digits = [int(d) for d in str(num)]
    return sum(digits) // len (digits)


# In[37]:


mean(42)


# In[38]:


mean(12345)


# In[39]:


mean(666)


# In[ ]:




