# CONVERSION_FIELDS.py 使用指南

## 简介

CONVERSION_FIELDS.py 是一个 Python 脚本，用于在人类可读的字段名和机器可读的字段名之间进行转换。该脚本使用飞书开放平台的 API，通过更新字段名的方式在两种模式之间进行切换。

## 设计思路

该脚本的主要功能是通过读取配置文件和命令行参数，构建请求体，然后发送请求到飞书的 API，将飞书表格中的字段名从人类可读的形式转换为机器可读的形式，或者反过来。在发送请求之前，脚本会检查字段名是否存在于字段映射中，如果存在，则进行转换。

1. 读取配置文件：程序首先读取配置文件 `feishu-config.ini` 中的参数，包括应用令牌、数据表 ID、视图 ID、页标记、页大小等。
2. 构建请求体：调用 `LIST_FIELDS` 函数来获取当前的字段列表，然后根据字段映射文件构建相应的数据结构。
3. 更新字段名：程序使用 `UPDATE_FIELD` 函数来更新字段名，将人类可读的字段名转换为机器可读的字段名，或者反过来。
4. 打印处理后的数据：程序将处理后的字段名打印出来，以便用户查看。

## 使用示例

以下是一个使用示例：

```python
from CONVERSION_FIELDS import CONVERSION_FIELDS_CMD

CONVERSION_FIELDS_CMD()
```

在这个示例中，你需要在命令行中指定 `-c` 或 `-b` 选项来选择转换模式，以及其他可选的参数。

## 输入参数

CONVERSION_FIELDS_CMD 函数接受以下参数：

- `-c`, `--convert_to_machine`: 将人类可读的字段名转换为机器可读的字段名。
- `-b`, `--convert_to_human`: 将机器可读的字段名转换为人类可读的字段名。
- `--app_token` (可选): Feishu 应用的 app_token，如果未提供，将从配置文件中读取。
- `--table_id` (可选): 要添加记录的数据表的 ID，如果未提供，将从配置文件中读取。
- `--view_id` (可选): 要添加记录的视图的 ID，如果未提供，将从配置文件中读取。
- `--page_token` (可选): 分页处理时的页标记，用于继续上次的操作，如果未提供，将从配置文件中读取。
- `--page_size` (可选): 每个批次发送的记录数量，如果未提供，将从配置文件中读取。
- `--config_file` (可选): 包含配置信息的文件的路径，如果未提供，将使用默认的 'feishu-config.ini'。

## 注意事项

- 在使用此脚本之前，请确保你已经在飞书开放平台上注册了你的应

用，并获取了相应的应用令牌。
- 请确保你的配置文件中包含了正确的字段映射信息。
- 在进行字段名转换时，请确保你的数据表中不存在重名的字段，否则可能会导致转换失败。
- 请谨慎使用此脚本，因为字段名的更改可能会影响到你的其他应用或服务。

## 命令行使用示例

以下是一些命令行使用示例：

- 将人类可读的字段名转换为机器可读的字段名：

```bash
python CONVERSION_FIELDS.py -c --app_token your_app_token --table_id your_table_id
```

- 将机器可读的字段名转换为人类可读的字段名：

```bash
python CONVERSION_FIELDS.py -b --app_token your_app_token --table_id your_table_id
```

在这些示例中，你需要将 `'your_app_token'` 和 `'your_table_id'` 替换为你自己的值。