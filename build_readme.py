# -*- coding: utf-8 -*-

import sys
import urllib.request
import json
import xml.etree.ElementTree as ET


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Content-Type": "application/json",
}

NS = {"ns": "http://www.w3.org/2005/Atom"}

HEADER = """

<img align="left" src="https://gist.github.com/Bhupesh-V/0246a3f681d2533d21efb1206d1ba9d4/raw/af7d53bfdbf30f725ef7ade206200086820739fd/AboutMe.gif" height="100px"> 
<div>
  <h3 align="right">wassup nerds 🖖</h3>
  <p align="right">I'm a Developer, Tech Writer and FOSS Enthusiast. I write (and work) with Python, Go, Bash &amp; Javascript (in that order).</p>
</div>


---
### ⚽ My Goals 

- [ ] Launch 🚀 a SaaS.
- [x] Get a Laptop 💻.
- [ ] Contribute to 2-3 Big FOSS Projects 🙈 (I'm lazy).
- [ ] Start A Newsletter 🗞️ for my [blog](https://bhupesh-v.github.io), [Subscribe Here](https://buttondown.email/bhupesh)
- [x] Write more stuff to share my experiences 🤔 & learning (hopefully on [freeCodeCamp](https://www.freecodecamp.org/news/author/bhupesh/) & HackerNoon).


"""

PROJECTS = """

## Recent Works
<details open>
  <summary>Some of my noticeable work <br><br></summary>
  <table>
    <tr>
      <td valign="top" width="33%"><samp><h3 align="center">dotman</h3></samp>
        <p align="center">
        <a href="https://github.com/Bhupesh-V/dotman">
           <img align="center" src="https://github.com/Bhupesh-V/dotman/blob/master/assets/dotman-logo.png" width="200"><br><br>
          <b> dotman is a simple, elegant  &amp;  easy to use dotfiles manager</b>
        </a>
        </p>
      </td>
      <td valign="top" width="33%"><samp><h3 align="center">ugit</h3></samp>
        <p align="center">
        <a href="https://github.com/Bhupesh-V/ugit">
          <img align="center" src="https://user-images.githubusercontent.com/34342551/115037937-a608d800-9eec-11eb-88a9-252da7d6f507.png" width="100"><br><br>
          <b>ugit helps you undo git commands. Your damage control git buddy. Undo from 15+ Git fuckups.</b>
        </a>
        </p>
      </td>
      <td valign="top" width="33%"><samp><h3 align="center">Memer Action</h3></samp>
        <p align="center">
          <a href="https://github.com/Bhupesh-V/memer-action">
             <img align="center" src="https://github.com/Bhupesh-V/memer-action/blob/master/images/header.png?raw=true" width="178"><br><br>
             <b>A GitHub Action for Programmer Memes xD</b>
           </a>
        </p>
      </td>
    </tr>
  </table>
</details>
"""

FOOTER="""

### What is Bhupesh upto nowadays 👀

- 🌱 I’m currently learning ...
   - Go (Golang)
<!-- - _Also I am looking for some remote internship/contract/fulltime work opportunities._ -->


### ☺️ Support
If you like my work, consider supporting me

[**PayPal**](https://paypal.me/BhupeshVarshney)

---
"""



WRITEUP_HEADER = """
<details open>
  <summary>✒️ Writeups <br><br></summary>
  <table>
    <tr>
      <td valign="top" width="50%"><b>Blogs</b>
          <ul>
"""


def request(url, data=None, method=None):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(e.reason)
        exit()
    return res


data = request("https://bhupesh-v.github.io/feed.xml")
tree = ET.fromstring(data)
entries = tree.findall("ns:entry", namespaces=NS)

def get_tils():
    data = request("https://raw.githubusercontent.com/Bhupesh-V/til/master/recent_tils.json")
    tils = json.loads(data)
    return tils

def main(todays_meme):

    with open('README.md', 'w') as file:
        file.write(HEADER)
        file.write(WRITEUP_HEADER)
        for e in entries[:4]:
            title = e.find("ns:title", namespaces=NS).text
            url = e.find("ns:id", namespaces=NS).text
            summary = e.find("ns:summary", namespaces=NS).text
            file.write(f"""<li><a title="{summary}" href="{url}">{title}</a></li>""")
        file.write("""<td valign="top" width="50%"><b>TIL</b>\n<ul>""")
        for item in get_tils()[:4]:
            file.write(f"""<li><a href="{item['url']}">{item['title']}</a></li>""")
        file.write("""</ul></td></tr></table></details>""")
        file.write(PROJECTS)
        file.write("\n\n### Today's Meme ٩(^‿^)۶\n\n")
        file.write(
            "<details open><summary><b>{0}</b></summary>\n\n".format(todays_meme[1]))
        file.write("""<table>\n<tr>\n<th valign="top" width="50%">\n""")
        file.write("""<img title="Memes here update every 24hrs, come back tommorrow for new meme ;)" alt="{title}" src="{meme}" height="50%"><br>\n""".format(
            title=todays_meme[1], meme=todays_meme[0]))
        file.write(
            """<p><strong>ℹ️ <a href="{source}">Source</a> [ Powered By 🔥 <a href="https://github.com/Bhupesh-V/memer-action">Memer Action</a> ]</strong></p>""".format(source=todays_meme[2]))
        file.write("\n</th>\n</tr>\n</table>\n</details>\n</ul></td>")
        file.write(FOOTER)


if __name__ == '__main__':
    # Args: [meme, title, source]
    # Run: python update_readme.py meme title source
    main(sys.argv[1:])
