# LFS push failes 
If files are over 100/150 mb and pushing these files fail, often a HTTP 413 error occurs. HTTP 413 is usually a proxy or any other networking/machine limitation. To solve this issue, you can run the following command on your local machine:

        ```shell
        git config http.version HTTP/1.1
        ```


