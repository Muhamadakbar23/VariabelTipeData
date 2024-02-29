#!/usr/bin/env python
# coding: utf-8

# <h1>Variabel dan Tipe Data Python <h1><hr>
#     <font color="red">Beberapa</font> aturan pembuatan variabel di <b>python</b>:
#     
#     

# <ol>
#     <li>Bersifat case sensitif => A != a</li>
#     <li>harus diawali dengan huruf atau karakter _(underscore)</li>
#     <li>Tidak Boleh menggunakan Space</li>
#     <li>Boleh menggunakan angka</li>
#     </ol>

# In[5]:


data_int = 100
data_float = 99.9
data_string = '1'
data_bool = True

print(data_int)
print(data_float)
print(data_string)
print(data_bool)



# Untuk mengetahui tipe data dari sebuah variabel gunakan command <b>type</b>

# In[9]:


print(type(data_int))
print(type(data_float))
print(type(data_string))
print(type(data_bool))


# Pada Python terdapat proses <b>CASTING</b> yaitu konversi pada sebuah tipe data ke tipe data yang lainya yaitu dengan sintaks <b>tipe_data(nama_variabel)

# In[11]:


int_to_float = float(data_int)
int_to_string = str(data_string)
int_to_bool = bool(data_int)

print("Nilai variabel data_int=",data_int)
print(int_to_float)
print(int_to_string)
print(int_to_bool)


# In[17]:


str_to_int = int(data_int)
str_to_float =float(data_int)
str_to_bool =bool(data_int)

print("Nilai variabel data_string",data_string)
print(str_to_int)
print(str_to_float)
print(str_to_bool)


# In[19]:


float_to_int =int(data_float)
float_to_str =str(data_float)
float_to_bool =bool(data_float)

print("Nilai variabel data_float",data_float)
print(float_to_int)
print(float_to_str)
print(float_to_bool)


# In[21]:


bool_to_int =int(data_bool)
bool_to_str =str(data_bool)
bool_to_float =float(data_bool)

print("Nilai variabel data_bool",data_bool)
print(bool_to_int)
print(bool_to_str)
print(bool_to_float )


# In[2]:


bil1 = int(input("isikan bilangan 1:"))
bil2 = int(input("isikan bilangan 2:"))
hasil_tambah = bil1 + bil2
hasil_bagi = bil1 / bil2
print("Hasil Perjumlahan",hasil_tambah)
print("Hasil Pembagian",hasil_bagi)

