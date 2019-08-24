# apt-get的相关操作及原理

- apt-get是Linux下的一种简便的**安装**和**更新**软件的方法。

- 使用apt-get install 时，实际上是从镜像源上下载软件，而镜像源的软件列表就存在/var/lib/apt/lists目录下。

- /etc/apt/source.list中给出了源网站的站点

- > 1. 下载软件时，先更新本地软件列表：
  >
  >    ```
  >    sudo	apt		update
  >    ```
  >
  > 2. 再安装软件
  >
  >    ```
  >    sudo	apt		install		<软件名>
  >    ```
  >
  > - 卸载软件
  >
  >   ```
  >   sudo	apt		remove		<软件名>
  >   ```
  >
  > - 下载软件包的源码
  >
  >   ```
  >   sudo	apt		source		<源码包名>
  >   ```
  >
  > - 将系统中的所有软件包一次性升级到最新版本
  >
  >   ```
  >   sudo	apt		upgrade
  >   ```
  >
  >   ---
  >
  >   ***update仅仅是通过软件源来更新本地列表，而upgrade是对软件包进行升级***
  >
  >   ---
  >
  > - 清理所有缓存文件
  >
  >   ```
  >   sudo	apt		clean
  >   ```
  >
  > - 清理低版本的文件
  >
  >   ```
  >   sudo	apt		autoclean
  >   ```
  >
  > - 完全卸载软件，并且删除配置
  >
  >   ```
  >   sudo 	apt		--purge remove <软件名>
  >   ```

  

  

  

  