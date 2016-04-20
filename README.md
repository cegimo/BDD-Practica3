# BDD-Practica3
Practica 3 Verificación y desarrollo -


Pylint report 


pylint selenium
No config file found, using default configuration
************* Module selenium
C: 32, 0: Final newline missing (missing-final-newline)
C:  1, 0: Missing module docstring (missing-docstring)
E:  1, 0: No name 'webdriver' in module 'selenium.selenium' (no-name-in-module)
W:  1, 0: Relative import 'selenium', should be 'selenium.selenium' (relative-import)
E:  2, 0: No name 'webdriver' in module 'selenium.selenium' (no-name-in-module)
C:  4, 0: Invalid constant name "driver" (invalid-name)
W:  7, 0: String statement has no effect (pointless-string-statement)
W: 10, 0: String statement has no effect (pointless-string-statement)
C: 11, 0: Invalid constant name "usuario" (invalid-name)
W: 14, 0: String statement has no effect (pointless-string-statement)
C: 15, 0: Invalid constant name "clave" (invalid-name)
W: 18, 0: String statement has no effect (pointless-string-statement)
W: 21, 0: String statement has no effect (pointless-string-statement)
C: 22, 0: Invalid constant name "tweet" (invalid-name)
W: 25, 0: String statement has no effect (pointless-string-statement)
W: 31,-1: String statement has no effect (pointless-string-statement)
W:  2, 0: Unused Keys imported from selenium.webdriver.common.keys (unused-import)


Report
======
20 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |13     |39.39 |13       |=          |
+----------+-------+------+---------+-----------+
|docstring |10     |30.30 |10       |=          |
+----------+-------+------+---------+-----------+
|comment   |1      |3.03  |0        |+1.00      |
+----------+-------+------+---------+-----------+
|empty     |9      |27.27 |9        |=          |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |6      |5        |+1.00      |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |9      |9        |=          |
+-----------+-------+---------+-----------+
|error      |2      |2        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+---------------------------+------------+
|message id                 |occurrences |
+===========================+============+
|pointless-string-statement |7           |
+---------------------------+------------+
|invalid-name               |4           |
+---------------------------+------------+
|no-name-in-module          |2           |
+---------------------------+------------+
|unused-import              |1           |
+---------------------------+------------+
|relative-import            |1           |
+---------------------------+------------+
|missing-final-newline      |1           |
+---------------------------+------------+
|missing-docstring          |1           |
+---------------------------+------------+



Global evaluation
-----------------
Your code has been rated at -2.50/10 (previous run: -2.00/10, -0.50)

