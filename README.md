# ShowMeTheCode
    Hello every one .. :) 
    These are my personal programming experiences and tricks :D
    I hope to be useful to you and if you see a mistake point here please open an issue and say it to me :)
    
## Configs:
    Introduction: 
        when we have a project and we have to publish and deploy it 
        on a vps or any machine we have a file that seperated from our code 
        and it has variables that we may change it in the future.
        so configs help us for this changing without update version of project.
    Points:
        * we must put a variable in to config file that usualy change of this doesn't change logic of code.

## Decorators in python:
    I am reading [this link](https://realpython.com/primer-on-python-decorators/) about decorators

## graylog
    - When you you want to test your graylog input try this script:
         ``` for i in {1..100} ; do echo '{"version": "1.1","host":"david.org","short_message":"A short message that helps you identify what is going on","full_message":"Backtrace here\n\nmore stuff","level":1,"_user_id":9001,"_some_info":"foo","_some_env_var":"bar"}' | nc -w 1 -u graylog.mydomain.com 12201  ; done ```

## Docker
    - Connection to postgres container and finally to the database:
        ``` 
        docker exec -it postgres psql -U postgres
        \c <database_name>
        ```
