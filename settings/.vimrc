set showcmd
set number
"set cursorline
set smartindent
"set nosmartindent
"set autoindent
"set cindent
set expandtab
set shiftwidth=4
set list listchars=tab:\>\-
set tabstop=4
set ignorecase
set smartcase
set incsearch
set wrapscan
set hlsearch
set belloff=all
set clipboard&
"set clipboard^=unnamedplus

filetype on
filetype plugin indent on

au FileType * setlocal formatoptions-=r
au FileType * setlocal formatoptions-=o

autocmd BufEnter *.sh  nnoremap <Space>e :!./%
autocmd FileType tex nnoremap <Space>e :!pdflatex -jobname out -interaction batchmode %
"autocmd FileType python  nnoremap <Space>e :!python3 %
autocmd BufEnter *.py  nnoremap <Space>e :!python3 %
autocmd BufEnter *.py  nnoremap <Space>r :!pypy3 %
autocmd BufEnter *.py nnoremap <Space>p :!./check_perf.sh %
autocmd BufEnter *.py nnoremap <Space>w :!/mnt/d/application/Anaconda3/python.exe %
"autocmd FileType python nnoremap <Space>c :!../tools-for-competitions/copy_and_subscribe.sh %
autocmd BufEnter *.py nnoremap <Space>s :!./run.sh
autocmd BufEnter *.py :set dictionary=~/python.dict

autocmd FileType ocaml  nnoremap <Space>e :!ocaml %
autocmd FileType java  nnoremap <Space>e :!javac %
autocmd BufEnter *.kts nnoremap <Space>e :!kotlinc -script %
autocmd BufEnter *.kt nnoremap <Space>e :!kotlinc % -include-runtime -d %:r.jar
autocmd BufEnter *.kt nnoremap <Space>r :!kotlin %:r.jar

autocmd BufEnter *.rs nnoremap <Space>e :!rustc %
autocmd BufEnter *.rs nnoremap <Space>r :!%:r

autocmd BufEnter *.m2 nnoremap <Space>e :!M2 %

autocmd BufEnter *.fsx nnoremap <Space>e :!fsharpi %
autocmd BufEnter *.fs nnoremap <Space>e :!fsharpc %
autocmd BufEnter *.fs nnoremap <Space>r :!mono %:r.exe
"autocmd BufEnter,BufNew *.fs nnoremap <Space>e :!cp % ./Program.fs;dotnet build
"autocmd BufEnter,BufNew *.fs nnoremap <Space>t :!dotnet run
"
autocmd BufEnter *.scala nnoremap <Space>e :!scala %
autocmd BufEnter *.hs nnoremap <Space>e :!stack ghci %
autocmd BufEnter *.nim nnoremap <Space>e :!nim c -o:./out -r %

"autocmd FileType cpp  nnoremap <Space>e :!g++ -O2 -Wfatal-errors --std=c++2a % -o out
"autocmd BufEnter *.cpp  nnoremap <Space>e :!g++-12 -O2 -Wfatal-errors --std=c++23 % -o out -I/user/include/eigen3
autocmd BufEnter *.cpp  nnoremap <Space>e :!g++-12 -O2 -Wfatal-errors -std=gnu++2b % -o out -I/user/include/eigen3
autocmd BufEnter *.cpp  nnoremap <Space>r :!./out
autocmd BufEnter *.cpp  nnoremap <Space>s :!./run.sh
"autocmd FileType cpp  nnoremap <Space>e :!ninja
"
"autocmd BufEnter,BufNewFile *.cs setfiletype csharp
autocmd FileType cs nnoremap <Space>e :!mcs ./% -out:%:r.exe

nnoremap <Space>x :!../tools-for-competitions/example_getter.py %
nnoremap <Space>1 :!../tools-for-competitions/checker.py % 1
nnoremap <Space>2 :!../tools-for-competitions/checker.py % 2
nnoremap <Space>3 :!../tools-for-competitions/checker.py % 3
nnoremap <Space>4 :!../tools-for-competitions/checker.py % 4
nnoremap <Space>5 :!../tools-for-competitions/checker.py % 5
nnoremap <Space>6 :!../tools-for-competitions/checker.py % 6
nnoremap <Space>7 :!../tools-for-competitions/checker.py % 7
nnoremap <Space>8 :!../tools-for-competitions/checker.py % 8
nnoremap <Space>9 :!../tools-for-competitions/checker.py % 9
nnoremap <Space>t :!../tools-for-competitions/sample_tester.py %
nnoremap <Space>c :!/mnt/d/atcoder/tools-for-competitions/copy_and_subscribe.sh %

autocmd BufReadPost *
      \ if line("'\"") >= 1 && line("'\"") <= line("$")
      \ |   exe "normal! g`\""
      \ | endif

colorscheme molokai
set showmatch

runtime snippets.vim

" Load settings for each location.
augroup vimrc-local
  autocmd!
  autocmd BufNewFile,BufReadPost * call s:vimrc_local(expand('<afile>:p:h'))
augroup END

function! s:vimrc_local(loc)
  let files = findfile('.vimrc.local', escape(a:loc, ' ') . ';', -1)
  for i in reverse(filter(files, 'filereadable(v:val)'))
    source `=i`
  endfor
endfunction
