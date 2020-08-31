# mkdocs-pom-parser-plugin

A simple `mkdocs` plugin which parsers a `pom.xml` file and exposes it's values as template environment variables.
This is handy when the project which is being documented is using maven. 

NOTE: Does not support multiple `pom.xml` files, but if you are interested - feel free to contribute.

## Installation

```
pip install mkdocs-pom-parser-plugin
``` 

## Usage

Add the plugin into your `mkdocs.yml`

```
plugins:
  - pom-parser-plugin:
      path: ../pom.xml (default, assumes this is a maven project )
```

By default, the plugin will export all of the commonly used tags as template environment variables:

| pom.xml                        | template variable     |
| ------------------------------ | --------------------- |
| `project.modelVersion`         | `POM_MODEL_VERSION`   |
| `project.groupId`              | `POM_GROUP_ID`        |
| `project.artifactId`           | `POM_ARTIFACT_ID`     |
| `project.packaging`            | `POM_PACKAGING`       |
| `project.version`              | `POM_VERSION`         |
| `project.name`                 | `POM_NAME`            |
| `project.description`          | `POM_DESCRIPTION`     |
| `project.url`                  | `POM_URL`             |

In your `.md` files you can reference to generate a `dependency installation` section in your documentation:

```
    <dependency>
        <groupId>{{ POM_GROUP_ID }}</groupId>
        <artifactId>{{ POM_ARTIFACT_ID }}</artifactId>
        <version>{{ POM_VERSION }}</version>
    </dependency>
```

If you need a field which is missing from the list above - you can add it via the configuration:

```
plugins:
  - pom-parser-plugin:
      path: ../pom.xml
      additional:
        # template key: valid xpath filter
        # will become usable via {{ POM_SCM_CONNECTION }} in the template.
        SCM_CONNECTION: ./scm/connection
```


## Development

1. Run `./build.sh` or 
2. `docker-compose up` and check `localhost:8000`
3. Install locally: `pip install --user . && mkdocs build --config-file tests/resources/mkdocs.yml`

## Release

1. `./create-release.sh` to create a tag.
2. Github Actions will do the rest.
