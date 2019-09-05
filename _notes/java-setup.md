---
layout: post
title: Java Setup
tags: [java, setup]
language: en
---

<p class="lead">
  The setup I should follow when setting up a Java project with Spring. As I
  rarely use Java for non-web stuff, the use of Spring is a given.
</p>

<hr />

Use [Spring Boot](https://spring.io/projects/spring-boot) and
[start.spring.io](https://start.spring.io) to create a project.

Use [spring-javaformat](https://github.com/spring-io/spring-javaformat) to
prettify the code and use Spring
[Checkstyle](https://checkstyle.sourceforge.io) coding standards. The IntelliJ
IDEA plugin has to be downloaded manually and installed from a JAR file. Configure Checkstyle using
the following `checkstyle.xml`:

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="com.puppycrawl.tools.checkstyle.Checker">
  <module name="io.spring.javaformat.checkstyle.SpringChecks">
    <property name="headerType" value="unchecked"/>
    <property name="projectRootPackage" value="com.example"/>
  </module>
</module>
```

And suppress the following checks with `suppressions.xml`:

```xml
<?xml version="1.0"?>
<!DOCTYPE suppressions PUBLIC
  "-//Checkstyle//DTD SuppressionFilter Configuration 1.2//EN"
  "https://checkstyle.org/dtds/suppressions_1_2.dtd">
<suppressions>
  <suppress checks="SpringImportOrder"/>
  <suppress checks="AvoidStarImport"/>
</suppressions>
```
