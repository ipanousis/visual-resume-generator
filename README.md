Graphical Resume Generator
===

Available Input Formats:
-------

* JSON (default)
```
{
	"company":"Cisco International Ltd.",
	"location":"London",
	"project":"DETL deployment automation",
	"technologies":["Ansible","Vagrant","OpenStack","Docker"],
	"start":"01/02/2015",
	"end":"01/03/2015"
}
```



Available Output Formats:

* ElasticSearch (default)

Output Stream:
-------

```
{
	<copy set of input fields>,
	"timestamp":input.start
}
{
	<copy set of input fields>,
	"timestamp":input.start+1 day
}
...
{
	<copy set of input fields>,
	"timestamp":input.end-1 day
}
{
	<copy set of input fields>,
	"timestamp":input.end
}
```

Available Graphical Configurations:

* Kibana3 (default)


Swagger API Documentation:

To see the documentation run:
```
bash ./bin/run.sh
```

and navigate on your browser to http://localhost:5000/
