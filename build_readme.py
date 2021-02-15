# -*- coding: utf-8 -*-

import sys

HEADER = """

<img align="left" src="https://gist.github.com/Bhupesh-V/0246a3f681d2533d21efb1206d1ba9d4/raw/af7d53bfdbf30f725ef7ade206200086820739fd/AboutMe.gif" height="100px"> 
<div>
  <h3 align="right">wassup nerds 🖖</h3>
  <p align="right">I'm a Backend Developer and FOSS Enthusiast. I got interested in programming when I learned how a <code>for</code> loop works 😮 in 2015 and since then I got interested in CS and have never looked back. Right now I write (and work) with Python, Go, C++, Bash &amp; Javascript (in that order). I am a side-project guy, and love 💜 to be a part of programming &amp; opensource communities.</p>
</div>


---
### ⚽ My Goals 

- [ ] Launch 🚀 a SaaS.
- [ ] Get a Laptop 💻.
- [ ] Contribute to 2-3 Big FOSS Projects 🙈 (I'm lazy).
- [x] Start A Newsletter 🗞️ for my [blog](https://bhupesh-v.github.io), [Subscribe Here](https://buttondown.email/bhupesh)
- [x] Write more stuff to share my experiences 🤔 & learning (hopefully on [freeCodeCamp](https://www.freecodecamp.org/news/author/bhupesh/) & HackerNoon).


### Recent Works
<details open>
  <summary>🌟 Projects 🌟</summary>
  <table>
    <tr>
      <td valign="top" width="33%"><samp><h4 align="center">dotman</h4></samp>
        <p align="center">
        <img align="center" src="https://github.com/Bhupesh-V/dotman/blob/master/assets/dotman-logo.png" width="200"><br><br>
        <a href="https://github.com/Bhupesh-V/dotman"><b> dotman is a simple, elegant  &amp;  easy to use dotfiles manager</b></a>
        </p>
      </td>
      <td valign="top" width="33%"><samp><h4 align="center">defe</h4></samp>
        <p align="center">
        <img align="center" src="https://raw.githubusercontent.com/Bhupesh-V/defe/2836e20d0416a4232e7d7f81a7988250e1d6718d/static/images/logodefe.svg" width="100"> <br><br>
        <a href="https://github.com/Bhupesh-V/defe"><b> A tech feed aggregator for Developers  &amp; technologists</b></a>
        </p>
      </td>
      <td valign="top" width="33%"><samp><h4 align="center">Memer Action</h4></samp>
        <p align="center">
           <img align="center" src="https://github.com/Bhupesh-V/memer-action/blob/master/images/header.png?raw=true" width="178"><br><br>
           <a href="https://github.com/Bhupesh-V/memer-action"><b>A GitHub Action for Programmer Memes xD</b></a>
        </p>
      </td>
    </tr>
  </table>
</details>

<details open>
  <summary>✒️ Writeups ✒️</summary>
  <table>
    <tr>
      <td valign="top" width="50%"><b>Blogs</b>
          <ul>
            <li><a href="https://bhupesh-v.github.io/learn-how-to-use-code-snippets-vim-cowboy/">How to use code snippets in Vim like a cowboy 🤠️</a></li>
            <li><a href="https://bhupesh-v.github.io/debugging-golang-vim-neovim">Debugging Go in Vim</a></li>
            <li><a href="https://bhupesh-v.github.io/what-i-have-learned-from-blogging-so-far-retrospect//">What I have learned from blogging so far - A retrospect</a></li>
            <li><a href="https://bhupesh-v.github.io/git-cake-when-is-my-readme-birthday/">git cake: when is my README's birthday?</a></li>
          </ul>
      </td>
      <td valign="top" width="50%"><b>TIL</b>
        <ul>
          <li><a href="https://github.com/Bhupesh-V/til/blob/master/Shell/extract-file-id-from-drive-shareable-link.md">Extract file id from drive shareable link</a></li>
          <li><a href="https://github.com/Bhupesh-V/til/blob/master/Shell/print-lines-between-two-words.md">Print lines between 2 words (using grep & awk)</a></li>
          <li><a href="https://github.com/Bhupesh-V/til/blob/master/Shell/monitor-network-data-usage.md">Monitor network (data) usage</a></li>
          <li><a href="https://github.com/Bhupesh-V/til/blob/master/Shell/random-emoji-one-liner.md">Random emoji 😲 in one line</a></li>
        </ul>
      </td>
    </tr>
  </table>
</details>
"""

FOOTER="""
### What is Bhupesh upto nowadays 👀

- 🌱 I’m currently learning ...
   - Go (Golang)
- 🔭 I’m currently working on ...
    - All of my pinned projects below 👇 (& more hidden ones)
- ~_Also I am looking for some remote internship/contract work opportunities._~


### ☺️ Support
If you like my work, consider supporting me

[**PayPal**](https://paypal.me/BhupeshVarshney) | [**ko-fi**](https://ko-fi.com/bhupesh)

---
"""


def main(todays_meme):

    with open('README.md', 'w') as file:
        file.write(HEADER)
        file.write("### Today's Meme ٩(^‿^)۶\n\n")
        file.write(
            "<details open><summary><b>{0}</b></summary>\n\n".format(todays_meme[1]))
        file.write("""<table>\n<tr>\n<th valign="top" width="50%">\n""")
        file.write("""<img title="Memes here update every 69th minute, come back again for new memes ;)" alt="{title}" src="{meme}" height="50%"><br>\n""".format(
            title=todays_meme[1], meme=todays_meme[0]))
        file.write(
            """<p><strong>ℹ️ <a href="{source}">Source</a> [ Powered By 🔥 <a href="https://github.com/Bhupesh-V/memer-action">Memer Action</a> ]</strong></p>""".format(source=todays_meme[2]))
        file.write("\n</th>\n</tr>\n</table>\n</details>\n")
        file.write(FOOTER)


if __name__ == '__main__':
    # Args: [meme, title, source]
    # Run: python update_readme.py meme title source
    main(sys.argv[1:])
