#!/usr/bin/env python
# coding: utf-8

# 
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics.

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[3]:


print(7 ** 4)


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[4]:


s = "Hi there Sam!"
s_lst = s.split()
print(s_lst)


# In[3]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[5]:


planet = "Earth"
diameter = 12742
a ="The diameter of the {0} is {1} kilometers.".format(planet, diameter)

print(a)


# In[ ]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[6]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[8]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])


# ** What is the main difference between a tuple and a list? **

# In[33]:


# Tuple is immutable
# Lists are mutable whereas tuples are immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[24]:





# In[34]:


def domainGet(domain):
  index = domain.find('@')
  return(domain[index+1:])
domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[27]:





# In[15]:


def findDog(sentence):
  if 'dog' in sentence:
    return True
  else:
    return False
findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[18]:


def countDog(sentence):
  a = sentence.split()
  count = 0
  for items in a:
    if items == 'dog':
      count += 1
  return count 
countDog('This dog runs faster than the other dog dude!')


# In[17]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[19]:


seq = ['soup','dog','salad','cat','great']
a = list(filter(lambda n : n[0] == 's', seq))
a


# In[35]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[32]:



def caught_speeding(speed, is_birthday):
    pass
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed = speed - 5
  if speed > 80:
    return "Big Ticket"
  elif speed > 60:
    return "Small Ticket"
  else:
    return "No Ticket"
caught_speeding(81,True)
caught_speeding(81,False)


# In[24]:


caught_speeding(81,True)


# In[25]:


caught_speeding(81,False)


# # Great job!
