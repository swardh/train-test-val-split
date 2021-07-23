

#Train, Test, Val split

###This is a program to move/copy files into Train, Test, Val folders.

---

Before

<pre>
Animals 
    - Cats
        - file1 
        - file2 
        - file3 
        - file4
        - file5 
        - file6 
    - Dogs
        - file1 
        - file2 
        - file3
        - file4 
        - file5 
        - file6 
</pre>

After with ttvmoveOutside.py

<pre>
Animals
    - Train 
        - Cat 
            - file1 
            - file2
            - file3
            - file4
        - Dog 
            - file1 
            - file2
            - file3
            - file4
    - Test 
        - Cat 
            - file5 
        - Dog 
            - file5 
    - Val 
        - Cat 
            - file6 
        - Dog 
            - file6 
</pre>

ttvmoveInside.py creates train, test, val folders within each of the folders that already exists.

<pre>
-Animals
    -Dog
        -train
            - file1 
            - file2
            - file3
            - file4
        -test
            - file5 
        -val
            - file6 
</pre>