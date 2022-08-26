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

NO_OF_BLOGS = NO_OF_TILS = 4

HEADER = """
<div>
  <h3>wassup nerds 🖖</h3>
  <p>Developer, FOSS Enthusiast & Creator living in New Delhi, India. I like to build & create stuff using Python, Go & Bash. I make Web, Tools, and Open-Source & frequently write about tech & my journey on my blog/newsletter.
  <ul>
    <li>I am a Community Admin at <a href="https://reddit.com/r/developersIndia">r/developersIndia</a> (Join us 🚀)</li>
    <li>In my free time, I am probably sleeping or reading something online.</li>
    <li>I write a lot of technical content, you can witness some of that below 👇</li>
  </ul>
</div>


---

"""

PROJECTS = """

## Recent Works
<details open>
  <summary>Some of my fun, weird & useful projects <br><br></summary>
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

### Hire Me

- [Know more about how we can collaborate professionally](https://bhupesh.me/hire)

### ☺️ Support
If you like my work, consider supporting me

[**GitHub Sponsors**](https://github.com/sponsors/Bhupesh-V/) | [**PayPal**](https://paypal.me/BhupeshVarshney)

---
"""



WRITEUP_HEADER = """
<details open>
  <summary>Recent Writeups <br><br></summary>
  <table>
    <tr>
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


def get_newsletters():
    print("Getting Newsletters")
    data = request("https://buttondown.email/bhupesh/rss")
    tree = ET.fromstring(data)
    entries = tree.findall('.//item')
    return entries

def get_blogs():
    print("Getting Blogs")
    data = request("https://bhupesh-v.github.io/feed.xml")
    tree = ET.fromstring(data)
    entries = tree.findall("ns:entry", namespaces=NS)
    return entries

def get_tils():
    print("Getting TILs")
    data = request("https://raw.githubusercontent.com/Bhupesh-V/til/master/recent_tils.json")
    tils = json.loads(data)
    return tils

def main(todays_meme):

    with open('README.md', 'w') as file:
        file.write(HEADER)
        file.write(WRITEUP_HEADER)

        file.write("""<td valign="top" width="34%"><b>Blogs</b><ul>""")
        for e in get_blogs()[:NO_OF_BLOGS]:
            title = e.find("ns:title", namespaces=NS).text
            url = e.find("ns:id", namespaces=NS).text
            summary = e.find("ns:summary", namespaces=NS).text
            file.write(f"""<li><a title="{summary}" href="{url}">{title}</a></li>""")
        file.write("""</ul></td>""")

        file.write("""<td valign="top" width="33%"><b>TIL</b>\n<ul>""")
        for item in get_tils()[:NO_OF_TILS]:
            file.write(f"""<li><a href="{item['url']}">{item['title']}</a></li>""")
        file.write("""</ul></td>""")

        file.write("""<td valign="top" width="33%"><b>Newsletter</b>\n<ul>""")
        for item in get_newsletters()[:NO_OF_TILS]:
            title = item.find(".//title").text
            link = item.find(".//link").text
            file.write(f"""<li><a href="{link}">{title}</a></li>""")
        file.write("""</ul></td>""")

        file.write("""</tr></table></details>""")

        file.write(PROJECTS)

        if todays_meme is not None:
            file.write("\n\n### Getting bored? have a meme \n\n")
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
