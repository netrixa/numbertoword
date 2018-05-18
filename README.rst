
Number to word
---------------
This is a Python module to convert number (eg. 123) to word (One hundred and twenty four). 
It works for positive/floating numbers upto the range of 10 raised to power 303 (i.e. Centillion).

Installation
-------------
Please ensure that you have **updated pip** to the latest version before installing numbertoword.

You can install the module using Python Package Index using the below command.

.. code-block:: python

  pip install numbertoword

Make sure you install all requirements given in requirements.txt

.. code-block:: python

  pip install -r requirements.txt


Usage
-----
First you have to import the module using the below code.
.. code-block:: python

    from numbertoword import num2word

Then you can use the **num2word** method to convert a number to word, as shown below.

.. code-block:: python

    >>> print num2word("1234")
    One thousand, two hundred and thirty four

    >>> print(num2word('1')) 
    One

    >>> print(num2word('0.1')) 
    Zero point one


    >>> print(word_to_num('12X45'))
    Error: 12X45 is not a valid Number/Floating point number



Bugs
-----------

Please ensure that you have updated pip to the latest version before installing word2number.
     
If you find any bugs/errors in the usage of above code, please raise an issue through 'https://github.com/netrixa/numbertoword'
or send an email to fems.david@hotmail.com with a clear example that can reproduce the issue.

