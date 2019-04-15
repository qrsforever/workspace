
## environment setup

### jupyter

```
sudo pip3 install -U jedi
sudo pip3 install -U jupyter
sudo pip3 install -U jupyter_contrib_nbextensions jupyter_nbextensions_configurator


sudo pip3 install -U jupyterthemes

sudo jupyter contrib nbextension install
sudo jupyter nbextensions_configurator enable


### 中文

sudo apt-get install font-manager

必要时: rm ~/.cache/matplotlib -fr (没作用)
```

### vim support

```
mkdir -p $(jupyter --data-dir)/nbextensions
cd $(jupyter --data-dir)/nbextensions
git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
chmod -R go-w vim_binding
jupyter nbextension enable vim_binding/vim_binding


chrome://extensions/shortcuts
UTILITY: Do nothing (disable browser shortcut - experimental) ctrl + N

```

### jedi code complete support, have some problem, don't try

```
ipython profile create

vim ~/.ipython/profile_default/ipython_config.py

c.Completer.greedy = True
c.Completer.jedi_compute_type_timeout = 400
c.Completer.use_jedi = True

```

### brower, workaround ctrl+n

```
https://www.opera.com/
wget https://download.operachina.com/pub/opera/desktop/55.0.2994.44/linux/opera-stable_55.0.2994.44_amd64.deb

jupyter notebook --notebook-dir=$currdir --browser='opera %s' >/dev/null 2>&1 &
```

## 其他

修改主题:
    https://github.com/dunovank/jupyter-themes
    jt -t oceans16 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T
    jt -t xxx -vim (使用~/.local/share/jupyter/nbextensions/vim_binding/vim_binding.css)
    jt -r (恢复)

个人爱好:insert和normal颜色互换:

vim ~/.local/share/jupyter/nbextensions/vim_binding/vim_binding.css

```css

/* Jupyter cell is in normal mode when code mirror */
.edit_mode .cell.selected .CodeMirror-focused.cm-fat-cursor {
  /* background-color: #F5F6EB; */
  background-color: #F6EBF1;
}
/* Jupyter cell is in insert mode when code mirror */
.edit_mode .cell.selected .CodeMirror-focused:not(.cm-fat-cursor) {
  /* background-color: #F6EBF1; */
  background-color: #F5F6EB;
}


/* 插入模式下， 括号看不清 */
div.CodeMirror span.CodeMirror-matchingbracket {
    color: #0000FF;
}

```
