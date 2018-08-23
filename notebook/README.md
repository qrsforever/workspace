
## environment setup

### jupyter

``` 
sudo pip3 install -U jedi
sudo pip3 install -U jupyter
sudo pip3 install -U jupyter_contrib_nbextensions
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

### jedi code complete support

```
ipython profile create

vim ~/.ipython/profile_default/ipython_config.py

c.Completer.greedy = True 
c.Completer.jedi_compute_type_timeout = 400
c.Completer.use_jedi = True

```
