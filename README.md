#### **Tasks from Telecom team | Yadro Impuls 2025**

Part1 (Python скрипт): для логов использовал простой print, за тело ответа взял response.content (если правильно понял задание)

Part2 (Dockerfile): сделал небольшую оптимизацию (почистил кеш, не плодил много слоев)

Part3 (Ansible): *docker_install.yml* - устанавливаю Docker со всеми проверками
                 *build_and_run.yml* -  собираю образ и запускаю контейнер

P.S.
Задания получились интересные, узнал много нового про ansible и docker.
Столкнулся с проблемой: изменил код скрипта(изменил вывод) --> запустил плейбук build_and_run --> вывод скрипта не поменялся
Возможно ansible кеширует старую версию скрипта, если полностью удалить контейнер и образ, после сборки скрипт обновит свой вывод.
Хотелось бы получить наводку от более опытных специалистов 🤝
