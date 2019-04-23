# 常用命令

## 参考

    [官网手册](https://docs.mongodb.com/manual/mongo/)
    [mongodb的安装和配置](https://blog.csdn.net/zn505119020/article/details/81331808)
    [Python mogodb](http://www.runoob.com/python3/python-mongodb.html)

## 配置文件
 
    [更多](https://docs.mongodb.com/manual/reference/configuration-options/)

    `mongod -f /etc/mongod.conf`

    默认存储路径: `/data/db`

    进入后台管理: `mongo`

## 超级用户相关:

1. 进入数据库admin

    use admin 

2. 增加或修改用户密码

    db.createUser({ user: "username", pwd: "password", roles: [{ role: "dbOwner", db: "yourdb" }] })

3. 查看用户列表

    db.system.users.find()

4. 用户认证

    db.auth('username','password')

5. 删除用户

    db.removeUser('name')

6. 查看所有用户

    show users

7. 查看所有数据库

    show dbs


## CRUD

### Create

### Read

### Update

### Delete
