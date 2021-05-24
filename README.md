# RESOURCE ARTISAN
> Artisan exists at the root of your application as the artisan script and provides a number of helpful 
> commands that can assist you while you build your application. 

## Installation 
```bash
  git+https://github.com/slavikengel/artisan
```

## Sample usage

```bash
    artisan --make lambda --name lambda_foo --url /path/to --http_method post
    artisan -m lambda -n lambda_foo -u /path/to -hm post
    
    artisan --make job --name job_foo --period 10
    artisan -m job -n job_foo -p 10
    
    artisan --make queue --name queue_foo
    artisan -m queue -n queue_foo
```

