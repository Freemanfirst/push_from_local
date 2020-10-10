set nocompatible  "去除VI一致性，必须要添加
filetype off      "必须要添加   

" 设置包括vundle和初始化相关的runtime path
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" 请将安装插件的命令放在vundle#begin和vundle#end之间

" 开始配置
"
" YouCompleteMe:语句补全插件
set runtimepath+=~/.vim/bundle/YouCompleteMe
autocmd InsertLeave * if pumvisible() == 0|pclose|endif "离开插入模式后自动关闭预览窗口
let g:ycm_collect_identifiers_from_tags_files = 1   " 开启YCM基于标签引擎
let g:ycm_collect_identifiers_from_comments_and_strings = 1 " 注释与字符串中的内容也用于补全
let g:syntastic_ignore_files=[".*\.py$"]
let g:ycm_seed_identifiers_with_syntax = 1     " 语法关键字补全
let g:ycm_complete_in_comments = 1
let g:ycm_confirm_extra_conf =  0             " 关闭加载.ycm_extra_conf.py提示
let g:ycm_key_list_select_completion = ['<c-n>','<Down>'] " 映射按键，如没有会拦截调tab，导致其他插件的tab不能用
let g:ycm_key_list_previous_completion=['<c-p>','<Up>']
let g:ycm_complete_in_comments=1     " 在注释输入中也能补全
let g:ycm_complete_in_strings=1      " 在字符串输入中也能补全
let g:ycm_collect_identifiers_from_comments_and_strings=1   " 注释和字符串中的文字也会被收入补全
let g:ycm_global_ycm_extra_conf='~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
let g:ycm_show_diagnostics_ui=0     " 禁用语法检查
inoremap <expr><CR> pumvisible() ? "\<C-y>":"\<CR>"       " 回车选中当前项
nnoremap <c-j> :YcmCompleter GoToDefinitionElseDeclaration<CR>     " 跳转到定义处
let g:ycm_min_num_of_chars_for_completion=2              " 从第2个键入字符就开始罗列匹配项



" github仓库中的插件
Plugin 'VundleVim/Vundle.vim'

Plugin 'vim-airline/vim-airline'
" vim-airline配置：优化vim界面
" let g:airline#extensions#tabline#enabled = 1
"
" airline设置
" 显示颜色
set t_Co=256
set laststatus=2
" 使用powerline打过补丁的字体
let g:airline_powerline_fonts = 1
" 开启tabline
let g:airline#extensions#tabline#enable = 1
" tabline中当前buffer两端的分隔字符
let g:airline#extension#tabline#left_sep = ' '
" tabline中未激活buffer两端的分隔字符
let g:airline#extensions#tabline#left_alt_sep = ' '
" tabline中buffer显示编号
let g:airline#extensions#tabline#buffer_nr_show = 1
" 映射切换buffer的键位
nnoremap [b :bp<CR>
nnoremap ]B :bn<CR>
" 映射<leader>num到num buffer
map <leader>1 :b 1<CR>
map <leader>2 :b 2<CR>
map <leader>3 :b 3<CR>
map <leader>4 :b 4<CR>
map <leader>5 :b 5<CR>
map <leader>6 :b 6<CR>
map <leader>7 :b 7<CR>
map <leader>8 :b 8<CR>
map <leader>9 :b 9<CR>


" vim-scripts 中的插件 "
Plugin 'taglist.vim'
" ctags 配置：F3快捷键显示程序中的各种tags，包括变量和函数等。
map <F3> :TlistToggle<CR>
let Tlist_Use_Right_Window=1
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
let Tlist_WinWidt=25


Plugin 'The-NERD-tree'
" NERDTree 配置：F2快捷键显示当前目录树
map <F2> :NERDTreeToggle<CR>
let NERDTreeWinSize=25

Plugin 'indentLine.vim'
Plugin 'delimitMate.vim'


" 非github仓库的插件 "
" Plugin 'git://git.wincent.com/command-t.git'
" 本地仓库的插件
"



call vundle#end()        " 必须

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""新文件标题
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"新建.c .h .sh .java文件，自动插入文件头
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.java exec ":call SetTitle()"
"定义函数SetTitle，自动插入文件头
func SetTitle()
	"如果文件类型为.sh文件
	if &filetype=='sh'
		call setline(1,"#######################################################################################")
		call append(line("."), "# File Name: ".expand("%"))
		call append(line(".")+1,"# Author: jmh")
		call append(line(".")+2,"# mail: 838616034@qq.com")
		call append(line(".")+3,"# Created Time: ".strftime("%c"))
		call append(line(".")+4,"#######################################################################################")
		call append(line(".")+5,"#!/bin/zsh")
		call append(line(".")+6,"PATH=/home/edison/bin:/home/edison/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/work/tools/gcc-3.4.5-glibc-2.3.6/bin")
		call append(line(".")+7,"export PATH")
		call append(line(".")+8,"")
	endif
	"新建文件后，自动定位到文件末尾
	autocmd BufNewFile * normal G
endfunc
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"键盘命令
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


filetype plugin indent on   " 必须 加载vim自带和插件相应的语法和文件类型相关脚本
set completeopt=longest,menu  " 打开文件类型检测，智能补全
