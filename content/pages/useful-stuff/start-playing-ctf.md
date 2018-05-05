Title: Start Playing CTF

If you are interested in infosec and want to learn new skills, why not learn by playing? By playing CTF challenges you can learn a great deal about many different topics.

The most common CTF competition style is Jeopardy, where you have challenges from different categories such as:

## Web Application Security
Websec requires knowledge on how to exploit common injection vulnerabilities, how browser and cookies interact with the user. 

Keywords: SQL Injection, XSS, CSRF, Same Origin Policy, Cookies, Access Controls

**Resources:**  
[The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws](https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470)  
[The Browser Hacker's Handbook](https://www.amazon.com/Browser-Hackers-Handbook-Wade-Alcorn/dp/1118662091)

## Forensics
Forensics in CTF is a broad category that involves many different areas such as steganography, memory dumps, computer images or network packet capture analysis. Generally, your objective is to reveal the hidden flag that can be embedded in an image, sent over a network or used on a computer from which a memory dump has been taken. To be successful in this category, you would need to be familiar with different image and file formats, analysing network packets and carving files from memory/image dumps.  
<br />
Keywords: PCAP files, memory analysis, wireshark, volatility, carving

## Cryptography
This category can require intermediate to advanced knowledge about cryptography. You could encounter anything from simple ciphers like ceaser to breaking RSA or AES crypto.  
<br />
Keywords: Asymmetric, Symmetric, Diffe Hellman, RSA, AES, Frequency Analysis, XOR

**Resources:**  
[Cryptography I](https://www.coursera.org/learn/crypto)

## Binary Exploitation / Reversing
This category requires knowledge about decompiling Java and python applications, as well as being able to read and understand assembly code. Usually you'll find a program written in C which you will need to reverse in order to find the flag. Understanding how programs are executed and how data is stored in memory is vital for solving challenges in this category.  
<br />
Keywords: gdb, strings, linux, x86, IDA Pro, ollydb, C, assembly

## Programming
This is a very broad category and involves creating a program to automate some task in order to get the flag. An example could be a website that displays an equation which you need to solve in 3 seconds. Your assignment would be to create a program to parse the equation, calculate and get the flag.

## Mobile
Analysing mobile platforms and HTTP(s) communication between apps and their servers. 
<br />
Keywords: API endpoints, Android, iOS, jadx, jd-gui

<hr class="vdivider"/>
<br />
Usually you have a few challenges per category, rated from easy to hard. If you are just starting out then you should focus on the easy challenges first. Try solve at least one challenge per category if you can, not only will you gain more points but you will increase your overall knowledge which you can transfer into career skills.  
<br />
Another way to learn more about the different topics listed above, is to read other people's writeups. You can find writeups at [ctftime.com](ctftime.com) for each CTF competition, Github or Google. For example, ChalmersCTF's writeups can be found here: [ChalmersCTF Writeups](https://github.com/ChalmersCTF/Writeups). Writeups can be great resource for learning new tricks and reading how other people solve challenges.  
<br />
More things to be aware of is the different tools that can help you solve your challenges. The following resource contains a list of tools that many players use during competitions: [ctf-tools](https://github.com/zardus/ctf-tools). Keep in mind that these are just tools that someone else built. If you can't find a tool that solves your particular problem, you might have to build it yourself, which brings us to programming. Being able to program is not necessarily required to play CTF but it helps immensely if you can. Programming/Scripting is a very central part of CTF and infosec as a whole.  
<br />
If you are still interested in playing CTF after reading this, I suggest starting with [PicoCTF 2017](https://2017game.picoctf.com) which will introduce you to the different kind of challenges and as you progress they will become harder and harder.
<br />
Another great resource to learn from is OWASP Juice Shop. Juice Shop is a self-hosted, intentionally insecure web application that contains all the vulnerabilities listed in the OWASP Top 10. Your job is to find them and exploit them and for every vulnerability you solve, you get points.  
<br />
If you have any other questions don't hesitate to contact us!